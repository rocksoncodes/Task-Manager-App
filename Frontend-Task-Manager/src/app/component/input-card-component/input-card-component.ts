import { Component } from '@angular/core';
import { Output } from '@angular/core';
import { EventEmitter } from '@angular/core';

@Component({
  standalone: true,
  selector: 'app-input-card-component',
  imports: [],
  templateUrl: './input-card-component.html',
  styleUrl: './input-card-component.css',
})
export class InputCardComponent {

  @Output() closeModal = new EventEmitter<boolean>();

  closeModalButton():void {
    this.closeModal.emit(false);
  }

  showNotification():void {
    alert("Task Saved")
    this.closeModal.emit(false);
  }

}
