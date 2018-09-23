import { NgModule, NO_ERRORS_SCHEMA } from '@angular/core';
import { NativeScriptModule } from 'nativescript-angular/nativescript.module';
import { NativeScriptHttpClientModule } from "nativescript-angular/http-client";
import { NativeScriptHttpModule } from 'nativescript-angular/http';
import { PagerModule } from "nativescript-pager/angular";

import { AppRoutingModule } from './app-routing.module.tns';
import { AppComponent } from './app.component.tns';
import { HomeComponentTNS } from './home/home.component.tns';
import { HttpModule } from '@angular/http';

// Uncomment and add to NgModule imports if you need to use two-way binding
// import { NativeScriptFormsModule } from "nativescript-angular/forms";

// Uncomment and add to NgModule imports  if you need to use the HTTP wrapper
// import { NativeScriptHttpClientModule } from 'nativescript-angular/http-client';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponentTNS,
  ],
  imports: [
    NativeScriptModule,
    AppRoutingModule,
    HttpModule,PagerModule,
    NativeScriptHttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent],
  schemas: [NO_ERRORS_SCHEMA]
})
/*
Pass your application module to the bootstrapModule function located in main.ts to start your app
*/
export class AppModule { }
