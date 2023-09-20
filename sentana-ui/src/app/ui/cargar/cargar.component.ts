import { Component } from '@angular/core';
import { FileUploadEvent } from 'primeng/fileupload';
import { ItemProcesados } from 'src/app/domains/listado';
import { BertService } from 'src/app/services/bert.service';
import { Bty5Service } from 'src/app/services/byt5.service';
import { NLTKService } from 'src/app/services/nltk.service';
import { RobertaService } from 'src/app/services/roberta.service';

@Component({
  selector: 'app-cargar',
  templateUrl: './cargar.component.html',
  styleUrls: ['./cargar.component.scss'],
})
export class CargarComponent {
  detalleActivado: boolean = false;
  botonEvaluar: boolean = false;
  contenido?: any;
  itemsProcesados: ItemProcesados[] = [];

  constructor(
    private bertService: BertService,
    private bty5Service: Bty5Service,
    private nltkService: NLTKService,
    private robertaService: RobertaService
  ) {}

  evaluarModelo(): void {
    this.detalleActivado = true;
    let contenidoArray: [] = this.contenido.split('\n');
    this.itemsProcesados = [];

    for (let i = 0; i < contenidoArray.length; i++) {
      let messageAux = new String(contenidoArray[i]).split(',');
      let hate = messageAux[5];
      let message = messageAux[6];
      this.itemsProcesados.push({ index: i + 1, hate: hate, message: message });

      this.bertService.predict(message, i).subscribe((data) => {
        this.itemsProcesados[i].bert = data.value[0].label;
      });

      this.bty5Service.predict(message, i).subscribe((data) => {
        this.itemsProcesados[i].byt5 = data.value[0].label;
      });

      this.nltkService.predict(message, i).subscribe((data) => {
        this.itemsProcesados[data.value[0].index].nlkt = data.value[0].label;
      });

      this.robertaService.predict(message, i).subscribe((data) => {
        this.itemsProcesados[i].roberta = data.value[0].label;
      });
    }
  }

  limpiarModelo(): void {
    this.itemsProcesados = [];
    this.contenido = [];
    this.detalleActivado = false;
    this.botonEvaluar = false;
  }

  onUpload(event: FileUploadEvent): void {
    this.limpiarModelo();

    let fileReader = new FileReader();
    fileReader.onloadend = (e) => {
      this.contenido = fileReader.result;
      this.botonEvaluar = true;
    };
    fileReader.readAsText(event.files[0]);
  }
}
