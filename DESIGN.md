## What

For this project we will be implementing a search engine. We'll figure out how 
to best store the neccessary information in MariaDB, collect data from a 
limited number of pages, and create a simple web server and web interface for quering our database.  
One of the things that makes or breaks a search engine is the quality of its ranking. We'll 
likely start with a really simple ranking system and see how much time we have left after that.

Technologies we expect to use:
- [Scrapy](https://scrapy.org/) to collect data and insert
it in the DB
- [MariaDB](https://mariadb.com) for our database
- [Flask](http://flask.pocoo.org/) to implement our webserver 
- [Angular](https://angular.io/) and 
[Material Design](https://material.io/) for our web interface.

## Who 
Developer |Points | Task
--|---|---
Vipul Sharma | 5 | Implement indexing keywords using: Stemming via Edge N gram method , Inverted Indexing and Segmenting
Laverne Schrock | 20 | Implement frontend to query database
Vipul Sharma | 20 | Implement crawler and querying from keywords, scoring using Google's PageRank algorithm
Both | 10 | Design REST interface to be provided by our webserver
Laverne Schrock | 5 | Design and Document database tables. What indexing? How many tables? What columns? _What are the **sematics** of what we store?_
Both | 15 | Implement the SQL queries in our webserver
