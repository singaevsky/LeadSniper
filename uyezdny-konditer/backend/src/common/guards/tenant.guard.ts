import { Injectable, CanActivate, ExecutionContext } from '@nestjs/common';
import { Observable } from 'rxjs';

@Injectable()
export class TenantGuard implements CanActivate {
  canActivate(
    context: ExecutionContext,
  ): boolean | Promise<boolean> | Observable<boolean> {
    const request = context.switchToHttp().getRequest();
    
    // Extract tenant information from subdomain or headers
    const host = request.headers.host;
    const subdomain = this.extractSubdomain(host);
    
    // Here we would normally validate the tenant against the database
    // For now, we'll just attach the subdomain to the request
    request.tenant = {
      id: null, // Would come from DB lookup
      subdomain,
      ownerId: null, // Would come from DB lookup
    };

    return true;
  }

  private extractSubdomain(host: string): string {
    const parts = host.split('.');
    if (parts.length >= 3) {
      return parts[0]; // subdomain.domain.com -> subdomain
    }
    return 'main'; // default tenant
  }
}