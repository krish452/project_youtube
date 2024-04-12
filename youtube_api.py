import requests
import os
from dotenv import load_dotenv
import sqlite3

#Assigning API key
load_dotenv()
api_key = os.getenv("API_KEY")

#Pass the keyword to search
query = 'aavesham'

#Pass required number of maximum results. 
max_results = 25


url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&q={query}&part=snippet&maxResults={max_results}"
response = requests.get(url).json()
#print(response)

#Extract information about videos
def extract_details():  
    video_details = []
    for item in response['items']:
        videoId = item['id']['videoId']
        channelId = item['snippet']['channelId']
        title = item['snippet']['title']
        channel_name = item['snippet']['channelTitle']
        video_details.append({'videoId':videoId, 'channelId':channelId, 'title': title, 'channel_name': channel_name})
    return video_details



def creating_db():
    #creating a database
    con = sqlite3.connect("videos.db")

    #create cursor
    cur = con.cursor()

    #create table
    cur.execute("create TABLE if not exists videos(videoId, channelId, title, channel_name)")

    #to check if a table has been created
    #res = cur.execute("SELECT name FROM sqlite_master")
    #res.fetchone()

    con.commit()
    con.close()

def inserting_into_db(video_details):
    con = sqlite3.connect("videos.db")
    cur = con.cursor()
    cur.executemany('INSERT OR REPLACE INTO videos VALUES (:videoId, :channelId, :title, :channel_name)', video_details)
    con.commit()
    con.close()

video_details = extract_details()
creating_db()
inserting_into_db(video_details)

def viewing_db():
    con = sqlite3.connect("videos.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM videos")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    con.close()

viewing_db()




