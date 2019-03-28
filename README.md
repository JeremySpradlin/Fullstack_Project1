Added View: requests_per_day
    Query: SELECT date(time) as thedate, count() as num
    FROM log
    GROUP BY thedate;
