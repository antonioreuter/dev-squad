import shutil
import subprocess
import tempfile
from pathlib import Path
import json

def run_cli(args, cwd):
    cli_path = cwd / "dev_squad" / "cli.py"
    cmd = ["uv", "run", "python", str(cli_path)] + args
    return subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)

def test_installation_windsurf_ide_native():
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        cwd = Path(__file__).parent.parent
        
        args = [
            "--project", str(tmp_path),
            "--ide", "windsurf",
            "--model", "ide-native",
            "--os", "linux",
            "--kb", "docs/kb"
        ]
        
        result = run_cli(args, cwd)
        assert result.returncode == 0, f"Installation failed: {result.stderr}"
        
        # Verify assets
        assert (tmp_path / ".devsquad").is_dir()
        assert (tmp_path / ".windsurfrules").is_file()
        
        mcp_file = tmp_path / ".devsquad" / "mcp.json"
        with open(mcp_file, "r") as f:
            data = json.load(f)
            assert len(data["mcpServers"]) == 13

def test_installation_vscode_claude_code():
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        cwd = Path(__file__).parent.parent
        
        args = [
            "--project", str(tmp_path),
            "--ide", "vscode",
            "--model", "claude-code",
            "--os", "macos",
            "--kb", "docs/kb"
        ]
        
        result = run_cli(args, cwd)
        assert result.returncode == 0, f"Installation failed: {result.stderr}"
        
        # Verify assets
        assert (tmp_path / ".devsquad").is_dir()
        assert (tmp_path / "CLAUDE.md").is_file()
        assert (tmp_path / ".claude" / "commands").is_dir()
        
        # Verify MCP
        assert (tmp_path / ".devsquad" / "mcp.json").is_file()

def test_no_overwrite():
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        cwd = Path(__file__).parent.parent
        
        # Pre-create a file
        existing_pointer = tmp_path / ".windsurfrules"
        existing_pointer.write_text("don't touch me")
        
        args = [
            "--project", str(tmp_path),
            "--ide", "windsurf",
            "--model", "ide-native",
            "--os", "linux",
            "--kb", "docs/kb"
        ]
        
        result = run_cli(args, cwd)
        assert result.returncode == 0
        
        # Verify it didn't overwrite
        assert existing_pointer.read_text() == "don't touch me"
        assert "already exists. Skipping" in result.stdout

if __name__ == "__main__":
    print("Running: test_installation_windsurf_ide_native...")
    test_installation_windsurf_ide_native()
    print("Passed!")
    
    print("Running: test_installation_vscode_claude_code...")
    test_installation_vscode_claude_code()
    print("Passed!")
    
    print("Running: test_no_overwrite...")
    test_no_overwrite()
    print("Passed!")
    
    print("\nAll tests passed successfully!")
