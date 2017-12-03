import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { QueryService } from '../query.service';
import { ResultPage } from '../result-page';
import { Result } from '../result';

@Component({
  selector: 'app-result-page',
  templateUrl: './result-page.component.html',
  styleUrls: ['./result-page.component.css']
})
export class ResultPageComponent implements OnInit {

  private data : ResultPage;
  private results : [Result];

  constructor(
    private route: ActivatedRoute,
    private queryService : QueryService
  ) { }

  ngOnInit() {
  }


  log() {
    this.route.queryParams.subscribe(
      value => {
        var query = value["q"];
        var page = value["p"];
        if ( query === undefined || page === undefined ) {
          console.log("a bad request");
        } else {
          this.data = this.queryService.submitQuery(query,page);
          this.results = this.data.results;
        }
      },
      error => console.log("error:" + error),
      () => console.log("finished")
    );
    console.log("A function was called");
  }


}
