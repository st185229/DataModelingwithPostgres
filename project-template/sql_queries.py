# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAYS"
user_table_drop = "DROP TABLE IF EXISTS USERS"
song_table_drop = "DROP TABLE IF EXISTS SONGS"
artist_table_drop = "DROP TABLE IF EXISTS ARTISTS"
time_table_drop = "DROP TABLE IF EXISTS TIME"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE SONGPLAYS (
    songplay_id serial PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    user_id VARCHAR ( 50 ) NOT NULL,
    level VARCHAR ( 255 )  NOT NULL,
    song_id VARCHAR ( 255 )  ,
    artist_id VARCHAR ( 25 )  ,
    session_id INT  NOT NULL,
    location VARCHAR ( 255 )  NOT NULL,
    user_agent VARCHAR ( 255 ))
    """)

user_table_create = ("""CREATE TABLE USERS (
    user_id serial PRIMARY KEY,
    first_name VARCHAR ( 25 ) NOT NULL,
    last_name VARCHAR ( 25 ) NOT NULL,
    gender character(1),
    level VARCHAR ( 25 ))
    """)

song_table_create = ("""CREATE TABLE SONGS (
    song_id VARCHAR (25) PRIMARY KEY, 
    title VARCHAR (255) NOT NULL , 
    artist_id VARCHAR( 25 ) NOT NULL, 
    year integer, 
    duration NUMERIC)
    """)

artist_table_create = ("""CREATE TABLE ARTISTS (
    artist_id VARCHAR ( 25 ) PRIMARY KEY, 
    name VARCHAR (255), 
    location VARCHAR(50), 
    latitude NUMERIC, 
    longitude NUMERIC)
    """)

time_table_create = ("""CREATE TABLE TIME(
    start_time timestamp primary key , 
    hour integer, 
    day integer, 
    week integer, 
    month integer, 
    year integer, 
    weekday integer)
    """)

# INSERT RECORDS

songplay_table_insert = """INSERT INTO songplays(start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""

user_table_insert = """
INSERT INTO users(user_id, first_name, last_name, gender, level)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE set level = EXCLUDED.level
"""

song_table_insert = """
INSERT INTO songs(song_id, title, artist_id, year, duration)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO  NOTHING
"""

artist_table_insert = """
INSERT INTO ARTISTS (artist_id ,name ,location , latitude ,longitude  ) 
VALUES(%s, %s,%s, %s,%s)
ON CONFLICT (artist_id) DO NOTHING
"""

time_table_insert = """
INSERT INTO time(start_time, hour, day, week, month, year, weekday)
VALUES(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING
"""

# FIND SONGS

song_select = """SELECT  s.song_id songid, s.artist_id artistid 
FROM  songs s 
INNER  JOIN  artists a on s.artist_id = a.artist_id 
WHERE s.title = %s AND a.name = %s AND s.duration = %s"""

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create,
                        artist_table_create, time_table_create]

drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop,
                      artist_table_drop, time_table_drop]
