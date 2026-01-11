import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  standalone: true,
  selector: 'app-input-card-component',
  imports: [CommonModule, MatDialogModule, MatButtonModule],
  templateUrl: './input-card-component.html',
  styleUrl: './input-card-component.css',
})
export class InputCardComponent {
  constructor(private dialog: MatDialogRef<InputCardComponent>) {}

  close() {
    this.dialog.close();
  }
}
