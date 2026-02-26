import os
import json
from pathlib import Path
from typing import List, Dict, Any, Optional

class ProjectMetadata:
    def __init__(self, path: Path, language: str):
        self.path = path
        self.language = language
        self.framework = "Unknown"
        self.version = "Unknown"
        self.structure = "Standard"
        self.meta_files = []
        self.gaps = []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": str(self.path),
            "language": self.language,
            "framework": self.framework,
            "version": self.version,
            "structure": self.structure,
            "meta_files": self.meta_files,
            "gaps": self.gaps
        }

class Detector:
    def detect(self, path: Path) -> Optional[ProjectMetadata]:
        pass

class NodeDetector(Detector):
    def detect(self, path: Path) -> Optional[ProjectMetadata]:
        pkg_json = path / "package.json"
        if not pkg_json.exists():
            return None
        
        meta = ProjectMetadata(path, "JavaScript/TypeScript")
        meta.meta_files.append("package.json")
        
        try:
            data = json.loads(pkg_json.read_text(encoding="utf-8"))
            deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
            
            if "next" in deps:
                meta.framework = "Next.js"
                meta.version = deps["next"]
                if (path / "src" / "app").exists() or (path / "app").exists():
                    meta.structure = "Next.js App Router"
                elif (path / "src" / "pages").exists() or (path / "pages").exists():
                    meta.structure = "Next.js Pages Router"
            elif "react" in deps:
                meta.framework = "React"
                meta.version = deps["react"]
        except Exception:
            pass
        return meta

class PythonDetector(Detector):
    def detect(self, path: Path) -> Optional[ProjectMetadata]:
        pyproject = path / "pyproject.toml"
        reqs = path / "requirements.txt"
        setup_py = path / "setup.py"
        
        if not (pyproject.exists() or reqs.exists() or setup_py.exists()):
            return None
            
        meta = ProjectMetadata(path, "Python")
        if pyproject.exists(): meta.meta_files.append("pyproject.toml")
        if reqs.exists(): meta.meta_files.append("requirements.txt")
        if setup_py.exists(): meta.meta_files.append("setup.py")
        
        return meta

class JavaDetector(Detector):
    def detect(self, path: Path) -> Optional[ProjectMetadata]:
        pom = path / "pom.xml"
        gradle = path / "build.gradle"
        
        if not (pom.exists() or gradle.exists()):
            return None
            
        meta = ProjectMetadata(path, "Java")
        if pom.exists(): 
            meta.meta_files.append("pom.xml")
            meta.framework = "Maven"
        if gradle.exists(): 
            meta.meta_files.append("build.gradle")
            meta.framework = "Gradle"
            
        return meta

class RepositoryScanner:
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)
        self.detectors = [NodeDetector(), PythonDetector(), JavaDetector()]
        self.ignored_dirs = {".git", "node_modules", "venv", ".venv", "target", "bin", "dist"}

    def scan(self) -> List[Dict[str, Any]]:
        projects = []
        self._recursive_scan(self.root_dir, 0, projects)
        return [p.to_dict() for p in projects]

    def _recursive_scan(self, current_dir: Path, depth: int, projects: List[ProjectMetadata]):
        if depth > 4:
            return

        # Check for projects in this directory
        for detector in self.detectors:
            meta = detector.detect(current_dir)
            if meta:
                # Check for .env security gap
                self._check_secrets(current_dir, meta)
                projects.append(meta)
                # If we found a project, we don't need to check other detectors for THIS dir
                break

        # Dive deeper
        try:
            for entry in current_dir.iterdir():
                if entry.is_dir() and entry.name not in self.ignored_dirs:
                    self._recursive_scan(entry, depth + 1, projects)
        except PermissionError:
            pass

    def _check_secrets(self, path: Path, meta: ProjectMetadata):
        env_file = path / ".env"
        gitignore = path / ".gitignore"
        
        if env_file.exists():
            is_ignored = False
            if gitignore.exists():
                content = gitignore.read_text(encoding="utf-8")
                if ".env" in content:
                    is_ignored = True
            
            if not is_ignored:
                meta.gaps.append("Unignored .env file detected")
