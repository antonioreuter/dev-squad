from pathlib import Path

class InventoryGenerator:
    def __init__(self, project_root: str, projects_metadata: list):
        self.project_root = Path(project_root)
        self.kb_root = self.project_root / ".devsquad" / "knowledge"
        self.inventory_dir = self.kb_root / "inventory"
        self.projects_metadata = projects_metadata

    def generate(self):
        self._ensure_kb_structure()
        self._write_stack_module()
        self._write_structure_module()
        self._write_gaps_module()

    def _ensure_kb_structure(self):
        self.inventory_dir.mkdir(parents=True, exist_ok=True)

    def _write_module(self, filename: str, title: str, meta: str, body: str):
        path = self.inventory_dir / filename
        manual_notes = ""
        
        if path.exists():
            content = path.read_text(encoding="utf-8")
            import re
            match = re.search(r"<!-- manual-notes-start -->(.*)<!-- manual-notes-end -->", content, re.DOTALL)
            if match:
                manual_notes = match.group(1).strip()

        notes_section = f"\n\n<!-- manual-notes-start -->\n{manual_notes}\n<!-- manual-notes-end -->" if manual_notes else "\n\n<!-- manual-notes-start -->\n<!-- Add your architectural notes here. They will be preserved during the next scan. -->\n<!-- manual-notes-end -->"

        full_content = f"# {title}\n\n{meta}\n\n{body}{notes_section}\n"
        path.write_text(full_content, encoding="utf-8")

    def _write_stack_module(self):
        meta = "<!-- load-on: tech-research, dependencies-update -->"
        body = ""
        for p in self.projects_metadata:
            rel_path = Path(p['path']).relative_to(self.project_root)
            display_path = "." if str(rel_path) == "." else str(rel_path)
            body += f"### Project: `{display_path}`\n"
            body += f"- **Language**: {p.get('language')}\n"
            body += f"- **Framework**: {p.get('framework')}\n"
            body += f"- **Version**: {p.get('version')}\n"
            body += f"- **Meta Files**: {', '.join(p.get('meta_files', []))}\n\n"
        
        self._write_module("stack.md", "Tech Stack Inventory", meta, body.strip())

    def _write_structure_module(self):
        meta = "<!-- load-on: routing-task, architectural-onboarding -->"
        body = ""
        for p in self.projects_metadata:
            rel_path = Path(p['path']).relative_to(self.project_root)
            display_path = "." if str(rel_path) == "." else str(rel_path)
            body += f"### Project: `{display_path}`\n"
            body += f"- **Paradigm**: {p.get('structure')}\n\n"
            
        self._write_module("structure.md", "Project Structure", meta, body.strip())

    def _write_gaps_module(self):
        meta = "<!-- load-on: security-audit, health-check -->"
        body = ""
        any_gaps = False
        for p in self.projects_metadata:
            gaps = p.get('gaps', [])
            if gaps:
                any_gaps = True
                rel_path = Path(p['path']).relative_to(self.project_root)
                display_path = "." if str(rel_path) == "." else str(rel_path)
                body += f"### Project: `{display_path}`\n"
                body += "\n".join([f"- [ ] {gap}" for gap in gaps]) + "\n\n"
        
        if not any_gaps:
            body = "No critical gaps detected."
            
        self._write_module("gaps.md", "Architectural Gaps & Debt", meta, body.strip())
