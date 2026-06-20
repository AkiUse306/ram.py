"""
Debugging and Diagnostics Module
Tools for debugging, profiling, and diagnosing your code
"""

import sys
import traceback
from functools import wraps
from datetime import datetime


def trace(func=None):
    """
    Decorator to trace function calls
    
    Args:
        func: Function to trace
    
    Returns:
        Wrapped function with trace output
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"🔍 [{timestamp}] Calling: {f.__name__}")
            print(f"   Args: {args}")
            print(f"   Kwargs: {kwargs}")
            
            try:
                result = f(*args, **kwargs)
                print(f"   Result: {result}")
                return result
            except Exception as e:
                print(f"   ❌ Error: {e}")
                raise
        return wrapper
    
    if func is not None:
        return decorator(func)
    return decorator


def log_info(message, level="INFO"):
    """
    Log information message
    
    Args:
        message (str): Message to log
        level (str): Log level (INFO, WARNING, ERROR, DEBUG)
    
    Returns:
        dict: Log entry
    """
    timestamp = datetime.now().isoformat()
    
    level_symbols = {
        "INFO": "ℹ️ ",
        "WARNING": "⚠️ ",
        "ERROR": "❌",
        "DEBUG": "🐛"
    }
    
    symbol = level_symbols.get(level, "•")
    
    print(f"{symbol} [{timestamp}] {level}: {message}")
    
    return {
        "timestamp": timestamp,
        "level": level,
        "message": message
    }


def get_stack_trace():
    """
    Get current stack trace
    
    Returns:
        str: Stack trace information
    """
    return traceback.format_stack()


def print_stack_trace():
    """
    Print current stack trace
    """
    traceback.print_stack()


def assert_value(condition, message="Assertion failed"):
    """
    Assert a condition
    
    Args:
        condition: Condition to check
        message (str): Error message if assertion fails
    
    Raises:
        AssertionError: If condition is False
    """
    if not condition:
        raise AssertionError(message)


def debug_print(*args, **kwargs):
    """
    Debug print with prefix
    
    Args:
        *args: Values to print
        **kwargs: Keyword arguments for print function
    """
    print("🐛 DEBUG:", *args, **kwargs)


__all__ = ['trace', 'log_info', 'get_stack_trace', 'print_stack_trace', 'assert_value', 'debug_print']
