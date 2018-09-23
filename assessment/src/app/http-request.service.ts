import { Injectable } from '@angular/core';
import { Http } from '@angular/http';


@Injectable({
  providedIn: 'root'
})


export class HttpRequestService {

  constructor(private _http:Http) { }

  getConfig(page) {
 
  return this._http.get('http://api.github.com/search/users?q=repos%3A1+location%3ABangalore&type=Users&page='+page);
}
 getConfigUrl(url) {
  return this._http.get(url);
}

getData(){
	return this._http.get('http://localhost:3000/api/tenant/');
}
getDataId(id){
	return this._http.get('http://localhost:3000/api/tenant/'+id);
}




}
