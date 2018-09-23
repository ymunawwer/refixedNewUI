import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Ng2SearchPipeModule } from 'ng2-search-filter';
import {NgxPaginationModule} from 'ngx-pagination';
import { Routes,RouterModule } from '@angular/router';
import { HttpRequestService } from './http-request.service';
import { HttpModule } from '@angular/http';
import {MatButtonModule} from '@angular/material';
import {MatCardModule} from '@angular/material/card';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';

export const routes: Routes = [
  {
      path: '',
      redirectTo: '/home',
      pathMatch: 'full',
  },
  {
      path: 'home',
      component: HomeComponent,
  },
];

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent
  ],
  imports: [NgxPaginationModule,Ng2SearchPipeModule,FormsModule,MatButtonModule, MatCardModule,
  RouterModule.forRoot(routes),HttpModule,
    BrowserModule
  ],
  providers: [HttpRequestService],
  bootstrap: [AppComponent]
})
export class AppModule { }
