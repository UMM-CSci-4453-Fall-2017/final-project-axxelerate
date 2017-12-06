import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, Params } from '@angular/router';
import { NotFoundComponent } from '../not-found/not-found.component';
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
  private badQuery: boolean = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private queryService : QueryService
  ) { }

  ngOnInit() {
    this.route.queryParams.subscribe(
      value => {
        var query = value["q"];
        var page = value["p"];
        if ( query === undefined ) {
          this.badQuery = true;
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
