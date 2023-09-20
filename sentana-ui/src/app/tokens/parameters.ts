import { InjectionToken } from '@angular/core';

export const BACKEND_URL = new InjectionToken<string>('API_URL', {
  providedIn: 'root',
  factory() {
    return 'http://localhost:8000/api/v1';
  },
});
