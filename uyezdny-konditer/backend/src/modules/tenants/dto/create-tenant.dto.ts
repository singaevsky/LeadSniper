import { IsString, IsNotEmpty, IsEmail, IsOptional, IsEnum, IsUUID, ValidateNested, IsUrl } from 'class-validator';
import { ApiProperty } from '@nestjs/swagger';
import { Type } from 'class-transformer';

enum SubscriptionPlan {
  BASIC = 'basic',
  PREMIUM = 'premium',
  ENTERPRISE = 'enterprise',
}

enum TenantStatus {
  ACTIVE = 'active',
  PENDING = 'pending',
  SUSPENDED = 'suspended',
}

class ContactInfoDto {
  @ApiProperty({ example: '+71234567890', required: false })
  @IsOptional()
  @IsString()
  phone?: string;

  @ApiProperty({ example: 'contact@shop.com', required: false })
  @IsOptional()
  @IsEmail()
  email?: string;

  @ApiProperty({ required: false })
  @IsOptional()
  @ValidateNested()
  @Type(() => AddressDto)
  address?: AddressDto;
}

class AddressDto {
  @ApiProperty({ example: 'ул. Пушкина' })
  @IsString()
  @IsNotEmpty()
  street: string;

  @ApiProperty({ example: 'д. 10' })
  @IsString()
  @IsNotEmpty()
  building: string;

  @ApiProperty({ example: 'Город' })
  @IsString()
  @IsNotEmpty()
  city: string;

  @ApiProperty({ example: 'Регион' })
  @IsString()
  @IsNotEmpty()
  region: string;

  @ApiProperty({ example: '123456' })
  @IsString()
  @IsNotEmpty()
  postalCode: string;
}

class ThemeSettingsDto {
  @ApiProperty({ example: '#E63946', required: false })
  @IsOptional()
  @IsString()
  primaryColor?: string;

  @ApiProperty({ example: '#F1FAEE', required: false })
  @IsOptional()
  @IsString()
  secondaryColor?: string;

  @ApiProperty({ example: 'https://cdn.example.com/logo.png', required: false })
  @IsOptional()
  @IsUrl()
  logoUrl?: string;

  @ApiProperty({ example: 'https://cdn.example.com/favicon.ico', required: false })
  @IsOptional()
  @IsUrl()
  faviconUrl?: string;
}

export class CreateTenantDto {
  @ApiProperty({ example: 'Мой кондитерский магазин' })
  @IsString()
  @IsNotEmpty()
  name: string;

  @ApiProperty({ example: 'my-bakery' })
  @IsString()
  @IsNotEmpty()
  subdomain: string;

  @ApiProperty({ example: 'Лучшие торты в городе!', required: false })
  @IsOptional()
  @IsString()
  description?: string;

  @ApiProperty({ example: 'basic', enum: SubscriptionPlan, required: false })
  @IsOptional()
  @IsEnum(SubscriptionPlan)
  subscriptionPlan?: SubscriptionPlan = SubscriptionPlan.BASIC;

  @ApiProperty({ required: false })
  @IsOptional()
  @ValidateNested()
  @Type(() => ContactInfoDto)
  contactInfo?: ContactInfoDto;

  @ApiProperty({ required: false })
  @IsOptional()
  @ValidateNested()
  @Type(() => ThemeSettingsDto)
  themeSettings?: ThemeSettingsDto;
}