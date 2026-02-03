import { createParamDecorator, ExecutionContext } from '@nestjs/common';

export interface TenantInfo {
  id: string;
  subdomain: string;
  ownerId: string;
}

export const Tenant = createParamDecorator<TenantInfo>(
  (data: unknown, ctx: ExecutionContext): TenantInfo => {
    const request = ctx.switchToHttp().getRequest();
    return request.tenant;
  },
);

export const GetTenant = (): ParameterDecorator => Tenant();