import redis
from django.http import request,response
from django.conf import settings
from .models import Product
from orders.models import OrderItem
from cart.cart import Cart
from django.shortcuts import render, redirect, get_object_or_404



# connect to redis
r = redis.Redis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)


class Recommender:
    def get_product_key(self, id):
        return f'product:{id}:purchased_with'


    #products_bought = pairs
    def products_bought(self, products):
        products = Product.objects.all()
        product_ids = [p.id for p in products]
       
        
        for product_id in product_ids:
            for with_id in product_ids:
                # get the other products bought with each product
                if product_id != with_id:
                    # increment score for product purchased together
                    r.zincrby(self.get_product_key(product_id),1,with_id)
        return product_ids

    def suggest_products_for(self, products, max_results=6):
        product_ids = [p.id for p in products]
       
        if len(products) == 1:
            # only 1 product
            suggestions = r.zrange(self.get_product_key(product_ids[0]),0, -1, desc=True)[:max_results]
        else:
            # generate a temporary key
            flat_ids = ''.join([str(id) for id in product_ids])
            tmp_key = f'tmp_{flat_ids}'
            # multiple products, combine scores of all products
            # store the resulting sorted set in a temporary key
            keys = [self.get_product_key(id) for id in product_ids]
            r.zunionstore(tmp_key, keys)
            # remove ids for the products the recommendation is for
            r.zrem(tmp_key, *product_ids)
            # get the product ids by their score, descendant sort
            suggestions = r.zrange(tmp_key, 0, -1,desc=True)[:max_results]
            
            # remove the temporary key
            r.delete(tmp_key)

        suggested_products_ids = [int(id) for id in suggestions]
        suggested_products = list(Product.objects.filter(id__in=suggested_products_ids))
        suggested_products.sort(key=lambda x: suggested_products_ids.index(x.id))
        return suggested_products_ids

    def clear_purchases(self):
        for id in Product.objects.values_list('id', flat=True):
            r.delete(self.get_product_key(id))


#re = Recommender()
#products = OrderItem.objects.filter(order_id=128).values()
#products = Product.objects.filter(id=12)
#print(products)
#order_items = OrderItem.objects.filter(order_id=128)
#print(products)
#gpk = re.suggest_products_for(products, 4)
#print(gpk)
# recommended_products = re.suggest_products_for(['1'], 4)


#manual recommendation system
import pandas as pd
import sqlite3 
import numpy as np
from sqlite3 import *


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



'''def get_recommendation():
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