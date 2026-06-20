"""
File Management and Organization Module
Organize, clean, and manage your files efficiently
"""

import shutil
from pathlib import Path
from datetime import datetime


def organize(directory):
    """
    Organize files in a directory by type
    
    Args:
        directory (str): Directory path to organize
    
    Returns:
        dict: Organization results
    """
    path = Path(directory).expanduser()
    
    if not path.exists():
        return {"status": "error", "message": f"Directory does not exist: {directory}"}
    
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.xls', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.iso'],
        'Code': ['.py', '.js', '.java', '.cpp', '.c', '.html', '.css', '.json'],
    }
    
    organized_count = 0
    
    for category, extensions in categories.items():
        category_path = path / category
        
        for file in path.glob('*'):
            if file.is_file() and file.suffix.lower() in extensions:
                category_path.mkdir(exist_ok=True)
                try:
                    shutil.move(str(file), str(category_path / file.name))
                    organized_count += 1
                except Exception as e:
                    pass
    
    return {
        "status": "success",
        "files_organized": organized_count,
        "directory": str(path),
        "timestamp": datetime.now().isoformat()
    }


def clean_downloads(downloads_dir="~/Downloads"):
    """
    Clean and organize downloads directory
    
    Args:
        downloads_dir (str): Path to downloads directory
    
    Returns:
        dict: Cleanup results
    """
    return organize(downloads_dir)


def sort_by_type(directory):
    """
    Sort files by type in a directory
    
    Args:
        directory (str): Directory to sort
    
    Returns:
        dict: Sort results
    """
    return organize(directory)


def get_directory_size(directory):
    """
    Get total size of a directory
    
    Args:
        directory (str): Directory path
    
    Returns:
        dict: Size information
    """
    path = Path(directory).expanduser()
    
    if not path.exists():
        return {"status": "error", "message": "Directory does not exist"}
    
    total_size = sum(f.stat().st_size for f in path.rglob('*') if f.is_file())
    
    return {
        "status": "success",
        "directory": str(path),
        "size_bytes": total_size,
        "size_mb": round(total_size / (1024 * 1024), 2),
        "size_gb": round(total_size / (1024 * 1024 * 1024), 2)
    }


__all__ = ['organize', 'clean_downloads', 'sort_by_type', 'get_directory_size']
