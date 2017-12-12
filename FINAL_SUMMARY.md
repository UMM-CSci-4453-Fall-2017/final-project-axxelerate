# Final Summary

## Project description and goals

The goal of this project was to create a simple search engine for pages on the
web. 

The project was to consist of 3 components:

1. A crawler written in python. This is program which downloads a webpage, selects some information
   from that page to store in the database, and then downloads more webpages based
   on the links found in the current webpage.
2. A web client written in Angular 4 which would allow a human to type in queries
   and view a list of relevant pages.
3. A web server written in python to accept queries from the web client and
   generate results based on the content in the DB.


## Database contents

## State of project

In this section, we describe what were and weren't able to accomplish.

It took us a while to decide what page our crawler should start on. We
eventually settled on restricting the crawler to collecting information from the
English Wikipedia site and pointed the crawler at that site's home page to get
it going. 

We were able to populate the database at a pretty good clip and would have been
able to build a really big database, but we had trouble with our connection to the
MariaDB database dying and never properly handled that scenario and only
collected data for a little over 5000 pages, which severely limits the relevancy
of our results. 

Adding indexes to the database after we filled it with data only took a short
while and increased the speed of our queries tremendously (e.g. going from 7
seconds to 0.01, and going from over 30 seconds to 0.01).

After populating the DB, we implented PageRank and computed a PageRank for each
page. This is the single mechanism we use for ranking results, but it isn't
particularly good for our scenario, since PageRank is better for establishing
the credibility/importance of pages, but all the content pages on Wikipedia are
equally important. It is just a question of which page is _relevant_ to the
given keyword and PageRank doesn't help with that.

The giving each URL a rank does allow us to sort the results and thus implement
semi-decent pagination. The pagination allows the client to avoid downloading
the results it doesn't care about, but if the client ends up paging through the
whol result list anyway, this will incure 2x the read cost on the DB that simply
dumping all the results would have incured.

Our server can currently only search for a single keyword at a time. We believe
that adding support for multiple keywords would not be tremendously complex, nor
should slow the query down too much.



## Potential for future work

## Overall reaction
