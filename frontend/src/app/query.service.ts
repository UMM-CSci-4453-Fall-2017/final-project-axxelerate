import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import { ResultPage } from './result-page'

@Injectable()
export class QueryService {

  private resultsUrl = "http://localhost:5000/results";

  constructor(
    private http: HttpClient
  ) { }

  submitQuery(query : string, f : number) : Observable<ResultPage> {
    return this.http.get<ResultPage>(this.resultsUrl + "?query=" + query + "&from=" + f);
  }

}
