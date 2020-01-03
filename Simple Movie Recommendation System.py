#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Simple Movie Recommendation Engine 


# In[1]:


# Import Pandas
import pandas as pd


# In[7]:


# Load Movies Metadata
metadata = pd.read_csv("/home/garv/Desktop/movies_metadata.csv", low_memory=False)


# In[4]:


# Print the first three rows
metadata.head(3)


# In[8]:


metadata.shape


# In[5]:


# calculate C, the mean rating across all movies:
c = metadata['vote_average'].mean()
print(c)


# In[ ]:


# The average rating of a movie on IMDB is around 5.6, on a scale of 10.

# Next, let's calculate the number of votes, m, received by a movie in the 90th percentile. 
# The pandas library makes this task extremely trivial using the .quantile() method of a pandas Series:


# In[12]:


# Calculate the minimum number of votes required to be in the chart, m
m = metadata['vote_count'].quantile(0.90)
print(m)


# In[13]:


# Filter out all qualified movies into a new dataframe
q_movies = metadata.copy().loc[metadata['vote_count'] >= m]
q_movies.shape


# In[ ]:


# You use the .copy() method to ensure that the new q_movies DataFrame created is independent of 
# your original metadata DataFrame. In other words, any changes made to the q_movies DataFrame does 
# not affect the metadata.


# In[ ]:


# v is the number of votes for the movie;
# m is the minimum votes required to be listed in the chart;
# R is the average rating of the movie; And
# C is the mean vote across the whole report


# In[14]:


# Function that computes the weighted rated of the movies

def weighted_rating(x, m=m, c=c):
    v = x['vote_count']
    R = x['vote_average']
    
    # calculate based on the IDMB formula
    return (v/(v+m) * R) + (m/(m+v) * c)


# In[15]:


# Define a new features 'score' and calculate its value with 'weighted_rating()'

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)


# In[18]:


# sort movies based on score calculated
q_movies = q_movies.sort_values('score', ascending=False)

# Print the top 15 movies
q_movies[['title','vote_count','score']].head(15)


# In[ ]:




