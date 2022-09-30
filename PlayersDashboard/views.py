from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import json
from json import dumps

from .models import PlayerStats
from .filters import PlayerFilter
from .forms import PlayerQueryForm

from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q


# Importing packages needed for regression
from .utils import get_graph, get_plot
import os

import pandas as pd
import numpy as np

from sqlalchemy import create_engine

import psycopg2


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


########################################################################################
# Create your views here.

def  homepage(request):
    
    return render(request, 'homepage.html') 

def search_player(request):

    player_objects = PlayerStats.objects.all()
    
    player_filter = PlayerFilter(request.GET, queryset=player_objects)

    context = {'filter': player_filter}
    return render(request, 'index.html', context)



def playerstable(request):
    players = PlayerStats.objects.all().values()
    template = loader.get_template('players.html')

    teams = PlayerStats.objects.values_list('tm')

    context = {
        'teams': teams,
    }

    return HttpResponse(template.render(context, request))




def get_positions_info(request):

    # all entries from our scraped data in our database 
    dataset = PlayerStats.objects.all().values()
    dataJSON = json.dumps(list(dataset))

    # list of teams
    teams = PlayerStats.objects.values_list(
        'tm', flat=True).distinct().order_by('tm')
    teams = list(teams)

    # get count for each positions
    positions = PlayerStats.objects.values('pos').annotate(count=Count('pos'))
    positionsJSON = json.dumps(list(positions))
    positionDictList = json.loads(positionsJSON)
    
    pos_name_list = []
    pos_count_list = []
    for person in positionDictList:
        position = person['pos']
        counts = person['count']
    
        pos_name_list.append(position)
        pos_count_list.append(counts)
   
    pos_count_dict = dict(zip(pos_name_list, pos_count_list))
    
    labels, values = zip(*pos_count_dict.items())
    

    template = loader.get_template('pie.html')
    context = {
        'dataset': dataset,
        'teams': teams,
        'pos_count_dict': pos_count_dict,
        'dataJSON': dataJSON,
        'labels':labels,
        'values':values,
    }

    return HttpResponse(template.render(context, request))


def get_regression(request):
    
    user = os.getenv('admin_user')
    password = os.getenv('db_password')

    # initialize connection string
    connection_string = "postgresql://{user}:{password}@localhost/NBA_Stats".format(user=user, password=password)
    
    # Create engine for postgresql conneciton
    engine = create_engine(connection_string)

    # connect engine to PostgreSQL server
    conn = engine.connect()
    
    # read sql table into dataframe
    df = pd.read_sql('SELECT * FROM player_stats', conn)
    
    # drop 0's since it doesn't affect our regression 
    indx = df[df['three_pt'] == 0].index
    df = df.drop(indx)
    
    # input features of dataset 
    # Log Transformed Linear Regression
    X_log = np.log(df['three_pt'].values.reshape(-1,1))

    # Output or Predicted Value of data
    y_log = df['mp'].values.reshape(-1,1)

    # Split the data into training/testing sets
    X_train_log, X_test_log, y_train_log, y_test_log = train_test_split(
    X_log, y_log, test_size= 0.20, random_state=85)
    
    # Create linear regression object
    regr = linear_model.LinearRegression()
    
    # Train the model using the training sets
    regr.fit(X_train_log, y_train_log)
    
    # Make predictions using the testing set
    y_pred_log = regr.predict(X_test_log)
    
    # our LR model's coefficient 
    coef_log_transf = regr.coef_
    coef_log_transf = coef_log_transf.item(0)
    coef_log_transf = round(coef_log_transf, 2)
    coef_log_transf = str(coef_log_transf)

    
    model_title = 'Log-Transfromed Regression \n (3 Points Made vs Minutes Played)'
    xlabel = '3 Pointers Log-Transformed'
    log_transf_chart = get_plot(X_test_log,y_test_log, y_pred_log, model_title, xlabel, coef_log_transf)
    
    # ---------------- Ordinary Linear Regression ----------------
    X = (df['three_pt'].values.reshape(-1,1))

    # Output or Predicted Value of data
    y = df['mp'].values.reshape(-1,1)

    # Split the data into training/testing sets
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size= 0.20, random_state=85)
    
    # Create linear regression object
    regr = linear_model.LinearRegression()
    
    # Train the model using the training sets
    regr.fit(X_train, y_train)
    
    # Make predictions using the testing set
    y_pred = regr.predict(X_test)
    
    # our LR model's coefficient 
    coef_OLS = regr.coef_
    coef_OLS = coef_OLS.item(0)
    coef_OLS = round(coef_OLS, 2)
    coef_OLS = str(coef_OLS)
    
    model_title = 'Linear Regression \n (3 Points Made vs Minutes Played)'
    xlabel = '3 Pointers'
    ols_chart = get_plot(X_test,y_test, y_pred, model_title, xlabel, coef_OLS)
    
    template = loader.get_template('dashboard_analysis.html')
    context = {'log_transf_chart' : log_transf_chart,
               'ols_chart': ols_chart,
               }
    
    return HttpResponse(template.render(context, request))





