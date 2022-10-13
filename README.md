# Django-NBA-Analytics-Automation

This project uses the Django framework to collect NBA data from 'https://www.basketball-reference.com/' through an automated process with Python's Scrapy library. 
Essentially the app has a data pipeline that extract relevant NBA player stats then transforms the data into a database table where it then loads the relevant data to 
be analyzed and used to train our predictive model of figuring out how many minutes a player will be given based on their core stats throughout the season. 
The app also has an interactive query filter where end user's can search specific players stats based on their name, team, or position played.
