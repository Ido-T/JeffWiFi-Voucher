# CHANGELOG

All notable changes to the JeffWiFi Voucher System.


# Version 2.5.3 - WISP Foundation Release

Date:
2026-08-01


## Added

### Secure Voucher Generation

- Replaced random generation with Python secrets module
- Added ambiguous character protection
- Added database uniqueness verification


### Database Improvements

- Completed database integrity repair
- Repaired historical voucher batch relationships
- Added database constraints
- Added foreign key protection
- Added transaction handling
- Added database indexes
- Added database audit tools


### MikroTik Integration

- Improved RouterOS export system
- Added export validation
- Added configurable hotspot server settings
- Added export history tracking
- Verified real MikroTik RouterOS import


### Testing

Completed validation:

- Database connection test
- Database integrity audit
- Voucher generation pipeline test
- Export validation test
- Export history test
- Transaction test
- Voucher lifecycle test


## Status

Stable foundation release.

The system is ready for the next phase:

- User management
- Roles and permissions
- Operator accountability
- Payment architecture
- MonCash/NatCash preparation
- WISP management features



# Version 2.5.2 - Database Hardening

Date:
2026-07-31


## Added

- Database connection hardening
- SQLite foreign key enforcement
- WAL mode
- Database indexes
- Schema migration with constraints
- Voucher status validation
- Financial validation rules
- Batch and sales relationship protection


## Status

Production-ready database foundation.



# Version 2.5.1 - Database Integrity Repair

## Added

- Repaired historical voucher batch relationships
- Added migration batch for legacy records
- Removed orphan batch records
- Verified sales and voucher lifecycle integrity


## Status

Database consistency restored.



# Version 2.5.0 - Clean Architecture Stabilization

Date:
2026-07-31


## Added

- Reorganized project structure
- Separated application files from tests
- Archived CSV migration files
- Archived old voucher generator
- Removed Python cache files
- Added root .gitignore
- Verified SQLite migration stability


## Testing Completed

- Database connection test
- Database integrity test
- Dashboard verification
- Voucher generation test
- Voucher management test


## Architecture Status

SQLite is the single source of truth.

CSV files are preserved only for historical migration purposes.



# Version 1.1.0 - Pricing and Revenue Foundation

Date:
2026-07-27


## Added

### Pricing System

Current pricing:

- 2 HOURS: 25 Gdes
- 4 HOURS: 50 Gdes
- 24 HOURS: 100 Gdes
- PREMIUM 7 DAYS: 700 Gdes


### Sales Tracking

Added:

- Sold status tracking
- Sold date tracking
- Sold amount tracking


### Revenue Dashboard

Added:

- Total sales
- Revenue calculation
- Revenue by plan


### Inventory Valuation

Added:

- Available voucher value calculation


## Status

Stable milestone completed.



# Version 1.0.0 - Initial Stable Release

Date:
2026-07-25


## Added

- Voucher generation system
- Multiple hotspot plans
- MikroTik RouterOS export
- Master inventory management
- Batch history tracking
- Voucher lifecycle management
- Status protection
- Inventory dashboard
- Data integrity verification


## Supported Plans

- 2 HOURS
- 4 HOURS
- 24 HOURS
- PREMIUM 7 DAYS