import glob
import os

import pandas as pd
import psycopg2

from sql_queries import *
from credentials import *


def process_song_file(cur, filepath):
    """
    This function process song file and intsert them into the song table , it also extracts the artist info and
    insert into artist table
    Parameters
    ----------
    cur: str
        database cursor
    filepath: str
        the file to be loaded
    Returns
    -------
    void
        Returns nothing
     """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[[
        'song_id',
        'title',
        'artist_id',
        'year',
        'duration'
    ]].values[0]
    cur.execute(song_table_insert, song_data)

    # insert artist record
    artist_data = df[[
        'artist_id',
        'artist_name',
        'artist_location',
        'artist_latitude',
        'artist_longitude'
    ]].values[0]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Populates time, user and songplay table
    Parameters
    ----------
    cur: str
        database cursor
    filepath: str
        the file to be loaded
    Returns
    -------
    void
        Returns nothing
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')

    # insert time data records
    time_data = pd.concat([
        t,
        t.dt.hour,
        t.dt.day,
        t.dt.isocalendar().week,
        t.dt.month,
        t.dt.year,
        t.dt.weekday], axis=1)
    column_labels = [
        'start_time',
        'hour',
        'day',
        'week',
        'month',
        'year',
        'weekday'
    ]
    time_df = pd.DataFrame(data=time_data.values, columns=column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (
            pd.to_datetime(row.ts, unit='ms'),
            row.userId,
            row.level,
            songid,
            artistid,
            row.sessionId,
            row.location,
            row.userAgent
        )
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    process datafiles
    Parameters
    ----------
    cur: str
        database cursor
    conn: str
        database connection
    filepath: str
        the file to be loaded
    func:
        the lambda function which execute processing of data
    Returns
    -------
    void
        Returns nothing
    """

    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """ This is the entrypoint , Initially it connects to the database """
    # Connect to the DB
    conn = psycopg2.connect("host={} dbname={} user={} password={}".format(host, dbname,user,password))
    # Return the cursor
    cur = conn.cursor()
    # Process song data
    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    # Process log data
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    # close the connection and quit
    conn.close()


if __name__ == "__main__":
    main()
