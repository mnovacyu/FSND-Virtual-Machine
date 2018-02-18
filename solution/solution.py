#!/usr/bin/python3

import psycopg2

db = psycopg2.connect(database="news")
c = db.cursor()

# Most popular three articles of all time
c.execute(
    "SELECT articles.title, count(log.path) AS views "
    "FROM log "
    "JOIN articles ON log.path LIKE CONCAT('%', articles.slug, '%') "
    "WHERE log.status = '200 OK' "
    "GROUP BY articles.title "
    "ORDER BY views desc "
    "LIMIT 3;")
articles = c.fetchall()

print("Most popular three articles of all time:")
for article, views in articles:
    print("\"" + article + "\" -- " + str(views) + " views")

# Most popular article authors of all time
c.execute(
    "SELECT authors.name, subquery1.views "
    "FROM authors, "
    "(SELECT articles.author AS author, count(log.path) AS views "
    "FROM log "
    "JOIN articles ON log.path LIKE CONCAT('%', articles.slug, '%') "
    "WHERE log.status = '200 OK' "
    "GROUP BY articles.author) subquery1 "
    "WHERE authors.id = subquery1.author "
    "ORDER BY views desc;")
authors = c.fetchall()

print("\nMost popular authors of all time:")
for author, views in authors:
    print(author + " -- " + str(views) + " views")

# On which days did more than 1% of requests lead to errors
c.execute(
    "SELECT ok.day, ((nf.num::float / (ok.num + nf.num)) * 100) as errors "
    "FROM "
    "(SELECT date_trunc('day', time)::date as day, count(status) as num "
    "FROM log "
    "WHERE status LIKE '%200%' "
    "GROUP BY day) ok "
    "JOIN "
    "(SELECT date_trunc('day', time)::date as day, count(status) as num "
    "FROM log "
    "WHERE status LIKE '%404%' "
    "GROUP BY day) nf "
    "ON ok.day = nf.day "
    "WHERE ((nf.num::float / (ok.num + nf.num)) * 100) > 1 "
    "ORDER BY errors desc;")
errors = c.fetchall()

print("\nDays with more than 1% request error rates:")
for day, error in errors:
    print(str(day) + " -- " + str("{0:.1f}".format(error)) + "% errors")

db.close()
