import {
  Component,
  Input,
  OnInit,
} from '@angular/core';

@Component({
  selector: 'app-taskcard-component',
  standalone: true,
  imports: [],
  templateUrl: './taskcard-component.html',
  styleUrl: './taskcard-component.css',
})
export class TaskcardComponent implements OnInit {
    @Input() task: any;
    taskTitle: string;
    taskDescription: string;
    taskStatus: string;
    taskProgress: string;

    constructor() {
      this.taskTitle = "";
      this.taskDescription = "";
      this.taskStatus = "";
      this.taskProgress = "";
    }

  ngOnInit() {
    this.setFallBackData()
    this.loadTasks()
  }

  setFallBackData(): void {
    if (!this.task) {
      this.taskTitle = "Task Title";
      this.taskDescription = "Your task description";
      this.taskStatus = "Pending";
      this.taskProgress = "Mark as Completed";
    }
  }

  loadTasks(): void {
    if (this.task) {
      this.taskTitle = this.task.title;
      this.taskDescription = this.task.task_descriptions;
      this.taskStatus = this.setTaskStatus(this.task.task_status);
      this.taskProgress = this.task.completed ? 'Completed' : 'Mark as Completed';
    }
  }

  setTaskStatus(status: any): any {
    if (status == 1) {
      this.taskStatus = "Due Today";
    } else if (status == 2) {
      this.taskStatus = "Due Tomorrow";
    } else if (status == 3) {
      this.taskStatus = "Overdue";
    }
    return this.taskStatus;
  }
}
