import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
@Injectable({
  providedIn: 'root'
})
export class HttpDeleteService {

  constructor(private _http:Http) { }
  
  removeData(id){
	return this._http.delete('http://localhost:3000/api/tenant/'+id);
}
}
