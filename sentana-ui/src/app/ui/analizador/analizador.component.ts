import { Component } from '@angular/core';
import { Info } from 'src/app/domains/info';
import { BertService } from 'src/app/services/bert.service';
import { Bty5Service } from 'src/app/services/byt5.service';
import { NLTKService } from 'src/app/services/nltk.service';
import { RobertaService } from 'src/app/services/roberta.service';

@Component({
  selector: 'app-analizador',
  templateUrl: './analizador.component.html',
  styleUrls: ['./analizador.component.scss'],
})
export class AnalizadorComponent {
  modelosActivados: boolean = false;
  message: string = '';
  infos: Info[] = [];

  constructor(
    private bertService: BertService,
    private bty5Service: Bty5Service,
    private nltkService: NLTKService,
    private robertaService: RobertaService
  ) {}

  analizarModelo(): void {
    this.infos = [];
    this.modelosActivados = true;

    this.bertService.predict(this.message, 0).subscribe((data) => {
      this.infos.push(data.value[0]);
    });

    this.bty5Service.predict(this.message, 0).subscribe((data) => {
      this.infos.push(data.value[0]);
    });

    this.nltkService.predict(this.message, 1).subscribe((data) => {
      this.infos.push(data.value[0]);
    });

    this.robertaService.predict(this.message, 0).subscribe((data) => {
      this.infos.push(data.value[0]);
    });
  }

  limpiarModelo(): void {
    this.infos = [];
    this.message = '';
    this.modelosActivados = false;
  }
}
