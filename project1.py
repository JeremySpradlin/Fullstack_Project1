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

query1 ='''
    select title, count(*) as num
    from articles, log
    where path like concat('%', slug)
    group by title order by num desc limit 3;
'''
query2 = '''
    SELECT name, count(*) as num
    FROM articles, authors, log
    WHERE path like concat('%', slug) and articles.author = authors.id
    GROUP BY name ORDER BY num desc;
'''


#FUNCTION: Takes a query string, connects to the database, runs the query string,
#and returns the results
def run_query(q_str):
    db = psycopg2.connect("dbname = news")
    c = db.cursor()
    c.execute(q_str)
    r = c.fetchall()
    db.close
    return r

#FUNCTION: This function will run the query results through a loop to print the
#output.
def print_results(results):
    for i in results:
        print("{0:32} {1:<10}".format(i[0], i[1]))

#FUNCTION: This function will print out the results for the first question, "What
#are the most popular 3 articles of all time?"
def most_pop_articles(q_str):
    results = run_query(q_str)
    print("What are the most popular 3 articles of all time?\n")
    print("{0:32} {1:10}".format("Title", "Views"))
    print_results(results)

#FUNCTION: This function will print out the results for the second question, "Who
#are the most popular authors of all time?"
def pop_authors(q_str):
    results = run_query(q_str)
    print("Who are the most popular authors of all time\n")
    print("{0:32} {1:10}".format("Authors", "Views"))
    print_results(results)

#Function: This function will print out the results for the third question, "On
#which day did more than 1% of requests lead to errors?"
def high_error_day(q_str):
    results = run_query(q_str)
    print("On which day did more than 1% of requests lead to errors?\n")
    print_results(results)

most_pop_articles(query1)
print("\n")
pop_authors(query2)
print("\n")
high_error_day(query1)
