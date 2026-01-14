import { Component, signal, OnInit } from '@angular/core';
import {SidebarComponent} from './component/sidebar-component/sidebar-component';
import {HomeComponent} from './component/home-component/home-component';
import {TaskcardComponent} from './component/taskcard-component/taskcard-component';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    SidebarComponent,
    HomeComponent,
    TaskcardComponent
  ],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit {
  protected readonly title = signal('Frontend-Task-Manager');
  tasks: any[];
  private apiUrl: string;

  constructor(private http: HttpClient) {
    this.tasks = [];
    this.apiUrl = 'http://localhost:5000/api/tasks/';
  }

  ngOnInit() {
    this.getAllTasks();
  }

  getAllTasks():void {
    this.http.get<any[]>(this.apiUrl + 'get/tasks/all').subscribe(data => {
      this.tasks = data;
      console.log('Tasks loaded:', this.tasks)
    });
  }


}
