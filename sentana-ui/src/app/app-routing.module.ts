import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './home/dashboard/dashboard.component';
import { AppLayoutComponent } from './layout/app.layout.component';
import { AnalizadorComponent } from './ui/analizador/analizador.component';
import { CargarComponent } from './ui/cargar/cargar.component';

const routes: Routes = [
  {
    path: '',
    component: AppLayoutComponent,
    children: [
      {
        path: '',
        component: DashboardComponent,
      },
      {
        path: 'ui/analizador',
        component: AnalizadorComponent,
      },
      {
        path: 'ui/cargar',
        component: CargarComponent,
      },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
