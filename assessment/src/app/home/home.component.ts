import { Component, OnInit } from '@angular/core';
import { HttpRequestService } from '../http-request.service';
import { HttpPostService } from '../http-post.service';
import { HttpDeleteService } from '../http-delete.service';
import { HttpPutService } from '../http-put.service';
import { NgForm } from '@angular/forms';


@Component({
  selector: 'home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
collection:any[];
collection1:any[];
p:number;
total:number;
pop:Boolean;
popupdate:Boolean;
tempname:String;
tempaadhar:Number;
temppan:String;
tempbuilding:Number;
temproom:Number;
id:String;

  constructor(private data:HttpRequestService,private post:HttpPostService,private deleteD:HttpDeleteService,private put:HttpPutService) {
  this.total=0;
  this.p = 1;
  this.id="";
  this.pop=false;
  this.popupdate=false;
  this.showData();
    
     
     
     this.collection1=[
     





];











this.xy();



   this.collection = []; 
   



    }

  ngOnInit() {

 
  }
  /*
  showData(page:number){
  this.data.getConfig(page)
  .subscribe(
  (response)=>{
  const data = response.json();
  this.total=data.total_count;
  this.collection=data["items"];
  //console.log(this.collection);
  this.collection.forEach((item)=>{

   
   this.data.getConfigUrl(item['url'])
  .subscribe(
  (response)=>{
  const data = response.json();
  console.log(data);
  
  this.collection1.push(data);
   
   //console.log(this.collection1);
   },
  (err)=>console.log(err)
 
  );
  });
  


  },
  (err)=>console.log(err)
 
  );



  }*/

  xy(){
  console.log(this.collection1[0]);
  }
  pageChanged(e){
  this.p=e;
  
  if(this.p%3===0){
  let page=(this.p/3)+1;
   this.showData();

  }
  }





  showData(){
  this.data.getData()
  .subscribe(
  (response)=>{
  console.log(response);
  const data = response.json();
  console.log(data);
  this.total=data.total_count;
  this.collection=data.ten;
  console.log("collection",this.collection);
 
   },
  (err)=>console.log(err)
 
  );
  }


  registerUser(data) {

  this.post.postData(data).subscribe(data => {alert("Succesfully Added Tenant details")
  location.reload(true);
  this.pop=false},(err) => {alert(err._body)});
    console.log(data);
    }

popup(){
if(this.pop){
  this.pop=false;
  }else{
  this.pop=true;
  }
    this.tempname="";
  
this.tempaadhar=null;
this.temppan="";
this.tempbuilding=null;
this.temproom=null;

}


popupupdate(){
if(this.popupdate){
  this.popupdate=false;
  }else{
  this.popupdate=true;
  }
    this.tempname="";
  
this.tempaadhar=null;
this.temppan="";
this.tempbuilding=null;
this.temproom=null;

}



delete(index){
  console.log(index);
  var res=this.deleteD.removeData(index).subscribe(data => {alert("Succesfully Removed")
  location.reload(true);
  },(err) => {alert(err)});
  
    
  console.log(res);
}

updateDate(data){


  console.log(data)
  this.put.updateData(this.id,data).subscribe(data => {alert("Succesfully Updated details")
  location.reload(true);
  this.popupdate=false;
  },(err) => {alert(err._body)});
    console.log(data);
}
updateDate1(id){

console.log("update called",id);
this.popupdate=true;
this.data.getDataId(id).subscribe(
  (response)=>{
  console.log(response);

  const data1 = response.json();
  this.tempname=data1.Name;
  
this.tempaadhar=data1.Aadhar_no;
this.temppan=data1.Pan;
this.tempbuilding=data1.Building_no;
this.temproom=data1.Room_no;
  })
this.id=id;
console.log(id);


}

 








