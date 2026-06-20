"""
Data Processing and Manipulation Module
Advanced tools for processing, filtering, and transforming data
"""

import json
from functools import reduce
from operator import itemgetter


def process(data, operation=None):
    """
    Process data with optional operation
    
    Args:
        data: Data to process
        operation: Operation function (optional)
    
    Returns:
        Processed data
    """
    if operation is None:
        return data
    
    if isinstance(data, list):
        return [operation(item) for item in data]
    elif isinstance(data, dict):
        return {k: operation(v) for k, v in data.items()}
    else:
        return operation(data)


def filter(data, predicate):
    """
    Filter data based on predicate
    
    Args:
        data: Data to filter (list or dict)
        predicate: Filter function
    
    Returns:
        Filtered data
    """
    if isinstance(data, list):
        return [item for item in data if predicate(item)]
    elif isinstance(data, dict):
        return {k: v for k, v in data.items() if predicate(v)}
    else:
        return data


def transform(data, mapper):
    """
    Transform data using mapper function
    
    Args:
        data: Data to transform
        mapper: Transformation function
    
    Returns:
        Transformed data
    """
    if isinstance(data, list):
        return list(map(mapper, data))
    elif isinstance(data, dict):
        return {k: mapper(v) for k, v in data.items()}
    else:
        return mapper(data)


def aggregate(data, func=sum):
    """
    Aggregate data using function
    
    Args:
        data: Data to aggregate (list)
        func: Aggregation function (default: sum)
    
    Returns:
        Aggregated result
    """
    if isinstance(data, list):
        return func(data)
    return None


def flatten(data):
    """
    Flatten nested data structure
    
    Args:
        data: Nested data (list or dict)
    
    Returns:
        Flattened data
    """
    if isinstance(data, list):
        result = []
        for item in data:
            if isinstance(item, (list, tuple)):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result
    elif isinstance(data, dict):
        result = {}
        for k, v in data.items():
            if isinstance(v, dict):
                flat = flatten(v)
                result.update(flat)
            else:
                result[k] = v
        return result
    return data


def merge(data_list):
    """
    Merge multiple data structures
    
    Args:
        data_list: List of data to merge
    
    Returns:
        Merged data
    """
    if not data_list:
        return None
    
    if isinstance(data_list[0], dict):
        result = {}
        for item in data_list:
            result.update(item)
        return result
    elif isinstance(data_list[0], list):
        result = []
        for item in data_list:
            result.extend(item)
        return result
    
    return None


def to_json(data):
    """
    Convert data to JSON string
    
    Args:
        data: Data to convert
    
    Returns:
        JSON string
    """
    return json.dumps(data, indent=2)


def from_json(json_str):
    """
    Parse JSON string
    
    Args:
        json_str: JSON string
    
    Returns:
        Parsed data
    """
    return json.loads(json_str)


__all__ = ['process', 'filter', 'transform', 'aggregate', 'flatten', 'merge', 'to_json', 'from_json']
