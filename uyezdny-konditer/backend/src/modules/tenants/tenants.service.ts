import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Tenant } from './entities/tenant.entity';
import { CreateTenantDto } from './dto/create-tenant.dto';
import { UpdateTenantDto } from './dto/update-tenant.dto';

@Injectable()
export class TenantsService {
  constructor(
    @InjectRepository(Tenant)
    private tenantsRepository: Repository<Tenant>,
  ) {}

  async create(createTenantDto: CreateTenantDto, ownerId: string): Promise<Tenant> {
    const tenant = new Tenant();
    tenant.name = createTenantDto.name;
    tenant.subdomain = createTenantDto.subdomain;
    tenant.description = createTenantDto.description;
    tenant.ownerId = ownerId;
    tenant.contactInfo = createTenantDto.contactInfo;
    tenant.themeSettings = createTenantDto.themeSettings;
    
    return await this.tenantsRepository.save(tenant);
  }

  async findAll(limit: number = 20, offset: number = 0): Promise<{ data: Tenant[]; total: number }> {
    const [data, total] = await this.tenantsRepository.findAndCount({
      skip: offset,
      take: limit,
      order: { createdAt: 'DESC' },
    });

    return { data, total };
  }

  async findOne(id: string): Promise<Tenant> {
    const tenant = await this.tenantsRepository.findOneBy({ id });
    if (!tenant) {
      throw new NotFoundException(`Tenant with ID ${id} not found`);
    }
    return tenant;
  }

  async findBySubdomain(subdomain: string): Promise<Tenant> {
    const tenant = await this.tenantsRepository.findOneBy({ subdomain });
    if (!tenant) {
      throw new NotFoundException(`Tenant with subdomain ${subdomain} not found`);
    }
    return tenant;
  }

  async update(id: string, updateTenantDto: UpdateTenantDto): Promise<Tenant> {
    const tenant = await this.findOne(id);
    
    Object.assign(tenant, updateTenantDto);
    
    return await this.tenantsRepository.save(tenant);
  }

  async remove(id: string): Promise<void> {
    const result = await this.tenantsRepository.delete(id);
    if (result.affected === 0) {
      throw new NotFoundException(`Tenant with ID ${id} not found`);
    }
  }
}