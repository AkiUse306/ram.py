"""
RAM.py - Modern Python Development Toolkit
Core module for fast processing, file management, and optimization
"""

__version__ = "1.0.0"
__author__ = "RAM Development Team"

import os
from datetime import datetime
from pathlib import Path

# Import submodules
from . import filetools
from . import speed
from . import debug
from . import data
from . import utils

# Import main functions for direct access
from .filetools import organize, clean_downloads, sort_by_type, get_directory_size
from .speed import superboost, optimize_memory, cache_enable, profile, benchmark
from .debug import trace, log_info, get_stack_trace, print_stack_trace, assert_value, debug_print
from .data import process, filter, transform, aggregate, flatten, merge, to_json, from_json
from .utils import convert, format_data, validate, sanitize, slugify, timestamp, get_date_range, retry


def start(project_path=None):
    """
    Start RAM.py and initialize the environment
    
    Args:
        project_path (str): Path to your project (optional)
    
    Returns:
        dict: Initialization status
    """
    timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    result = {
        "status": "initialized",
        "timestamp": timestamp_str,
        "version": __version__
    }
    
    if project_path:
        path = Path(project_path).expanduser()
        if path.exists():
            result["project_path"] = str(path)
            result["project_exists"] = True
        else:
            result["project_exists"] = False
            result["warning"] = f"Project path does not exist: {project_path}"
    
    print(f"🚀 RAM.py initialized at {timestamp_str}")
    return result


def get_version():
    """Get the current version of RAM.py"""
    return __version__


# Define what gets imported with "from ramtools import *"
__all__ = [
    # Core functions
    'start',
    'get_version',
    
    # Submodules
    'filetools',
    'speed',
    'debug',
    'data',
    'utils',
    
    # File tools
    'organize',
    'clean_downloads',
    'sort_by_type',
    'get_directory_size',
    
    # Speed/Performance
    'superboost',
    'optimize_memory',
    'cache_enable',
    'profile',
    'benchmark',
    
    # Debug
    'trace',
    'log_info',
    'get_stack_trace',
    'print_stack_trace',
    'assert_value',
    'debug_print',
    
    # Data
    'process',
    'filter',
    'transform',
    'aggregate',
    'flatten',
    'merge',
    'to_json',
    'from_json',
    
    # Utils
    'convert',
    'format_data',
    'validate',
    'sanitize',
    'slugify',
    'timestamp',
    'get_date_range',
    'retry',
]

