import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { FormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { CardModule } from 'primeng/card';
import { DropdownModule } from 'primeng/dropdown';
import { FileUploadModule } from 'primeng/fileupload';
import { InputTextModule } from 'primeng/inputtext';
import { PanelModule } from 'primeng/panel';
import { RadioButtonModule } from 'primeng/radiobutton';
import { SelectButtonModule } from 'primeng/selectbutton';
import { TableModule } from 'primeng/table';
import { TabViewModule } from 'primeng/tabview';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DashboardComponent } from './home/dashboard/dashboard.component';
import { AppLayoutModule } from './layout/app.layout.module';
import { AnalizadorComponent } from './ui/analizador/analizador.component';
import { CargarComponent } from './ui/cargar/cargar.component';

@NgModule({
  declarations: [
    AppComponent,
    AnalizadorComponent,
    DashboardComponent,
    CargarComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    AppLayoutModule,
    CardModule,
    InputTextModule,
    ButtonModule,
    RadioButtonModule,
    FormsModule,
    SelectButtonModule,
    TableModule,
    PanelModule,
    TabViewModule,
    DropdownModule,
    FileUploadModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
