from pathlib import Path


# =====================================
# JEFF WIFI CONFIGURATION
# =====================================


# Project base folder

BASE_DIR = Path(__file__).parent



# =====================================
# FILE LOCATIONS
# =====================================


# Master inventory database

INVENTORY_FILE = (
    BASE_DIR /
    "inventory" /
    "master_inventory.csv"
)



# Batch history

BATCH_HISTORY_FILE = (
    BASE_DIR /
    "inventory" /
    "batch_history.csv"
)



# Generated voucher files

VOUCHER_FOLDER = (
    BASE_DIR /
    "vouchers"
)



# MikroTik import files

IMPORT_FOLDER = (
    BASE_DIR /
    "imports"
)



# Voucher cards

CARD_FOLDER = (
    BASE_DIR /
    "cards"
)



# Backup folder

BACKUP_FOLDER = (
    BASE_DIR /
    "backups"
)




# =====================================
# VOUCHER PLANS
# =====================================


PLANS = {

    "1": {

        "name": "2 HOURS",
        "prefix": "2H-",
        "profile": "2-HOURS",
        "price": 25,
        "limit_uptime": "2h"

    },


    "2": {

        "name": "4 HOURS",
        "prefix": "4H-",
        "profile": "4-HOURS",
        "price": 50,
        "limit_uptime": "4h"

    },


    "3": {

        "name": "24 HOURS",
        "prefix": "24H-",
        "profile": "24-HOURS",
        "price": 100,
        "limit_uptime": "24h"

    },


    "4": {

        "name": "PREMIUM 7 DAYS",
        "prefix": "7D-",
        "profile": "PREMIUM-7DAYS",
        "price": 700,
        "limit_uptime": "7d"

    }

}

# ==========================
# MikroTik Configuration
# ==========================

MIKROTIK = {

    "hotspot_server": "hotspot1"

}