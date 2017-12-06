import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.css']
})
export class LandingPageComponent implements OnInit {

  query : string = "";

  constructor(
    private router: Router
  ) { }

  ngOnInit() {
  }

  submitQuery(query : string) {
    this.router.navigate(["search"], {queryParams: {q: query, p: 1}});
  }

}
