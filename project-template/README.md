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
### Step 2
At the terminal run create_tables.py
This has three functions 
1. Create database :- The create_database routine create the spartifydb database.
The databse is dropped first if exists
```python
cur.execute("DROP DATABASE IF EXISTS sparkifydb")
```
*Note that a student user has to be created manually who has db admin privileges*
*Note Auto commit of transactions are set as True, means all CRUD operations are committed automatically 
2. Drop tables <br>
*This runs each and every drop table query from sql_queries.py*
1. Create tables <br>
   *This runs each and every drop table query from sql_queries.py*
### Step 3 First Level Testing
The first level testing can be done through the jupyter notebook  etl.ipynb
This does the following 
1. Process song_data
In this first part, an ETL was performed on  dataset, song_data, to create the songs and artists dimensional tables.  The  get_files function provided  to get a list of all song JSON files in data/song_data and loaded one sample record into song table
2. Similar to song table, the artists table is also populated with one record
3. Also time and users table
4. The songplay table is populated at the last 
### ETL of bulk load
The etl.py do the ETL of the entire fileset 
