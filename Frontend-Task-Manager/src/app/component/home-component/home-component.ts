import { Component } from '@angular/core';

@Component({
  selector: 'app-home-component',
  imports: [],
  templateUrl: './home-component.html',
  styleUrl: './home-component.css',
})
export class HomeComponent {

  userName: string = 'Rockson'
  subtitle: string = 'Here\'s whats on your plate today'

}
