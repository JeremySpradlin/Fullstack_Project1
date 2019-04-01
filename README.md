# Udacity Fullstack ND Project 1

This is my Project 1 submission for Udacity's Fullstack Nanodegree Program.  
This project requires writing a python script that will connect to a provided
database and run queries to answer the following questions:

1) What are the most popular 3 articles of all time?

2) Who are the most popular authors of all time?

3) On which day did more than 1% of requests lead to errors?

## Installation
### Prerequisites
This script requires installing both [Virtual Box](https://www.virtualbox.org "Virtual Box")
and [Vagrant](https://www.vagrantup.com "Vagrant").  Download and install both of these
applications before continuing.  

Then, download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip "FSND-Virtual-Machine.zip").  This will give you a folder called
*FSND-Virtual-Machine* that contains the virtual machine.

As an alternative method, you can also use [GitHub](https://www.github.com "GitHub") to
fork and clone [this repository](https://github.com/udacity/fullstack-nanodegree-vm "This Repository").

Once the VM is downloaded, `cd` into the VM directory, and run the following
command:
```
vagrant up
```
This will cause Vagrant to download the VM and finish the installation.

Once  `vagrant up` has finished running, you can run `vagrant ssh` to SSH into
the VM.

### Accessing VM Files
The folder `/vagrant` on the VM is shared with the same folder on your machine,
allowing you to access and pass files between your host machine and the VM.

### Conifgure the Database
Download and unzip [this file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip "This file").
Copy the file `newsdata.sql` into your `/vagrant` directory.

`cd` into the `vagrant` directory and run the following command:
```
psql -d news -f newsdata.sql
```

To add the custom views, run the command `psql news` to access the database and
copy and paste the below views into the prompt and press `ENTER`.

### Running the script
To run the reporting script, ssh into the VM using `vagrant ssh`, `cd` to the
folder containing the project, and run the following:
```
python project1.py
```

## Views added to the source Database
The following views were added to the SQL database to help facilitate
search queries.  Copy and paste these into the `psql` prompt to load them in
a fresh database.

### requests_per_day
```
CREATE VIEW requests_per_day AS
    SELECT date(time) as request_date, count(*) as request_count
    FROM log
    GROUP BY request_date;
```
### errors_per_day
```
CREATE VIEW errors_per_day AS
    SELECT date(time) as error_date, count(*) as error_count
    FROM log
    GROUP BY error_date;
```
### error_rate
```
CREATE VIEW error_rate AS
    SELECT error_date, error_count::float/request_count::float AS error_rate
    FROM errors_per_day, requests_per_day
    WHERE error_date = request_date;
```
