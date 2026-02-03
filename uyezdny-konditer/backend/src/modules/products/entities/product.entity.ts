import { Entity, Column, PrimaryGeneratedColumn, CreateDateColumn, UpdateDateColumn, ManyToOne, JoinColumn } from 'typeorm';
import { Shop } from '../../shops/entities/shop.entity';

@Entity('products')
export class Product {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ type: 'uuid' }) // Foreign key to Shop
  shopId: string;

  @ManyToOne(() => Shop, shop => shop.products)
  @JoinColumn({ name: 'shop_id' })
  shop: Shop;

  @Column({ type: 'varchar', length: 255 })
  name: string;

  @Column({ type: 'text', nullable: true })
  description?: string;

  @Column({ 
    type: 'enum', 
    enum: ['cakes', 'pastries', 'cookies', 'other'], 
    default: 'other' 
  })
  category: 'cakes' | 'pastries' | 'cookies' | 'other';

  @Column({ type: 'decimal', precision: 10, scale: 2 })
  price: number;

  @Column({ type: 'decimal', precision: 10, scale: 2, nullable: true })
  discountPrice?: number;

  @Column({ type: 'text', array: true, nullable: true })
  images?: string[];

  @Column({ type: 'jsonb', nullable: true }) // Store nutritional info as JSON
  nutritionalInfo?: {
    calories: number;
    proteins: number; // in grams
    fats: number; // in grams
    carbohydrates: number; // in grams
    weight: number; // in grams
  };

  @Column({ type: 'varchar', array: true, nullable: true })
  ingredients?: string[];

  @Column({ type: 'jsonb', nullable: true }) // Store customizable options as JSON
  customizableOptions?: Array<{
    type: 'size' | 'flavor' | 'decoration';
    options: Array<{
      name: string;
      multiplier?: number; // for size adjustments
      additionalCost?: number; // extra cost for this option
    }>;
  }>;

  @Column({ type: 'boolean', default: true })
  available: boolean;

  @Column({ type: 'decimal', precision: 3, scale: 2, default: 0.00 })
  rating: number;

  @Column({ type: 'int', default: 0 })
  reviewCount: number;

  @CreateDateColumn({ type: 'timestamp' })
  createdAt: Date;

  @UpdateDateColumn({ type: 'timestamp' })
  updatedAt: Date;
}