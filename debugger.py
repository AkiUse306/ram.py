#!/usr/bin/env python3
"""
RAM.py Debugger with Autocomplete
An interactive Python debugger with intelligent suggestions
"""

import sys
import os
import code
import inspect
from pathlib import Path

# Add RAM LIB to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from ramtools import *
except ImportError:
    pass


class RAMDebugger(code.InteractiveConsole):
    """Interactive debugger with RAM.py and autocomplete suggestions"""
    
    def __init__(self, locals=None, filename="<console>"):
        if locals is None:
            locals = {
                'start': start,
                'superboost': superboost,
                'organize': organize,
                'clean_downloads': clean_downloads,
                'filter': filter,
                'transform': transform,
                'process': process,
                'log_info': log_info,
                'trace': trace,
                'optimize_memory': optimize_memory,
                'cache_enable': cache_enable,
                'profile': profile,
                'convert': convert,
                'validate': validate,
                'timestamp': timestamp,
                'flatten': flatten,
                'merge': merge,
                '__name__': '__console__',
                '__doc__': None,
            }
        
        super().__init__(locals, filename)
        self.suggestions = self._get_suggestions()
    
    def _get_suggestions(self):
        """Get available RAM.py functions and modules for suggestions"""
        suggestions = {
            'start': 'Initialize RAM.py',
            'superboost': 'Optimize and deduplicate data',
            'organize': 'Organize files by type',
            'clean_downloads': 'Clean downloads folder',
            'filter': 'Filter data using predicate',
            'transform': 'Transform data with mapper',
            'process': 'Process data with operation',
            'log_info': 'Log information message',
            'trace': 'Trace function calls',
            'optimize_memory': 'Optimize memory usage',
            'cache_enable': 'Enable caching',
            'profile': 'Profile function performance',
            'convert': 'Convert between types',
            'validate': 'Validate data',
            'timestamp': 'Get current timestamp',
            'flatten': 'Flatten nested structures',
            'merge': 'Merge multiple datasets',
        }
        return suggestions
    
    def runsource(self, source, filename="<input>", symbol="single"):
        """Override to add suggestions"""
        # Check if user is typing a function name
        words = source.strip().split()
        if words and words[0] in self.suggestions:
            func_name = words[0]
            print(f"💡 Suggestion: {func_name} - {self.suggestions[func_name]}")
        
        return super().runsource(source, filename, symbol)
    
    def interact(self, banner=""):
        """Start the interactive debugger"""
        cprt = 'Type "help", "copyright", "credits" or "license" for more information.'
        if not banner:
            banner = f"""RAM.py Debugger v1.0
{cprt}

Available functions:
  start()           - Initialize RAM.py
  superboost()      - Optimize data
  organize()        - Organize files
  filter()          - Filter data
  transform()       - Transform data
  log_info()        - Log messages
  trace()           - Trace functions
  
Type a function name and press Enter to see suggestions.
Type 'help(function_name)' for detailed help.
Type 'exit()' or Ctrl+D to quit.
"""
        
        super().interact(banner=banner, exitmsg='Exiting RAM.py Debugger...')


def main():
    """Main entry point"""
    debugger = RAMDebugger()
    debugger.interact()


if __name__ == '__main__':
    main()
