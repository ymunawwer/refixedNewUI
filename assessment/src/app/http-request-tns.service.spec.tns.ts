import { TestBed, inject } from '@angular/core/testing';

import { HttpRequestTnsService } from './http-request-tns.service';

describe('HttpRequestTnsService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [HttpRequestTnsService]
    });
  });

  it('should be created', inject([HttpRequestTnsService], (service: HttpRequestTnsService) => {
    expect(service).toBeTruthy();
  }));
});
