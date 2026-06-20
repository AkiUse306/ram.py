#!/usr/bin/env python3
"""
RAM.py Library Manager Application
A desktop application for managing and accessing the RAM.py library with Package ID authentication.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import uuid
import os
from datetime import datetime
import webbrowser

# Valid Package IDs (demo)
VALID_PACKAGE_IDS = [
    '550e8400-e29b-41d4-a716-446655440000',
    '6ba7b810-9dad-11d1-80b4-00c04fd430c8',
    '6ba7b811-9dad-11d1-80b4-00c04fd430c8',
]

# Available Modules
MODULES = {
    'ramtools': {
        'description': 'Core library utilities and main entry point',
        'functions': ['start()', 'initialize()', 'version()'],
        'color': '#0078d4'
    },
    'filetools': {
        'description': 'File management and organization utilities',
        'functions': ['organize(path)', 'clean_downloads()', 'sort_by_type()'],
        'color': '#107c10'
    },
    'speed': {
        'description': 'Performance optimization tools',
        'functions': ['superboost(data)', 'optimize_memory()', 'cache_enable()'],
        'color': '#f25022'
    },
    'debug': {
        'description': 'Debugging helpers and utilities',
        'functions': ['trace()', 'profile()', 'log_info()'],
        'color': '#7fba00'
    },
    'data': {
        'description': 'Data processing and manipulation tools',
        'functions': ['process()', 'filter()', 'transform()'],
        'color': '#00a4ef'
    },
    'utils': {
        'description': 'General utility functions',
        'functions': ['convert()', 'format_data()', 'validate()'],
        'color': '#ffb900'
    }
}

CODE_EXAMPLES = {
    'Basic Usage': '''from ramtools import start

# Start RAM.py
start("YOUR_PROJECT_PATH")''',
    
    'File Organization': '''from ramtools import filetools

# Organize your Downloads folder
filetools.organize("./Downloads")

# Clean up files
filetools.clean_downloads()''',
    
    'Performance Boost': '''from ramtools import speed

# Supercharge your data
data = [1, 2, 3, 4, 5]
result = speed.superboost(data)
print(result)''',
    
    'Debugging': '''from ramtools import debug

# Debug your code
debug.trace()
debug.profile()''',
    
    'Data Processing': '''from ramtools import data

# Process data efficiently
result = data.process(dataset)
filtered = data.filter(result)''',
}


class RAMLibraryManager:
    def __init__(self, root):
        self.root = root
        self.root.title("RAM.py Library Manager v1.0")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f0f0')
        
        # Set window icon appearance
        self.root.resizable(True, True)
        self.authenticated = False
        self.current_package_id = None
        
        # Style configuration
        self.setup_styles()
        
        # Create main frames
        self.create_ui()
        
    def setup_styles(self):
        """Configure ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        style.configure('TFrame', background='#f0f0f0')
        style.configure('Title.TLabel', background='#f0f0f0', font=('Segoe UI', 18, 'bold'), foreground='#0078d4')
        style.configure('Subtitle.TLabel', background='#f0f0f0', font=('Segoe UI', 11), foreground='#555555')
        style.configure('TButton', font=('Segoe UI', 10))
        
    def create_ui(self):
        """Create the main user interface"""
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        # Create login screen
        self.login_frame = ttk.Frame(self.main_frame)
        self.login_frame.pack(fill=tk.BOTH, expand=True)
        self.create_login_screen()
        
        # Create library screen (hidden initially)
        self.library_frame = ttk.Frame(self.main_frame)
        self.library_frame.pack(fill=tk.BOTH, expand=True)
        self.create_library_screen()
        
        # Show login screen
        self.show_login_screen()
        
    def create_login_screen(self):
        """Create the login/authentication screen"""
        # Center container
        center_frame = ttk.Frame(self.login_frame)
        center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=500, height=400)
        
        # Add white background
        login_box = tk.Frame(center_frame, bg='white', relief=tk.FLAT, bd=1)
        login_box.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(login_box, text='Welcome to RAM.py', font=('Segoe UI', 20, 'bold'), 
                               bg='white', fg='#0078d4')
        title_label.pack(pady=(30, 10))
        
        # Subtitle
        subtitle_label = tk.Label(login_box, text='Enter your Package ID to access the library', 
                                  font=('Segoe UI', 11), bg='white', fg='#666666')
        subtitle_label.pack(pady=(0, 30))
        
        # Package ID input
        label = tk.Label(login_box, text='Package ID (GUID):', font=('Segoe UI', 10, 'bold'), 
                        bg='white', fg='#333333')
        label.pack(anchor=tk.W, padx=30, pady=(0, 5))
        
        self.package_id_entry = tk.Entry(login_box, font=('Consolas', 10), width=40)
        self.package_id_entry.pack(padx=30, pady=(0, 20))
        self.package_id_entry.insert(0, '550e8400-e29b-41d4-a716-446655440000')
        
        # Continue button
        continue_btn = tk.Button(login_box, text='Continue', font=('Segoe UI', 11, 'bold'),
                                bg='#0078d4', fg='white', activebackground='#106ebe', 
                                relief=tk.FLAT, bd=0, cursor='hand2', command=self.authenticate)
        continue_btn.pack(fill=tk.X, padx=30, pady=(0, 20))
        
        # Status label
        self.status_label = tk.Label(login_box, text='', font=('Segoe UI', 9), bg='white', fg='#d13438')
        self.status_label.pack(pady=(0, 10))
        
        # Separator
        sep_frame = tk.Frame(login_box, height=1, bg='#e0e0e0')
        sep_frame.pack(fill=tk.X, padx=30, pady=20)
        
        # Forgot ID section
        forgot_label = tk.Label(login_box, text="Don't have your Package ID?", font=('Segoe UI', 10, 'bold'),
                               bg='white', fg='#666666')
        forgot_label.pack(anchor=tk.W, padx=30, pady=(0, 5))
        
        help_text = tk.Label(login_box, text='Run this command in your terminal:', font=('Segoe UI', 9),
                            bg='white', fg='#666666')
        help_text.pack(anchor=tk.W, padx=30, pady=(0, 5))
        
        cmd_frame = tk.Frame(login_box, bg='#f5f5f5', relief=tk.FLAT, bd=1)
        cmd_frame.pack(fill=tk.X, padx=30, pady=(0, 20))
        
        cmd_label = tk.Label(cmd_frame, text='ramtools getpkg_id', font=('Consolas', 9),
                            bg='#f5f5f5', fg='#333333')
        cmd_label.pack(padx=10, pady=8)
        
    def create_library_screen(self):
        """Create the main library screen"""
        # Clear previous content
        for widget in self.library_frame.winfo_children():
            widget.destroy()
        
        # Header frame
        header_frame = tk.Frame(self.library_frame, bg='white', relief=tk.FLAT, bd=1, height=100)
        header_frame.pack(fill=tk.X)
        
        # Welcome message
        welcome_label = tk.Label(header_frame, text='Welcome to RAM.py Library', 
                                font=('Segoe UI', 16, 'bold'), bg='white', fg='#0078d4')
        welcome_label.pack(anchor=tk.W, padx=30, pady=(20, 5))
        
        # Package ID display
        pkg_label = tk.Label(header_frame, text='Your Package ID:', 
                            font=('Segoe UI', 10), bg='white', fg='#666666')
        pkg_label.pack(anchor=tk.W, padx=30, pady=(5, 3))
        
        pkg_id_display = tk.Label(header_frame, text=self.current_package_id, 
                                 font=('Consolas', 9), bg='#f5f5f5', fg='#333333', 
                                 relief=tk.FLAT, bd=1)
        pkg_id_display.pack(anchor=tk.W, padx=30, pady=(0, 20), fill=tk.X)
        
        # Content area with notebook (tabs)
        notebook = ttk.Notebook(self.library_frame)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Modules Tab
        modules_frame = ttk.Frame(notebook)
        notebook.add(modules_frame, text='Modules')
        self.create_modules_tab(modules_frame)
        
        # Examples Tab
        examples_frame = ttk.Frame(notebook)
        notebook.add(examples_frame, text='Code Examples')
        self.create_examples_tab(examples_frame)
        
        # Footer frame with logout
        footer_frame = tk.Frame(self.library_frame, bg='#f0f0f0')
        footer_frame.pack(fill=tk.X, padx=10, pady=10)
        
        logout_btn = tk.Button(footer_frame, text='Logout', font=('Segoe UI', 10, 'bold'),
                              bg='#d13438', fg='white', activebackground='#c50f1f',
                              relief=tk.FLAT, bd=0, cursor='hand2', command=self.logout)
        logout_btn.pack(anchor=tk.E, padx=0, pady=5)
        
    def create_modules_tab(self, parent):
        """Create modules display tab"""
        # Create canvas with scrollbar
        canvas_frame = ttk.Frame(parent)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        canvas = tk.Canvas(canvas_frame, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            '<Configure>',
            lambda e: canvas.configure(scrollregion=canvas.bbox('all'))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Create module cards
        for module_name, module_info in MODULES.items():
            self.create_module_card(scrollable_frame, module_name, module_info)
    
    def create_module_card(self, parent, name, info):
        """Create a single module card"""
        card = tk.Frame(parent, bg='white', relief=tk.FLAT, bd=1)
        card.pack(fill=tk.X, pady=10, padx=5)
        
        # Card header with color accent
        header = tk.Frame(card, bg=info['color'], height=4)
        header.pack(fill=tk.X)
        
        # Card content
        content = tk.Frame(card, bg='white')
        content.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        # Module name
        name_label = tk.Label(content, text=name, font=('Segoe UI', 12, 'bold'), 
                             bg='white', fg='#333333')
        name_label.pack(anchor=tk.W)
        
        # Description
        desc_label = tk.Label(content, text=info['description'], font=('Segoe UI', 10),
                             bg='white', fg='#666666', wraplength=400, justify=tk.LEFT)
        desc_label.pack(anchor=tk.W, pady=(5, 10))
        
        # Functions
        func_text = ', '.join(info['functions'])
        func_label = tk.Label(content, text=f'Functions: {func_text}', font=('Consolas', 9),
                             bg='#f5f5f5', fg='#333333', wraplength=400, justify=tk.LEFT)
        func_label.pack(anchor=tk.W, fill=tk.X, padx=5, pady=5)
    
    def create_examples_tab(self, parent):
        """Create code examples tab"""
        # Create canvas with scrollbar
        canvas_frame = ttk.Frame(parent)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        canvas = tk.Canvas(canvas_frame, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            '<Configure>',
            lambda e: canvas.configure(scrollregion=canvas.bbox('all'))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Create example cards
        for example_name, code in CODE_EXAMPLES.items():
            self.create_example_card(scrollable_frame, example_name, code)
    
    def create_example_card(self, parent, title, code):
        """Create a single code example card"""
        card = tk.Frame(parent, bg='white', relief=tk.FLAT, bd=1)
        card.pack(fill=tk.X, pady=10, padx=5)
        
        # Title
        title_label = tk.Label(card, text=title, font=('Segoe UI', 11, 'bold'),
                              bg='white', fg='#0078d4')
        title_label.pack(anchor=tk.W, padx=15, pady=(10, 5))
        
        # Code frame
        code_frame = tk.Frame(card, bg='#1e1e1e', relief=tk.FLAT, bd=1)
        code_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 10))
        
        # Code text
        code_label = tk.Label(code_frame, text=code, font=('Consolas', 9),
                             bg='#1e1e1e', fg='#d4d4d4', justify=tk.LEFT)
        code_label.pack(anchor=tk.NW, padx=10, pady=10)
    
    def authenticate(self):
        """Handle authentication"""
        package_id = self.package_id_entry.get().strip()
        
        # Validate GUID format
        guid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
        import re
        
        if re.match(guid_pattern, package_id, re.IGNORECASE) or package_id in VALID_PACKAGE_IDS:
            self.authenticated = True
            self.current_package_id = package_id
            self.show_library_screen()
        else:
            self.status_label.config(text='❌ Invalid Package ID format. Must be a valid GUID.',
                                    fg='#d13438')
    
    def show_login_screen(self):
        """Show the login screen"""
        self.library_frame.pack_forget()
        self.login_frame.pack(fill=tk.BOTH, expand=True)
    
    def show_library_screen(self):
        """Show the library screen"""
        self.login_frame.pack_forget()
        
        # Recreate library screen with current package ID
        for widget in self.library_frame.winfo_children():
            widget.destroy()
        
        self.create_library_screen()
        self.library_frame.pack(fill=tk.BOTH, expand=True)
    
    def logout(self):
        """Handle logout"""
        self.authenticated = False
        self.current_package_id = None
        self.package_id_entry.delete(0, tk.END)
        self.package_id_entry.insert(0, '550e8400-e29b-41d4-a716-446655440000')
        self.status_label.config(text='')
        self.show_login_screen()


def main():
    """Main application entry point"""
    root = tk.Tk()
    app = RAMLibraryManager(root)
    root.mainloop()


if __name__ == '__main__':
    main()
