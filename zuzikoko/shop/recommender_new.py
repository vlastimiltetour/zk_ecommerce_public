import redis
from django.http import request,response
from django.conf import settings
from .models import Product
from orders.models import OrderItem
from cart.cart import Cart
from django.shortcuts import render, redirect, get_object_or_404


#manual recommendation system
import pandas as pd
import sqlite3 
import numpy as np
from sqlite3 import *
#from sklearn.feature_extraction.text import TfidfVectorizer

'''
conn = sqlite3.connect('db.sqlite3') 
    #make a query
sql_query = pd.read_sql_query ("SELECT * FROM shop_product", conn)
df = pd.DataFrame(sql_query)

vectorizer = TfidfVectorizer(ngram_range=(1,2))
tfidf = vectorizer.fit_transform(df['name'])

def get_recommendation():
    #setup a connection
    conn = sqlite3.connect('db.sqlite3') 
    #make a query
    sql_query = pd.read_sql_query ("SELECT * FROM orders_orderitem", conn)
    df = pd.DataFrame(sql_query)
    #orders = df['product_id'].value_counts().sort_values(ascending=False).nlargest(4)
    product_id_in_order = 11
    #get orders with specific product id
    orders = df.loc[df['product_id']==product_id_in_order]['id'].values
    orders_list = np.ndarray.tolist(orders)
    similar_products = OrderItem.objects.filter(id__in=orders_list)
    #get the id of the other product which is not product id
    #recom_products = Product.objects.get(id=10)
    recom_products = Product.objects.filter(id__in=[11, 13, 10, 12])
    return recom_products


#print(get_recommendation())



def get_recommendation():
    #setup a connection
    conn = sqlite3.connect('db.sqlite3') 
    #make a query
    sql_query = pd.read_sql_query ("SELECT * FROM orders_orderitem", conn)
    df = pd.DataFrame(sql_query)
    df1 = df['product_id'].value_counts().sort_values(ascending=False).nlargest(4)
    #recom_products = Product.objects.get(id=10)
    recom_products = Product.objects.filter(id__in=[11, 13, 10, 12])
    return recom_products'''



#python recommendation engine
'''
import pandas as pd
conn = sqlite3.connect('db.sqlite3') 
    #make a query
sql_query = pd.read_sql_query ("SELECT * FROM orders_orderitem", conn)
df = pd.DataFrame(sql_query)
#machine learning library
from sklearn.feature_extraction.text import TfidfVectorizer
#initialize the class, ngram is analyzing tuples of words next to each other, increasing accuracy
vectorizer = TfidfVectorizer(ngram_range=(1,2))
#apply vectorizer to turn the set of titles to a matrix [setf]
tfidf = vectorizer.fit_transform(df["id"])
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

title = 'Košile 1'
query_vec = vectorizer.transform([title])
similarity = cosine_similarity(query_vec, tfidf).flatten()
#find the 5 most similar titles to our search term
indices = np.argpartition(similarity, -5)[-5:]
#indices in the vector of 5 most similar vector
results = df.iloc[indices].iloc[::-1] #removes the most similar
#results = df.iloc[indices]
print(results)
'''