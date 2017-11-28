# Search API

This page documents the REST API that we will provide to allow apps to use our
search engine. 

Our REST API will have a single endpoint.

## `GET /results`

This endpoint requires the following query paramenters

- `?query=` : A string specifying the query for the database
- `?page=` : Which page of the results to view (see below). If not included,
  behaves as if `?page=1`. In general, you should leave this off and then read
  the `nextPage` key from the result.

Queries can return massive amounts of results and returning them all in a single
query may be problematic. In addition, an interface for this would probably only
want to display the first few results so downloading all of them would be a
waste of bandwidth. Our endpoint therfore only returns 10 results at a time. To
fetch the first page of results use `?page=1`, to fetch the second use `?page=2`,
etc.

The response will be JSON containing the following keys:

- `nextPage`: If there are additional pages, this is a full URL to fetch the
  next page of results. Otherwise will be absent or `null`.
- `prevPage`: If the request was not for the first page, this will refer to the 
  previous page.
- `results`: An array of objects describing one search result. There will be at
  most 10 elements in this list. Each of these objects has the following keys
  - `title`: The title of the page being linked to
  - `link`: The full URL to the page
  - `snippet`: A string pulled from the contents of the page
  
Example response:

```json
{
 "prevPage": "http://localhost:80/results?query=example?page=2",
 "nextPage": "http://localhost:80/results?query=example?page=3",
 "results":
 [
   {
     "title": "This is a page",
     "link": "http://example.com/index.html",
     "snippet": "This domain is established to be used for illustrative examples"
   },
   { ... },
   { ... },
   { ... },
   { ... },
   { ... },
   { ... },
   { ... },
   { ... },
   { ... }
 ]
}
```

This pagination scheme is not really following standards, but it will do.
