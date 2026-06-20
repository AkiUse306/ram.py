"""
Utility Functions Module
General-purpose utilities for common tasks
"""

import re
from datetime import datetime, timedelta


def convert(value, target_type):
    """
    Convert value to target type
    
    Args:
        value: Value to convert
        target_type: Target type (str, int, float, bool, list, dict)
    
    Returns:
        Converted value
    """
    try:
        if target_type == str:
            return str(value)
        elif target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == bool:
            if isinstance(value, str):
                return value.lower() in ('true', '1', 'yes', 'on')
            return bool(value)
        elif target_type == list:
            if isinstance(value, (list, tuple)):
                return list(value)
            return [value]
        elif target_type == dict:
            if isinstance(value, dict):
                return value
            return {"value": value}
    except (ValueError, TypeError):
        return None


def format_data(data, format_type="json"):
    """
    Format data in different ways
    
    Args:
        data: Data to format
        format_type: Format type (json, csv, xml, etc.)
    
    Returns:
        Formatted data as string
    """
    import json
    
    if format_type == "json":
        return json.dumps(data, indent=2)
    elif format_type == "csv" and isinstance(data, list):
        return "\n".join([",".join(str(v) for v in row) for row in data])
    elif format_type == "str":
        return str(data)
    
    return str(data)


def validate(value, rule):
    """
    Validate value against rule
    
    Args:
        value: Value to validate
        rule: Validation rule (dict with pattern, type, min, max, etc.)
    
    Returns:
        bool: True if valid, False otherwise
    """
    if 'type' in rule:
        if type(value).__name__ != rule['type']:
            return False
    
    if 'pattern' in rule:
        if not re.match(rule['pattern'], str(value)):
            return False
    
    if 'min' in rule:
        if len(value) if hasattr(value, '__len__') else value < rule['min']:
            return False
    
    if 'max' in rule:
        if len(value) if hasattr(value, '__len__') else value > rule['max']:
            return False
    
    return True


def sanitize(text):
    """
    Sanitize text by removing special characters
    
    Args:
        text: Text to sanitize
    
    Returns:
        Sanitized text
    """
    return re.sub(r'[^a-zA-Z0-9_\-\s]', '', str(text))


def slugify(text):
    """
    Convert text to URL-friendly slug
    
    Args:
        text: Text to slugify
    
    Returns:
        Slugified text
    """
    text = str(text).lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text


def timestamp():
    """
    Get current timestamp
    
    Returns:
        str: Current timestamp
    """
    return datetime.now().isoformat()


def get_date_range(days=7):
    """
    Get date range
    
    Args:
        days: Number of days (default: 7)
    
    Returns:
        dict: Start and end dates
    """
    end = datetime.now()
    start = end - timedelta(days=days)
    
    return {
        "start": start.isoformat(),
        "end": end.isoformat(),
        "days": days
    }


def retry(max_attempts=3, delay=1):
    """
    Decorator for retry logic
    
    Args:
        max_attempts: Maximum number of attempts
        delay: Delay between attempts in seconds
    
    Returns:
        Decorator function
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            import time
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    time.sleep(delay)
            return None
        return wrapper
    return decorator


__all__ = ['convert', 'format_data', 'validate', 'sanitize', 'slugify', 'timestamp', 'get_date_range', 'retry']
