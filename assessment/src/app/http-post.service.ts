import { Injectable } from '@angular/core';
import { Http } from '@angular/http';



@Injectable({
  providedIn: 'root'
})
export class HttpPostService {

  constructor(private _http:Http) { }
  
  postData(data){
 
	return this._http.post('http://localhost:3000/api/tenant/',data,
             

            );
}

}
