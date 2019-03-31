# Udacity Fullstack ND Project 1

This is my Project 1 submission for Udacity's Fullstack Nanodegree Program.  
This project requires writing a python script that will connect to a provided
database and run queries to answer the following questions:

1) What are the most popular 3 articles of all time?

2) Who are the most popular authors of all time?

3) On which day did more than 1% of requests lead to errors?

## Instructions for running the script
The script can be run by navigating to the directory containing the script
and running the script by typing `python project1.py` and hitting `ENTER`

The script works by storing three SQL queries designed to return the answers
to the 3 listed questions.  It then will run each query, and then format and
output the query results into a readable format easy for users to understand.

## Views added to the source Database
The following views were added to the SQL database to help facilitate
search queries:

### requests_per_day
```
SELECT date(time) as request_date, count(*) as request_count
    FROM log
    GROUP BY request_date;
```
### errors_per_day
```
SELECT date(time) as error_date, count(*) as error_count
    FROM log
    GROUP BY error_date;
```
### error_rate
```
SELECT error_date, error_count::float/request_count::float AS error_rate
    FROM errors_per_day, requests_per_day
    WHERE error_date = request_date;
```
