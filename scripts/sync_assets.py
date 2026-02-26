import shutil
import sys
from pathlib import Path

def sync_assets():
    root_dir = Path(__file__).parent.parent.resolve()
    devsquad_src = root_dir / ".devsquad"
    cli_assets_dir = root_dir / "dev-squad-cli" / "dev_squad" / "assets" / ".devsquad"
    
    if not devsquad_src.exists():
        print(f"Error: Source directory {devsquad_src} does not exist. Run this script from the project root.", file=sys.stderr)
        sys.exit(1)
        
    print(f"Syncing {devsquad_src} to {cli_assets_dir}...")
    
    # Define what needs to be synced inside the .devsquad folder for the internal installer
    folders_to_sync = ["agents", "rules", "skills", "workflows", "templates"]
    
    # Also sync mcp.json if it exists at the root of .devsquad
    files_to_sync = ["mcp.json.sample"]
    
    # 1. Clean destination and ensure it exists
    if cli_assets_dir.exists():
        shutil.rmtree(cli_assets_dir)
    cli_assets_dir.mkdir(parents=True, exist_ok=True)
    
    # 2. Copy folders
    for folder_name in folders_to_sync:
        src_folder = devsquad_src / folder_name
        dest_folder = cli_assets_dir / folder_name
        
        if src_folder.exists() and src_folder.is_dir():
            print(f"  Copying {folder_name}/")
            shutil.copytree(src_folder, dest_folder, dirs_exist_ok=True)
        else:
            print(f"  Warning: {folder_name}/ not found in source.")

    # 3. Copy files
    for file_name in files_to_sync:
        src_file = devsquad_src / file_name
        dest_file = cli_assets_dir / file_name
        
        # In the deployed version we usually want this to be mcp.json
        if file_name == "mcp.json.sample" and src_file.exists():
             shutil.copy2(src_file, cli_assets_dir / "mcp.json")
             print(f"  Copied {file_name} as mcp.json")
        elif src_file.exists() and src_file.is_file():
            print(f"  Copying {file_name}")
            shutil.copy2(src_file, dest_file)
            
    print("Asset sync complete!")

if __name__ == "__main__":
    sync_assets()
