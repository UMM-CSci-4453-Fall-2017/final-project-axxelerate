import { Injectable } from '@angular/core';
import { ResultPage } from './result-page'

@Injectable()
export class QueryService {

  results : ResultPage = {
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

  constructor() {
  }

  submitQuery(query : string, page : number) : ResultPage {
    return this.results;
  }

}
