import { Component } from '@angular/core';
import {InputCardComponent} from '../input-card-component/input-card-component';

@Component({
  selector: 'app-home-component',
  imports: [
    InputCardComponent
  ],
  templateUrl: './home-component.html',
  styleUrl: './home-component.css',
})

export class HomeComponent {
  showForm:boolean;
  currentDate: Date;
  currentHour: number;
  userName: string;
  greeting: string;
  subtitle: string;

  constructor() {
    this.currentDate = new Date();
    this.currentHour = this.currentDate.getHours();
    this.userName = "Rockson"
    this.greeting = '';
    this.subtitle = ''
    this.showForm = false;
    this.setGreeting()
  }

  setGreeting() {
    if (this.currentHour >= 0 && this.currentHour <= 11) {
      this.greeting = "Good Morning";
      this.subtitle = "Here's whats on your plate this morning";

    } else if (this.currentHour >= 12 && this.currentHour <= 16) {
      this.greeting = "Good Afternoon";
      this.subtitle = "Here's whats on your plate this afternoon";

    } else {
      this.greeting = "Good Evening";
      this.subtitle = "Here's whats on your plate this evening";
    }
  }

  showModal() {
    this.showForm = true;
    console.log("showModal activated");
  }

  hideModal() {
    this.showForm = false;
  }
}
