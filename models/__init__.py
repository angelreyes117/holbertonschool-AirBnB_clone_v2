#!/usr/bin/python3
"""
Models package initialization.

Instantiates the storage engine (FileStorage or DBStorage)
based on the HBNB_TYPE_STORAGE environment variable,
and calls reload() to load any existing data.
"""

import os
from models.engine import file_storage, db_storage

# Determine which storage engine to use
storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    # Database storage
    storage = db_storage.DBStorage()
else:
    # File (JSON) storage
    storage = file_storage.FileStorage()

# Load existing data from storage
storage.reload()

