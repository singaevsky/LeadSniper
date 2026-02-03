import { Controller, Get, Post, Body, Patch, Param, Delete, Query, UseGuards } from '@nestjs/common';
import { TenantsService } from './tenants.service';
import { CreateTenantDto } from './dto/create-tenant.dto';
import { UpdateTenantDto } from './dto/update-tenant.dto';
import { ApiTags, ApiOperation, ApiResponse, ApiParam, ApiQuery } from '@nestjs/swagger';
import { TenantGuard } from '../../common/guards/tenant.guard';

@ApiTags('tenants')
@Controller('tenants')
export class TenantsController {
  constructor(private readonly tenantsService: TenantsService) {}

  @ApiOperation({ summary: 'Create a new tenant' })
  @ApiResponse({ status: 201, description: 'Tenant created successfully.' })
  @ApiResponse({ status: 400, description: 'Bad request.' })
  @Post()
  async create(@Body() createTenantDto: CreateTenantDto) {
    // In a real application, ownerId would come from authenticated user
    const ownerId = 'mock-owner-id';
    return await this.tenantsService.create(createTenantDto, ownerId);
  }

  @ApiOperation({ summary: 'Get all tenants' })
  @ApiResponse({ status: 200, description: 'List of tenants.' })
  @ApiQuery({ name: 'limit', required: false, type: Number, description: 'Number of items to return' })
  @ApiQuery({ name: 'offset', required: false, type: Number, description: 'Offset for pagination' })
  @Get()
  async findAll(
    @Query('limit') limit?: string,
    @Query('offset') offset?: string,
  ) {
    const limitNum = limit ? parseInt(limit, 10) : 20;
    const offsetNum = offset ? parseInt(offset, 10) : 0;
    
    return await this.tenantsService.findAll(limitNum, offsetNum);
  }

  @ApiOperation({ summary: 'Get tenant by ID' })
  @ApiResponse({ status: 200, description: 'Tenant found.' })
  @ApiResponse({ status: 404, description: 'Tenant not found.' })
  @ApiParam({ name: 'id', description: 'Tenant ID' })
  @Get(':id')
  async findOne(@Param('id') id: string) {
    return await this.tenantsService.findOne(id);
  }

  @ApiOperation({ summary: 'Update tenant by ID' })
  @ApiResponse({ status: 200, description: 'Tenant updated.' })
  @ApiResponse({ status: 404, description: 'Tenant not found.' })
  @ApiParam({ name: 'id', description: 'Tenant ID' })
  @Patch(':id')
  async update(@Param('id') id: string, @Body() updateTenantDto: UpdateTenantDto) {
    return await this.tenantsService.update(id, updateTenantDto);
  }

  @ApiOperation({ summary: 'Delete tenant by ID' })
  @ApiResponse({ status: 200, description: 'Tenant deleted.' })
  @ApiResponse({ status: 404, description: 'Tenant not found.' })
  @ApiParam({ name: 'id', description: 'Tenant ID' })
  @Delete(':id')
  async remove(@Param('id') id: string) {
    return await this.tenantsService.remove(id);
  }
}