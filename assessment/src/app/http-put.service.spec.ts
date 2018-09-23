import { TestBed, inject } from '@angular/core/testing';

import { HttpPutService } from './http-put.service';

describe('HttpPutService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [HttpPutService]
    });
  });

  it('should be created', inject([HttpPutService], (service: HttpPutService) => {
    expect(service).toBeTruthy();
  }));
});
