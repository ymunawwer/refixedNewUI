import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
@Injectable({
  providedIn: 'root'
})
export class HttpPutService {

  constructor(private _http:Http) { }

updateData(id,data){
 
	return this._http.put('http://localhost:3000/api/tenant/'+id,data        

            );
}

}
