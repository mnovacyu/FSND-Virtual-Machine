# "Database code" for the DB Forum.

import datetime
import psycopg2

conn = psycopg2.connect("dbname=forum")

cursor = conn.cursor()

def get_posts():
  """Return all posts from the 'database', most recent first."""
  cursor.execute("SELECT content, time FROM posts ORDER BY time desc")
  posts = cursor.fetchall()
  return posts

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  cursor.execute("INSERT INTO posts (content, time) VALUES (%s, %s)", (content, datetime.datetime.now()))
  conn.commit()