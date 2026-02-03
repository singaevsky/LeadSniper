import { Entity, Column, PrimaryGeneratedColumn, CreateDateColumn, UpdateDateColumn, OneToMany, Unique } from 'typeorm';
import { Shop } from '../../shops/entities/shop.entity';

@Entity('tenants')
@Unique(['subdomain'])
export class Tenant {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ type: 'varchar', length: 255 })
  name: string;

  @Column({ type: 'varchar', unique: true, length: 100 })
  subdomain: string;

  @Column({ type: 'text', nullable: true })
  description?: string;

  @Column({ type: 'uuid' }) // Foreign key to User who owns this tenant
  ownerId: string;

  @Column({ 
    type: 'enum', 
    enum: ['active', 'pending', 'suspended'], 
    default: 'pending' 
  })
  status: 'active' | 'pending' | 'suspended';

  @Column({ 
    type: 'enum', 
    enum: ['basic', 'premium', 'enterprise'], 
    default: 'basic' 
  })
  subscriptionPlan: 'basic' | 'premium' | 'enterprise';

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

  @Column({ type: 'jsonb', nullable: true }) // Store theme settings as JSON
  themeSettings?: {
    primaryColor?: string;
    secondaryColor?: string;
    logoUrl?: string;
    faviconUrl?: string;
  };

  @CreateDateColumn({ type: 'timestamp' })
  createdAt: Date;

  @UpdateDateColumn({ type: 'timestamp' })
  updatedAt: Date;

  // Relations
  @OneToMany(() => Shop, shop => shop.tenant)
  shops: Shop[];
}