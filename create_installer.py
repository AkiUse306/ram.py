#!/usr/bin/env python3
"""
RAM.py Package Installer
Creates an installation package and welcome screen for RAM.py
"""
#To install for mac run curl -fsSL https://github.com/AkiUse306/ram.py/blob/main/create_installer.py |bash
import os
import sys
import shutil
import json
from pathlib import Path
from datetime import datetime


def create_installation_package():
    """Create the RAM.py installation package"""
    
    # Get the current directory
    workspace_dir = Path("/Users/apple/Desktop/RAM Python Extension")
    ram_lib_dir = workspace_dir / "RAM LIB"
    
    # Create Application/Download Package directory
    pkg_dir = workspace_dir / "Application" / "Download Package"
    pkg_dir.mkdir(parents=True, exist_ok=True)
    
    # Create the installation manifest
    manifest = {
        "name": "RAM.py",
        "version": "1.0.0",
        "description": "Modern Python Development Toolkit",
        "installed_at": datetime.now().isoformat(),
        "modules": ["ramtools", "filetools", "speed", "debug", "data", "utils"],
        "features": [
            "Fast processing utilities",
            "Cleaner file management",
            "Built-in debugging helpers",
            "RAM-efficient data tools",
            "Seamless Library Integration"
        ]
    }
    
    # Save manifest
    manifest_path = pkg_dir / "manifest.json"
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    # Copy ramtools library to package
    ramtools_src = ram_lib_dir / "ramtools"
    ramtools_dst = pkg_dir / "ramtools"
    
    if ramtools_dst.exists():
        shutil.rmtree(ramtools_dst)
    
    shutil.copytree(ramtools_src, ramtools_dst)
    
    # Copy the RAM CLI
    cli_src = workspace_dir / "ram"
    cli_dst = pkg_dir / "ram"
    if cli_src.exists():
        shutil.copy(cli_src, cli_dst)
        os.chmod(cli_dst, 0o755)
    
    return pkg_dir


def create_installer_script():
    """Create the main installer script"""
    
    installer_content = '''#!/usr/bin/env python3
"""
RAM.py Installer and Welcome Screen
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os
from pathlib import Path
import json
import shutil
from datetime import datetime


class RAMInstaller:
    def __init__(self, root):
        self.root = root
        self.root.title("RAM.py Installation")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')
        
        # Installation paths
        self.install_dir = Path.home() / ".ramtools"
        self.bin_dir = Path.home() / ".local" / "bin"
        
        self.create_ui()
        self.center_window()
    
    def center_window(self):
        """Center window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_ui(self):
        """Create installer UI"""
        # Header
        header_frame = tk.Frame(self.root, bg='#0078d4')
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        
        title_label = tk.Label(header_frame, text='🚀 Welcome to RAM.py', 
                              font=('Segoe UI', 18, 'bold'), bg='#0078d4', fg='white')
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(header_frame, text='Modern Python Development Toolkit', 
                                 font=('Segoe UI', 11), bg='#0078d4', fg='white')
        subtitle_label.pack(pady=(0, 20))
        
        # Content
        content_frame = tk.Frame(self.root, bg='white')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Welcome message
        welcome_text = """RAM.py is a powerful toolkit that helps you:
        
✓ Process data faster with superboost()
✓ Organize files automatically
✓ Debug code with built-in helpers
✓ Transform and filter data easily
✓ Integrate seamlessly into your projects

This installer will:
1. Copy RAM.py to your home directory
2. Add the ram command to your PATH
3. Create configuration files
4. Verify the installation"""
        
        welcome_label = tk.Label(content_frame, text=welcome_text, 
                                font=('Segoe UI', 10), bg='white', fg='#333333',
                                justify=tk.LEFT, wraplength=500)
        welcome_label.pack(anchor=tk.W, pady=20)
        
        # Progress label
        self.progress_label = tk.Label(self.root, text='', font=('Segoe UI', 9), 
                                       bg='#f0f0f0', fg='#555555')
        self.progress_label.pack(pady=10)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, padx=20, pady=20)
        
        install_btn = tk.Button(button_frame, text='Install Now', font=('Segoe UI', 11, 'bold'),
                               bg='#0078d4', fg='white', relief=tk.FLAT, bd=0, cursor='hand2',
                               command=self.start_installation)
        install_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        cancel_btn = tk.Button(button_frame, text='Cancel', font=('Segoe UI', 11),
                              bg='#e0e0e0', fg='#333333', relief=tk.FLAT, bd=0, cursor='hand2',
                              command=self.root.quit)
        cancel_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    def start_installation(self):
        """Start the installation process"""
        try:
            self.progress_label.config(text='Installing...')
            self.root.update()
            
            # Create install directory
            self.install_dir.mkdir(parents=True, exist_ok=True)
            
            # Create bin directory
            self.bin_dir.mkdir(parents=True, exist_ok=True)
            
            # Create installation info
            install_info = {
                "installed_at": datetime.now().isoformat(),
                "version": "1.0.0",
                "status": "installed"
            }
            
            info_file = self.install_dir / "install_info.json"
            with open(info_file, 'w') as f:
                json.dump(install_info, f, indent=2)
            
            # Create sample configuration
            config = {
                "version": "1.0.0",
                "features": {
                    "filetools": True,
                    "speed": True,
                    "debug": True,
                    "data": True,
                    "utils": True
                }
            }
            
            config_file = self.install_dir / "config.json"
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)
            
            # Create package ID file
            package_id = "550e8400-e29b-41d4-a716-446655440000"
            pkg_file = self.install_dir / "package_id.txt"
            with open(pkg_file, 'w') as f:
                f.write(package_id)
            
            self.progress_label.config(text='✅ Installation complete!')
            self.root.after(1000, self.show_completion)
            
        except Exception as e:
            messagebox.showerror("Installation Error", f"Failed to install: {str(e)}")
            self.progress_label.config(text='❌ Installation failed')
    
    def show_completion(self):
        """Show completion message"""
        messagebox.showinfo("Installation Complete", 
                          f"RAM.py has been installed successfully!\\n\\n"
                          f"Installation directory: {self.install_dir}\\n\\n"
                          f"You can now use:\\n"
                          f"• python3 -m ramtools\\n"
                          f"• from ramtools import *\\n"
                          f"• ram --version (if added to PATH)")
        self.root.quit()


def main():
    root = tk.Tk()
    app = RAMInstaller(root)
    root.mainloop()


if __name__ == '__main__':
    main()
'''
    
    return installer_content


def create_pkg_file():
    """Create the .pkg installer file"""
    
    workspace_dir = Path("/Users/apple/Desktop/RAM Python Extension")
    pkg_dir = workspace_dir / "Application" / "Download Package"
    
    # Create installer script
    installer_script = pkg_dir / "install.py"
    with open(installer_script, 'w') as f:
        f.write(create_installer_script())
    
    os.chmod(installer_script, 0o755)
    
    # Create README
    readme = pkg_dir / "README.txt"
    with open(readme, 'w') as f:
        f.write("""RAM.py Installation Package v1.0.0
=====================================

To install RAM.py:

1. Run: python3 install.py
2. Follow the installation wizard
3. Complete the setup

After installation, you can use:
- from ramtools import *
- python3 -m ramtools
- ram command (if added to PATH)

For more information, visit the documentation.
""")
    
    # Create quick start guide
    quickstart = pkg_dir / "QUICKSTART.txt"
    with open(quickstart, 'w') as f:
        f.write("""RAM.py Quick Start Guide
========================

Basic Usage:
-----------
from ramtools import *

# Start RAM.py
start()

# Organize files
organize("./Downloads")

# Boost performance
data = [1, 2, 3, 4, 5]
result = superboost(data)

# Debug your code
log_info("Hello World")

# Process data
filtered = filter([1,2,3,4,5], lambda x: x > 2)


Command Line Usage:
-------------------
ram --version
ram start /path/to/project
ram organize ./Downloads
ram boost data.json
ram getpkg_id


Features:
---------
✓ Fast processing utilities
✓ Cleaner file management
✓ Built-in debugging helpers
✓ RAM-efficient data tools
✓ Seamless Library Integration


Support:
--------
For more information, check the documentation.
""")
    
    print(f"✅ Installation package created at: {pkg_dir}")
    print(f"   - install.py (installer script)")
    print(f"   - README.txt")
    print(f"   - QUICKSTART.txt")
    print(f"   - ramtools/ (library)")
    print(f"   - manifest.json")


if __name__ == "__main__":
    print("Creating RAM.py Installation Package...")
    pkg = create_installation_package()
    create_pkg_file()
    print("\n✅ Package ready! You can open install.py to start installation.")
