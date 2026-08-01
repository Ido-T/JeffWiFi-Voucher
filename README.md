# JeffWiFi Voucher Manager

## Version 2.5.3 - WISP Foundation Release

Date:
2026-08-01


## Overview

JeffWiFi Voucher Manager is a Python-based WiFi voucher management system designed for MikroTik Hotspot environments.

The project started as a simple voucher generator and has evolved into the foundation of a future WISP (Wireless Internet Service Provider) management platform.


## Current Architecture
Python Application
|
V
SQLite Database
|
V
MikroTik RouterOS Integration



## Completed Features


## Voucher Management

- Secure voucher generation using Python `secrets` module
- Protection against ambiguous characters
- Multiple hotspot plans
- Voucher lifecycle management
- Database duplicate prevention

Voucher lifecycle:
AVAILABLE
|
V
SOLD
|
V
USED


## Database System

- Migrated from CSV storage to SQLite
- Database integrity checks
- Foreign key validation
- Database constraints
- Transaction handling
- Performance indexes
- Duplicate voucher protection
- Database audit tools


## Inventory and Sales

- Voucher inventory tracking
- Sales recording
- Revenue tracking
- Stock valuation
- Inventory dashboard


## Audit and Accountability

- Voucher action logging
- Sales history
- Usage activation history
- Database integrity reports


## MikroTik Integration

- RouterOS `.rsc` export
- Hotspot user creation
- Configurable hotspot server
- Export validation
- Export history tracking

Tested successfully with:

- MikroTik hAP ax3
- RouterOS Hotspot


## Project Structure
JeffWiFi-Voucher/

    main.py
    config.py
    generator.py
    inventory.py
    exporter.py
    voucher_manager.py
    inventory_dashboard.py

    database/
        SQLite database tools
        migrations
        database management

    tests/
        application tests
        database integrity tests

    documentation/
        project documentation
        changelog
        project history



## Running the Application

```markdown
Generate vouchers:

```bash
python main.py



View inventory dashboard:

python inventory_dashboard.py

Run database integrity audit:

python tests/database/full_database_audit.py

Run tests:

python tests/test_generation_pipeline.py

python tests/test_export_validation.py

python tests/test_export_history.py

Future WISP Roadmap

JeffWiFi is designed to grow into a complete WISP management platform.

Future features:

User accounts
Roles and permissions
Operator accountability
Customer management
Payment architecture
MonCash integration
NatCash integration
MikroTik device management
Multiple locations and zones
Web dashboard
API integration
Network monitoring
Current Status

JeffWiFi v2.5.3 Foundation Release

This version provides a stable foundation for future WISP operational features.

