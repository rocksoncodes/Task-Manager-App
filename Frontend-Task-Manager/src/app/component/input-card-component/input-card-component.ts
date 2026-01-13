import { Component } from '@angular/core';
import { Output } from '@angular/core';
import { EventEmitter } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  standalone: true,
  selector: 'app-input-card-component',
  imports: [
    FormsModule
  ],
  templateUrl: './input-card-component.html',
  styleUrl: './input-card-component.css',
})
export class InputCardComponent {
  taskTitle: string;
  taskDescription: string;
  taskStatus: string;
  isCompleted: boolean;

  constructor( private http: HttpClient ) {
    this.taskTitle = '';
    this.taskDescription = '';
    this.taskStatus = '';
    this.isCompleted = false;
  }

  @Output() closeModal = new EventEmitter<boolean>();

  closeModalButton(): void {
    this.closeModal.emit(false);
  }

  saveTask(): void {
    const payload = {
      title: this.taskTitle,
      task_descriptions: this.taskDescription,
      task_status: this.taskStatus,
      completed: this.isCompleted
    };

    this.http.post('http://localhost:5000/api/tasks/create/task', payload).subscribe(response => {
      console.log("Success", response);
    });

    alert("Task saved:" + " " + this.taskTitle);
    this.closeModal.emit(false);
  }

}
