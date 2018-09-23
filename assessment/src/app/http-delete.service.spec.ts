import { TestBed, inject } from '@angular/core/testing';

import { HttpDeleteService } from './http-delete.service';

describe('HttpDeleteService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [HttpDeleteService]
    });
  });

  it('should be created', inject([HttpDeleteService], (service: HttpDeleteService) => {
    expect(service).toBeTruthy();
  }));
});
