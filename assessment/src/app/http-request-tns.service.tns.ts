import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
@Injectable({
  providedIn: 'root'
})
export class HttpRequestTnsService {

  constructor(private httpclient:HttpClient) { }

   getConfigTns(page) {
 
  return this.httpclient.get('https://api.github.com/search/users?q=repos%3A1+location%3ABangalore&type=Users&page='+page);
}
 getConfigUrlTns(url) {
  return this.httpclient.get(url);
}

getData(){
	return this.httpclient.get('http://localhost:3000/api/tenant/');
}


}




