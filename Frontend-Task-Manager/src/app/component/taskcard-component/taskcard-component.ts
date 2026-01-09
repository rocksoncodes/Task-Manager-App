import { Component } from '@angular/core';

@Component({
  selector: 'app-taskcard-component',
  imports: [],
  templateUrl: './taskcard-component.html',
  styleUrl: './taskcard-component.css',
})
export class TaskcardComponent {
    taskTitle: string = "Task Title";
    taskDescription: string = "Your task for today is help John Doe with the development";
    taskStatus: string = "Pending";
    taskProgress: string = "Mark as Completed";
}
