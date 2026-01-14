import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-taskcard-component',
  standalone: true,
  imports: [],
  templateUrl: './taskcard-component.html',
  styleUrl: './taskcard-component.css',
})
export class TaskcardComponent implements OnInit {
    @Input() task: any;

    taskTitle: string = "Task Title";
    taskDescription: string = "Your task for today is help John Doe with the development";
    taskStatus: string = "Pending";
    taskProgress: string = "Mark as Completed";

  ngOnInit() {
    if (this.task) {
      this.taskTitle = this.task.title;
      this.taskDescription = this.task.task_descriptions;
      this.taskStatus = `Status: ${this.task.task_status}`;
      this.taskProgress = this.task.completed ? 'Completed' : 'Mark as Completed';
    }
  }
}
