import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.css']
})
export class LandingPageComponent implements OnInit {

  query : string = "";

  constructor() { }

  ngOnInit() {
  }

  submitQuery(query : string) {
    console.log("search is not yet implemented: '" + query + "'");
  }

}
