import { Component } from '@angular/core';
import { Output } from '@angular/core';
import { EventEmitter } from '@angular/core';
import { FormsModule } from '@angular/forms';

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

  constructor() {
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
    alert("Task saved:" + " " + this.taskTitle);
    this.closeModal.emit(false);
  }

}
