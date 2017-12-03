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
    this.route.queryParams.subscribe(
      value => {
        var query = value["q"];
        var page = value["p"];
        if ( query === undefined ) {
          console.log("a bad request");
        } else {
          if ( page === undefined ) {
            page = 0;
          }
          this.queryService.submitQuery(query,page).subscribe(
            value => {
              this.results = value.results;
            },
            error => {
              console.log("Failure in fetching data:");
            });
        }
      },
      error => console.log("error:" + error),
      () => console.log("finished")
    );
  }

}
