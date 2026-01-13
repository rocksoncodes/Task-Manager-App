import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-sidebar-component',
  imports: [],
  templateUrl: './sidebar-component.html',
  styleUrl: './sidebar-component.css',
})
export class SidebarComponent {
  userName: string;
  email: string;
  tasks: any;
  private apiUrl: string;

  constructor(private http: HttpClient) {
    this.userName = 'Rockson Michael'
    this.email = 'michaelrockson@gmail.com'
    this.tasks = [];
    this.apiUrl = 'http://localhost:5000/api/tasks/';
  }

  getAllTasks():void {
    this.http.get(this.apiUrl + 'get/tasks/all').subscribe(data => {
      this.tasks = data;
      console.log(this.tasks);
    });
  }

  getTomorrowsTasks():void {
    this.http.get(this.apiUrl + "get/tasks/2").subscribe(data => {
      this.tasks = data;
      console.log(this.tasks);
    });
  }

  getCompletedTasks():void {
    this.http.get(this.apiUrl + 'get/completed/tasks/true').subscribe(data => {
      this.tasks = data;
      console.log(this.tasks);
    })
  }

}
