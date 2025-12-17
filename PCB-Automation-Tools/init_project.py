import os
import sys
import datetime

def create_project_structure(project_name):
    """
    Automated Project Initializer for Yang-Tech-Lab.
    Generates standard folder structure for hardware engineering projects.
    """
    # 1. Define the standard directory structure
    # A professional structure impresses clients immediately
    folders = [
        "01_Datasheets",       # Component specifications and data
        "02_Schematics",       # Circuit diagrams (PDF/Sch)
        "03_PCB_Gerber",       # Manufacturing files (Gerber, BOM, CPL)
        "04_Firmware",         # Source code (ESP32/STM32/Python)
        "05_3D_Models",        # Mechanical files and renders
        "06_Docs"              # Invoices, Quotes, Requirements
    ]

    # Get current working directory
    base_path = os.getcwd()
    
    # Define project root path
    project_path = os.path.join(base_path, project_name)
    
    print(f"🚀 Initializing project: {project_name} ...")
    
    try:
        # Create the main project directory
        os.makedirs(project_path, exist_ok=True)
        
        # 2. Create sub-directories
        for folder in folders:
            folder_path = os.path.join(project_path, folder)
            os.makedirs(folder_path, exist_ok=True)
            print(f"   ✅ Created: {folder}/")
            
        # 3. Generate a README file with project metadata
        readme_content = f"""# {project_name}
Created by: Yang-Tech-Lab
Date: {datetime.datetime.now().strftime("%Y-%m-%d")}

## Project Structure
- 01_Datasheets: Component specifications
- 03_PCB_Gerber: Production files for JLCPCB
- 04_Firmware: Source code

Thank you for choosing Yang-Tech-Lab!
"""
        with open(os.path.join(project_path, "README.txt"), "w", encoding="utf-8") as f:
            f.write(readme_content)
            print("   📄 Created: README.txt")

        print(f"\n✨ Project {project_name} setup complete!")
        print(f"📂 Location: {project_path}")

    except Exception as e:
        print(f"❌ Error: {e}")

# --- Main Entry Point ---
if __name__ == "__main__":
    print("--- Yang-Tech-Lab Project Initializer ---")
    p_name = input("Enter new project name (e.g., YTL_001): ").strip()
    
    if p_name:
        create_project_structure(p_name)
    else:
        print("❌ Project name cannot be empty!")