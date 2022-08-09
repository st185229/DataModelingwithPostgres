+-# Data Modeling with Postgres
## Summary 

This project is to create and populate an RDBMS database - postgres  schema and tables. In the first part of the project , the data analysed and a set of nomralised tables are designed. 
There were two sets of data . The first is the song data and other one is the log data. These tables are tested using a sample set of data.  
Further an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL is built and tested.

*

## How to run 

The table creation script should run at first, It can be done on the python console python create_tables.py
The credentials.py holds the single file for credentials 

### Step 1

* Install Postgres
* Create postgres server  
* Note:- A student user is to be manually created 
* Create a database (here its sparkifydb)  and set it as dbname in credentials.py

```python
host="127.0.0.1"
master_db="postgres"
dbname="sparkifydb"
user="student"
password="student"
```
# Step 2
At the terminal run create_tables.py
This has three functions 
1. Create database
1. Drop tables
 