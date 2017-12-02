import { Injectable } from '@angular/core';

@Injectable()
export class QueryService {

  results : ResultPage;

  constructor() {
    results = {
      nextPage: "nxt",
      prevPage: "prev",
      results: [
        {
          title: "a title",
          link: " a link",
          snippet: "This is demo data"
        }
      ]
    };
  }

  submitQuery(query : string, page : int) : ResultPage {
    return results;
  }

}
