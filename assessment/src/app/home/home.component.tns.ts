import { Component, OnInit } from '@angular/core';
import { HttpRequestTnsService } from '../http-request-tns.service.tns';
import { SearchBar } from "ui/search-bar";



@Component({
  selector: 'home',
  templateUrl: './home.component.tns.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponentTNS implements OnInit {
collection:any[];
collection1:any[];
myItems:any = [];
p:number;
total:number;
previousEnable:boolean;

  constructor(private data:HttpRequestTnsService) {
  this.total=0;
  this.p = 1;
  this.myItems = [];
  this.showData();
  this.previousEnable=false;
  this.searchEnable=false;
    
     
     
     this.collection1=[

];











this.xy();



   this.collection = []; 
   



    }

  ngOnInit() {

 
  }
  showData(page:number){
  this.data.getConfigTns(page)
  .subscribe(
  (response)=>{
  
console.log(response);
this.total=response.total_count;
this.collection=response['items'];
//alert(this.total);

  this.collection.forEach((item)=>{

   //alert(item['url']);
   this.data.getConfigUrlTns(item['url'])
  .subscribe(
  (response)=>{
 // alert(response['name']);
  
  
  
  this.collection1.push(response);
  this.myItem.push(response)
   
   //alert(this.collection1['name']);
   },
  (err)=>console.log(err)
 
  );
  });



  },
  (err)=>console.log(err)
 
  );



  }

  xy(){
  console.log(this.collection1[0]);
  }
 /* pageChanged(e){
  this.p=e;
  
  if(this.p%3===0){
  let page=(this.p/3)+1;
   this.showData(page);

  }
  }*/
  onTapNext(){
  this.p=this.p+1;
  let page=this.p;
  //alert(page);
  this.showData(page);
  }
   onTapPrevious(){
   let page;
   if(this.p===1){
   
   this.previousEnable=false;

  
  }else{
  this.previousEnable=true;
  this.p=this.p-1;
  page=this.p;
  this.showData(page);
  
  }
  
  //alert(this.previousEnable);
  }


   public onSubmit(args) {
         let searchBar = <SearchBar>args.object;
        let searchValue = searchBar.text.toLowerCase();

        this.myItems = [];
        if (searchValue !== "") {
            this.collection1.forEach((item)=>{
             if (item.name.toLowerCase().indexOf(searchValue) !== -1) {
                    this.myItems.push(item);
                    
                    }
                    }
                    });
               
                
            }
       
    

    public onTextChanged(args) {
      let searchBar = <SearchBar>args.object;
        let searchValue = searchBar.text.toLowerCase();

        this.myItems = [];
        if (searchValue !== "") {
            this.collection1.forEach((item)=>{
             if (item.name.toLowerCase().indexOf(searchValue) !== -1) {
                    this.myItems.push(item);
                    
                    }
                    }
                    });
               

    }
       public onClear(args) {
        let searchBar = <SearchBar>args.object;
        searchBar.text = "";
        searchBar.hint = "Search";

        this.myItems = [];
        this.collection1.forEach(item => {
            this.myItems.push(item);
        });
    }

    onSearchTap(){
    if(searchEnable===true){
    this.searchEnable=false;
    }else{
    this.searchEnable=true;
    }
    }



    showData(){
  this.data.getData()
  .subscribe(
  (response)=>{
  console.log(response);
  alert(response)
  const data = response.json();
  console.log(data);
  this.total=data.total_count;
  this.collection=data["items"];
  console.log(this.collection);
 
   },
  (err)=>console.log(err)
 
  );
  }
  


}



