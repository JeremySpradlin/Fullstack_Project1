#!/usr/bin/env python2
#
#
#This application will utilize the python module psycopg2 to connect to a
#databse (news) and perform queries to answer the following questions:
#
#1) What are the most popular three articles of all time?
#
#2) Who are the most popular article authors of all time?
#
#3) On which days did more than 1% of requests lead to errors?
#
#
#This application will output the answers to the question to the terminal in
#a readable text format.

#Imports
import psycopg2

query1 = "select title from articles"

#FUNCTION: Takes a query string, connects to the database, runs the query string,
#and returns the results
def run_query(q_str):
    db = psycopg2.connect("dbname = news")
    c = db.cursor()
    c.execute(q_str)
    r = c.fetchall()
    db.close
    return r


results = run_query(query1)
print(results)
