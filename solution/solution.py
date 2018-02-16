import psycopg2

db = psycopg2.connect(database="news")
c = db.cursor()

# Most popular three articles of all time
c.execute("SELECT articles.title, count(log.path) AS views "
  "FROM log "
  "JOIN articles ON log.path LIKE CONCAT('%', articles.slug, '%') "
  "WHERE log.status = '200 OK' "
  "GROUP BY articles.title "
  "ORDER BY views desc "
  "LIMIT 3;")
articles = c.fetchall()

print("Most popular three articles of all time:")
for article, views in articles:
  print ("\"" + article + "\" -- " + str(views) + " views")

# Most popular article authors of all time
c.execute("SELECT authors.name, subquery1.views "
  "FROM authors, "
  "(SELECT articles.author AS author, count(log.path) AS views "
  "FROM log "
  "JOIN articles ON log.path LIKE CONCAT('%', articles.slug, '%') "
  "WHERE log.status = '200 OK' "
  "GROUP BY articles.author "
  "ORDER BY views desc) subquery1 "
  "WHERE authors.id = subquery1.author;")
authors = c.fetchall()

print("\nMost popular authors of all time:")
for author, views in authors:
  print (author + " -- " + str(views) + " views")

db.close()

# On which days did more than 1% of requests lead to errors