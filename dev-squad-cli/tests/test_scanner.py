import pytest
import os
from dev_squad.scanner import RepositoryScanner

def test_detect_nodejs_project(tmp_path):
    # Setup
    (tmp_path / "package.json").write_text('{"name": "test-node", "dependencies": {"next": "15.0.0"}}', encoding="utf-8")
    (tmp_path / "app").mkdir()
    
    scanner = RepositoryScanner(root_dir=str(tmp_path))
    metadata = scanner.scan()
    
    assert metadata["language"] == "JavaScript/TypeScript"
    assert metadata["framework"] == "Next.js"
    assert metadata["version"] == "15.0.0"
    assert metadata["structure"] == "Next.js App Router"
    assert "package.json" in metadata["meta_files"]

def test_detect_python_project(tmp_path):
    # Setup
    (tmp_path / "pyproject.toml").write_text("[project]\nname = 'test-py'", encoding="utf-8")
    
    scanner = RepositoryScanner(root_dir=str(tmp_path))
    metadata = scanner.scan()
    
    assert metadata["language"] == "Python"
    assert "pyproject.toml" in metadata["meta_files"]

def test_detect_unignored_env_gap(tmp_path):
    # Setup
    (tmp_path / ".env").write_text("SECRET=123", encoding="utf-8")
    (tmp_path / ".gitignore").write_text("node_modules/", encoding="utf-8") # .env NOT ignored
    
    scanner = RepositoryScanner(root_dir=str(tmp_path))
    metadata = scanner.scan()
    
    assert "Unignored .env file detected" in metadata["gaps"]
