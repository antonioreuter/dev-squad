import pytest
import os
from pathlib import Path
from dev_squad.scanner import RepositoryScanner

def test_recursive_multi_language_scan(tmp_path):
    # Setup Mono-repo
    # 1. Java sub-project
    java_dir = tmp_path / "java-service"
    java_dir.mkdir()
    (java_dir / "pom.xml").write_text("<project></project>")
    
    # 2. Python sub-project
    py_dir = tmp_path / "py-lib"
    py_dir.mkdir()
    (py_dir / "pyproject.toml").write_text("[tool.poetry]")
    
    # 3. Node/Next.js sub-project
    web_dir = tmp_path / "web-app"
    web_dir.mkdir()
    (web_dir / "package.json").write_text('{"dependencies": {"next": "15.0.0"}}')
    (web_dir / "app").mkdir() # App Router
    
    scanner = RepositoryScanner(root_dir=str(tmp_path))
    results = scanner.scan()
    
    assert len(results) == 3
    
    langs = [r['language'] for r in results]
    assert "Java" in langs
    assert "Python" in langs
    assert "JavaScript/TypeScript" in langs
    
    # Check Next.js specific details
    web_res = next(r for r in results if r['language'] == "JavaScript/TypeScript")
    assert web_res['framework'] == "Next.js"
    assert web_res['structure'] == "Next.js App Router"

def test_security_gap_in_subproject(tmp_path):
    sub_dir = tmp_path / "service-a"
    sub_dir.mkdir()
    (sub_dir / "pyproject.toml").write_text("")
    (sub_dir / ".env").write_text("SECRET=123")
    # No .gitignore
    
    scanner = RepositoryScanner(root_dir=str(tmp_path))
    results = scanner.scan()
    
    assert "Unignored .env file detected" in results[0]['gaps']
