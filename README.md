# Logs Analysis Project
This project's goal is to build an internal reporting tool that will use infromation from a database to discover what kind of articles the site's readers like.

The project contains three major components:
* an Ubuntu virtual machine
* a Postgres database
* a Python script for analyzing logs of the database.

## Ubuntu Virtual Machine
Prerequsites: [Vagrant 2.0.2 or higher](https://www.vagrantup.com/)\
This vm is located in the `FSND-Virtual-Machine/vagrant` subdirectory.

## Postgres Database
The `news` database contains information regarding a newspaper site. It contains articles, web server log for the site, and information about article authors.

## Python Script
The python script located under `solution/solution.py` analyzes the news data base and answers the three following questions:

1. What are the most popular three articles of all time?
1. Who are the most popular article authors of all time?
1. On which days did more than 1% of requests lead to errors?

## Usage
### Setting up the Virtual Machine & Database
1. Clone repo
1. Navigate to the `FSND-Virtual-Machine/vagrant` subdirectory
1. `vagrant up` to bring up the vm
1. `vagrant ssh` to login to the vm
1. Download and unzip the `FSND-Virtual-Machine/newsdata.zip` file from within the vm. This contains the Postgres database dump file which will create and populate the `news` database.
1. Run `psql -d news -f newsdata.sql` to populate the database

### Run Log Analysis Tool
1. From within the vm, download the `solution/solution.py` script
1. Run the script - `python3 solution.py`
1. A copy of the intended output is located in `solution/solution_output.txt`
