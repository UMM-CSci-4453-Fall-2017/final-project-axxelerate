## What

For this project we will be implementing a search engine. We'll figure out how 
to best store the neccessary information in MariaDB, collect data from a 
limited number of pages, and create a simple web server and web interface for quering our database.  

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
Vipul Sharma | 20 | Implement scraper to populate database
Laverne Schrock | 20 | Implement frontend to query database
Both | 5 | Design REST interface to be provided by our webserver
Both | 15 | Design and Document database tables. What indexing? How many tables? What columns? _What are the **sematics** of what we store?_
Both | 10 | Implement the SQL queries in our webserver
