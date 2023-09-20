import { HttpClient } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';
import { BACKEND_URL } from '../tokens/parameters';
import { BaseService } from './base.service';
import { ResponseTo } from '../domains/response';
import { Observable, catchError, retry } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class RobertaService extends BaseService {
  constructor(
    @Inject(BACKEND_URL) private url: string,
    private http: HttpClient
  ) {
    super();
  }

  predict(message: string, index: number): Observable<ResponseTo> {
    return this.http
      .post<ResponseTo>(`${this.url}/roberta/predict/`, {
        data: [message, index],
      })
      .pipe(retry(1), catchError(this.handleError));
  }
}
