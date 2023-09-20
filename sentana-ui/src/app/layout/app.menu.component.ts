import { OnInit } from '@angular/core';
import { Component } from '@angular/core';
import { LayoutService } from './service/app.layout.service';

@Component({
  selector: 'app-menu',
  templateUrl: './app.menu.component.html',
})
export class AppMenuComponent implements OnInit {
  model: any[] = [];

  constructor(public layoutService: LayoutService) {}

  ngOnInit() {
    this.model = [
      {
        label: 'Home',
        items: [
          { label: 'Dashboard', icon: 'pi pi-fw pi-home', routerLink: ['/'] },
        ],
      },
      {
        label: 'Opciones',
        items: [
          {
            label: 'Analizador de Sentimiento',
            icon: 'pi pi-fw pi-id-card',
            routerLink: ['/ui/analizador'],
          },
          {
            label: 'Evaluar Modelos con DataSet',
            icon: 'pi pi-fw pi-chart-line',
            routerLink: ['/ui/cargar'],
          },
        ],
      },
    ];
  }
}
