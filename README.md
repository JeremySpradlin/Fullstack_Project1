Added Views:
requests_per_day
    SELECT date(time) as request_date, count() as request_count
    FROM log
    GROUP BY request_date;

errors_per_day
    SELECT date(time) as error_date, count() as error_count
    FROM log
    GROUP BY error_date

error_rates
    SELECT error_date, error_count::float/requests_count::float AS error_rate
    FROM errors_per_day, requests_per_day
    ORDER BY error_rate desc;
