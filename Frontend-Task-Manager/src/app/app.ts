import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {SidebarComponent} from './component/sidebar-component/sidebar-component';
import {HomeComponent} from './component/home-component/home-component';
import {TaskcardComponent} from './component/taskcard-component/taskcard-component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, SidebarComponent, HomeComponent, TaskcardComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('Frontend-Task-Manager');
}
