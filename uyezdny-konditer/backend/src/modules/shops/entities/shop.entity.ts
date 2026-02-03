import { Entity, Column, PrimaryGeneratedColumn, CreateDateColumn, UpdateDateColumn, ManyToOne, JoinColumn, OneToMany } from 'typeorm';
import { Tenant } from '../../tenants/entities/tenant.entity';
import { Product } from '../../products/entities/product.entity';

@Entity('shops')
export class Shop {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ type: 'uuid' }) // Foreign key to Tenant
  tenantId: string;

  @ManyToOne(() => Tenant, tenant => tenant.shops)
  @JoinColumn({ name: 'tenant_id' })
  tenant: Tenant;

  @Column({ type: 'varchar', length: 255 })
  name: string;

  @Column({ type: 'text', nullable: true })
  description?: string;

  @Column({ type: 'varchar', unique: true, length: 100 })
  subdomain: string;

  @Column({ type: 'varchar', length: 255, nullable: true })
  logoUrl?: string;

  @Column({ type: 'jsonb', nullable: true }) // Store contact info as JSON
  contactInfo?: {
    phone?: string;
    email?: string;
    address?: {
      street: string;
      building: string;
      city: string;
      region: string;
      postalCode: string;
    };
  };

  @Column({ type: 'decimal', precision: 10, scale: 2, default: 0.00 })
  rating: number;

  @Column({ type: 'int', default: 0 })
  reviewCount: number;

  @Column({ type: 'boolean', default: true })
  isActive: boolean;

  @CreateDateColumn({ type: 'timestamp' })
  createdAt: Date;

  @UpdateDateColumn({ type: 'timestamp' })
  updatedAt: Date;

  // Relations
  @OneToMany(() => Product, product => product.shop)
  products: Product[];
}