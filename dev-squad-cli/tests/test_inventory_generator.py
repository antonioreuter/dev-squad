import pytest
import os
from pathlib import Path
from dev_squad.inventory_generator import InventoryGenerator

def test_auto_initialize_kb(tmp_path):
    # Setup
    kb_root = tmp_path / ".devsquad" / "knowledge"
    # kb_root does not exist initially
    
    metadata = {
        "language": "Python",
        "framework": "Unknown",
        "version": "Unknown",
        "structure": "Standard",
        "meta_files": ["pyproject.toml"],
        "gaps": []
    }
    
    generator = InventoryGenerator(project_root=str(tmp_path), metadata=metadata)
    generator.generate()
    
    assert kb_root.exists()
    assert (kb_root / "inventory").exists()
    assert (kb_root / "inventory" / "stack.md").exists()
    assert (kb_root / "inventory" / "structure.md").exists()

def test_inventory_content_generation(tmp_path):
    metadata = {
        "language": "JavaScript/TypeScript",
        "framework": "Next.js",
        "version": "15.0.0",
        "structure": "Next.js App Router",
        "meta_files": ["package.json"],
        "gaps": ["Unignored .env file detected"]
    }
    
    generator = InventoryGenerator(project_root=str(tmp_path), metadata=metadata)
    generator.generate()
    
    stack_file = tmp_path / ".devsquad" / "knowledge" / "inventory" / "stack.md"
    content = stack_file.read_text(encoding="utf-8")
    
    assert "JavaScript/TypeScript" in content
    assert "Next.js" in content
    assert "15.0.0" in content
    
    gaps_file = tmp_path / ".devsquad" / "knowledge" / "inventory" / "gaps.md"
    assert "Unignored .env file detected" in gaps_file.read_text(encoding="utf-8")

def test_preserve_manual_notes(tmp_path):
    metadata = {"language": "Python", "framework": "Unknown"}
    generator = InventoryGenerator(project_root=str(tmp_path), metadata=metadata)
    generator.generate()
    
    stack_file = tmp_path / ".devsquad" / "knowledge" / "inventory" / "stack.md"
    current_content = stack_file.read_text(encoding="utf-8")
    
    # Simulate user adding a note
    updated_content = current_content.replace(
        "<!-- manual-notes-start -->\n<!-- Add your architectural notes here. They will be preserved during the next scan. -->\n<!-- manual-notes-end -->",
        "<!-- manual-notes-start -->\nThis is a custom architectural note.\n<!-- manual-notes-end -->"
    )
    stack_file.write_text(updated_content, encoding="utf-8")
    
    # Re-generate
    generator.generate()
    
    new_content = stack_file.read_text(encoding="utf-8")
    assert "This is a custom architectural note." in new_content
    assert "Python" in new_content
