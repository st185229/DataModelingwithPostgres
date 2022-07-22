# DROP TABLES

songplay_table_drop = "DROP TABLE SONGPLAYS"
user_table_drop = "DROP TABLE USERS"
song_table_drop = "DROP TABLE SONGS"
artist_table_drop = "DROP TABLE ARTISTS"
time_table_drop = "DROP TABLE TIME"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE SONGPLAYS (
    songplay_id serial PRIMARY KEY,
    start_time VARCHAR ( 50 ) UNIQUE NOT NULL,
    user_id VARCHAR ( 50 ) NOT NULL,
    level VARCHAR ( 255 )  NOT NULL,
    song_id VARCHAR ( 255 )  NOT NULL,
    artist_id VARCHAR ( 25 )  NOT NULL,
    session_id VARCHAR ( 255 )  NOT NULL,
    location VARCHAR ( 255 )  NOT NULL,
    user_agent TIMESTAMP NOT NULL)
    """)

user_table_create = ("""CREATE TABLE USERS (
    user_id serial PRIMARY KEY,
    first_name VARCHAR ( 25 ) NOT NULL,
    last_name VARCHAR ( 25 ) NOT NULL,
    gender character(1),
    level VARCHAR ( 50 ))
    """)

song_table_create = ("""CREATE TABLE SONGS (
    song_id serial PRIMARY KEY, 
    title VARCHAR (50), 
    artist_id VARCHAR ( 25 ), 
    year integer, 
    duration NUMERIC)
    """)

artist_table_create = ("""CREATE TABLE ARTISTS (
    artist_id VARCHAR ( 25 ), 
    name VARCHAR (25), 
    location VARCHAR(50), 
    latitude NUMERIC, 
    longitude NUMERIC)
    """)

time_table_create = ("""CREATE TABLE TIME(
    start_time VARCHAR (50), 
    hour VARCHAR(50), 
    day integer, 
    week integer, 
    month integer, 
    year integer, 
    weekday integer)
    """)

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create,
                        artist_table_create, time_table_create]

drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop,
                      artist_table_drop, time_table_drop]
