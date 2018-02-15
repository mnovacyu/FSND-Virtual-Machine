# "Database code" for the DB Forum.

import bleach
import datetime
import psycopg2

DBNAME = "forum"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  conn = psycopg2.connect(database=DBNAME)
  cursor = conn.cursor()
  cursor.execute("SELECT content, time FROM posts ORDER BY time desc")
  posts = cursor.fetchall()
  return posts
  conn.close()

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  conn = psycopg2.connect(database=DBNAME)
  cursor = conn.cursor()
  cleaned_text = bleach.clean(content)
  cursor.execute("INSERT INTO posts (content, time) VALUES (%s, %s)", (cleaned_text, datetime.datetime.now()))
  conn.commit()
  conn.close()