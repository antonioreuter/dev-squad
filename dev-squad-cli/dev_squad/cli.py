import argparse
import json
import shutil
import sys
import os
from pathlib import Path
import questionary
from rich.console import Console

console = Console()

# Defined constants for normalized flag values
IDE_CHOICES = {
    "vscode": "VSCode",
    "windsurf": "Windsurf",
    "antigravity": "Antigravity"
}

MODEL_CHOICES = {
    "ide-native": "IDE Native (Built-in)",
    "claude-code": "Claude Code",
    "github-copilot": "GitHub Copilot"
}

OS_CHOICES = ["Linux", "macOS", "Windows"]

def print_header():
    console.print("\n[magenta bold]  _____             _____                       _[/]")
    console.print("[magenta bold] |  __ \\           / ____|                     | |[/]")
    console.print("[magenta bold] | |  | | _____   | (___   __ _ _   _  __ _  __| |[/]")
    console.print("[magenta bold] | |  | |/ _ \\ \\ / \\___ \\ / _` | | | |/ _` |/ _` |[/]")
    console.print("[magenta bold] | |__| |  __/\\ V / ____) | (_| | |_| | (_| | (_| |[/]")
    console.print("[magenta bold] |_____/ \\___| \\_/ |_____/ \\__, |\\__,_|\\__,_|\\__,_|[/]")
    console.print("[magenta bold]                              | |[/]")
    console.print("[magenta bold]                              |_|  Agentic SDD Framework[/]")
    console.print("\n[cyan]Welcome to the DevSquad Installer Wizard![/]")
    console.print("-" * 56)

def ask_project(default=None):
    if default:
        return default
    return questionary.text(
        "Step 1: Enter the project destination directory",
        default="."
    ).ask()

def ask_os(default=None):
    if default:
        # Simple case-insensitive match
        for choice in OS_CHOICES:
            if choice.lower() == default.lower():
                return choice
    return questionary.select(
        "Step 2: Select your Operating System",
        choices=OS_CHOICES
    ).ask()

def ask_ide(default=None):
    if default and default.lower() in IDE_CHOICES:
        return IDE_CHOICES[default.lower()]
    return questionary.select(
        "Step 3: Select your target IDE",
        choices=list(IDE_CHOICES.values())
    ).ask()

def ask_model(default=None):
    if default and default.lower() in MODEL_CHOICES:
        return MODEL_CHOICES[default.lower()]
    return questionary.select(
        "Step 4: Select your AI Model / Agent Extension",
        choices=list(MODEL_CHOICES.values())
    ).ask()

def create_file_safely(target_file: Path, content: str):
    if target_file.exists():
        console.print(f"[yellow]File {target_file} already exists. Skipping to avoid overwriting your settings.[/]")
    else:
        target_file.parent.mkdir(parents=True, exist_ok=True)
        target_file.write_text(content, encoding="utf-8")
        console.print(f"[green]✓ Created {target_file}[/]")

def print_architecture_brief():
    console.print("\n[yellow bold]Architecture Note: Skill-Centric Tooling[/]")
    console.print("DevSquad decouples tools (MCP Servers) from Agents and assigns them to [bold]Skills[/].")
    console.print("This ensures modularity and follows the principle of least privilege.")
    console.print("-" * 56)

POINTER_CONTENT = """# DevSquad Framework Base Context

You are operating within the **DevSquad** Agentic SDD Framework. You are not a generic coding assistant; you are an autonomous virtual multi-agent team.

## 🛑 CRITICAL: Passive Mode by Default

**You MUST NOT create, modify, rename, or delete ANY file in this project unless the user has explicitly and directly asked you to do so in their current message.**

- Do NOT autonomously generate plans, summaries, or documents.
- Do NOT create files as a "helpful" side-effect of reading context.
- Do NOT take any file-system action until instructed.
- Your default posture is **read-only and responsive** — not proactive.

If you have something to suggest, **say it in the chat**. Do not write it to a file.

---

## 🤐 Communication Style: Silent Execution

**Do NOT narrate or announce what you are about to do before doing it.**

- ❌ BAD: *"I'll now run the workflow, first scanning the repo, then extracting unknowns..."*
- ✅ GOOD: *(just do it, then report the results)*

Rules:
- **No pre-execution summaries.** Do not describe your plan before acting on it.
- **No step-by-step narration.** Execute silently; only surface findings, decisions, and outputs.
- **Report results, not intentions.** When done, present the outcome clearly and concisely.
- **Ask, don't assume.** If something is unclear, ask a single, focused clarifying question. Do not proceed on assumptions.

---

To prevent context exhaustion, your rules and workflows are NOT concatenated here. Instead, your complete brain and operational guidelines are kept strictly modular in the `.devsquad/` directory at the root of this workspace.

### Your Directory Structure
- **`.devsquad/rules/`**: Contains strict, always-on constraints (e.g., architecture, coding-standards, security, devops).
- **`.devsquad/workflows/`**: Contains step-by-step orchestration scripts (e.g., `/squad.plan`, `/squad.help`, `/squad.implement`).
- **`.devsquad/skills/`**: Contains on-demand specialist roles you can adopt (e.g., lead-developer, solution-architect).

### 🚨 Core Directives
1. **Never guess the rules.** Whenever you are asked to perform a task, proactively read the relevant `.md` files in the `.devsquad/` directory using your file-reading tools.
2. **Execution:** If asked to trigger a workflow (e.g., `/squad.plan`), you MUST read that specific workflow file in `.devsquad/workflows/` and strictly follow its steps sequentially.
3. **Response Formatting:** You MUST ALWAYS conclude your responses by adhering to `.devsquad/rules/squad-participation.md`. Read it before your first reply.

Stay modular, stay strict, and protect the codebase.
"""

def deploy_assets(dest_path: Path, sys_os, ide, model):
    target_dir = dest_path / ".devsquad"
    if not target_dir.exists():
        console.print(f"[blue]Brain not found. Deploying .devsquad assets to {dest_path}...[/]")
        
        # Smart Discovery: 
        # 1. Check internal package assets (Production)
        # 2. Check repository root (Development)
        internal_src = Path(__file__).parent / "assets" / ".devsquad"
        dev_src = Path(__file__).parent.parent.parent / ".devsquad"
        
        source_dir = None
        if internal_src.exists():
            source_dir = internal_src
            console.print("[dim]  (Source: Internal Package Assets)[/]")
        elif dev_src.exists():
            source_dir = dev_src
            console.print("[dim]  (Source: Development Repository Root)[/]")
            
        if source_dir:
            shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)
            console.print("[green]✓ DevSquad brain successfully deployed.[/]")
            
            # Explicit verification for templates
            if (source_dir / "templates").exists():
                console.print("[green]✓ Documentation templates installed.[/]")
            else:
                console.print("[yellow]! Note: No documentation templates found in source brain.[/]")
        else:
            console.print("[red bold]Error: .devsquad assets not found in package or dev path.[/]")
            sys.exit(1)

    # 1. Base IDE pointer
    if ide == "Antigravity":
        console.print("[green]✓ Native structure already active in .devsquad/[/]")
    elif ide == "Windsurf":
        console.print(f"[blue]Projecting lightweight pointer to {dest_path}/.windsurfrules...[/]")
        create_file_safely(dest_path / ".windsurfrules", POINTER_CONTENT)
        
        # Project workflows to .windsurf/workflows/ for native slash command visibility
        windsurf_workflow_dir = dest_path / ".windsurf" / "workflows"
        source_workflow_dir = target_dir / "workflows"
        
        if source_workflow_dir.exists():
            console.print(f"[blue]Projecting native Windsurf Workflows to {windsurf_workflow_dir}...[/]")
            if not windsurf_workflow_dir.exists():
                windsurf_workflow_dir.mkdir(parents=True, exist_ok=True)
            
            for workflow_file in source_workflow_dir.glob("*.md"):
                shutil.copy2(workflow_file, windsurf_workflow_dir / workflow_file.name)
            console.print("[green]✓ Slash commands are now natively visible in Windsurf.[/]")
    elif ide == "VSCode":
        if model not in ["Claude Code", "GitHub Copilot"]:
            console.print(f"[blue]Generating {dest_path}/AGENT_INSTRUCTIONS.md...[/]")
            create_file_safely(dest_path / "AGENT_INSTRUCTIONS.md", POINTER_CONTENT)

    # 2. Add Model Extension Tooling
    if model == "Claude Code":
        console.print(f"[blue]Creating {dest_path}/CLAUDE.md for Claude Code...[/]")
        create_file_safely(dest_path / "CLAUDE.md", POINTER_CONTENT)
        
        # Project workflows to .claude/commands/ for Claude Code slash commands
        claude_commands_dir = dest_path / ".claude" / "commands"
        source_workflow_dir = target_dir / "workflows"
        if source_workflow_dir.exists():
            console.print(f"[blue]Projecting native Claude Code Commands to {claude_commands_dir}...[/]")
            claude_commands_dir.mkdir(parents=True, exist_ok=True)
            
            for workflow_file in source_workflow_dir.glob("*.md"):
                shutil.copy2(workflow_file, claude_commands_dir / workflow_file.name)
            console.print("[green]✓ Slash commands are now natively visible in Claude Code.[/]")
            
    elif model == "GitHub Copilot":
        console.print(f"[blue]Creating {dest_path}/.github/copilot-instructions.md...[/]")
        create_file_safely(dest_path / ".github/copilot-instructions.md", POINTER_CONTENT)
        
        # Project workflows to .github/prompts/ for VS Code Copilot Chat
        github_prompts_dir = dest_path / ".github" / "prompts"
        source_workflow_dir = target_dir / "workflows"
        if source_workflow_dir.exists():
            console.print(f"[blue]Projecting native VS Code Copilot Prompts to {github_prompts_dir}...[/]")
            github_prompts_dir.mkdir(parents=True, exist_ok=True)
            
            prompt_recommendations = {}
            for workflow_file in source_workflow_dir.glob("*.md"):
                shutil.copy2(workflow_file, github_prompts_dir / workflow_file.name)
                # VS Code Copilot refers to these by filename or stem
                prompt_recommendations[workflow_file.name] = True
                prompt_recommendations[workflow_file.stem] = True
            
            # Safely update .vscode/settings.json
            vscode_dir = dest_path / ".vscode"
            vscode_dir.mkdir(parents=True, exist_ok=True)
            settings_file = vscode_dir / "settings.json"
            settings = {}
            if settings_file.exists():
                try:
                    settings = json.loads(settings_file.read_text(encoding="utf-8"))
                except json.JSONDecodeError:
                    pass
            
            if "chat.promptFilesRecommendations" not in settings:
                settings["chat.promptFilesRecommendations"] = {}
            settings["chat.promptFilesRecommendations"].update(prompt_recommendations)
            
            settings_file.write_text(json.dumps(settings, indent=2), encoding="utf-8")
            console.print("[green]✓ Slash commands are now natively visible in VS Code Copilot Chat.[/]")

def generate_mcp_config(dest_path: Path):
    mcp_config = {"mcpServers": {}}
    templates = {
        "AWS Documentation MCP Server": {
            "id": "awslabs.aws-documentation-mcp-server",
            "config": {
                "command": "uvx",
                "args": ["awslabs.aws-documentation-mcp-server@latest"],
                "env": {
                    "FASTMCP_LOG_LEVEL": "ERROR",
                    "AWS_DOCUMENTATION_PARTITION": "aws",
                    "MCP_USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
                },
                "disabled": False,
                "autoApprove": []
            }
        },
        "AWS IaC MCP Server": {
            "id": "awslabs.aws-iac-mcp-server",
            "config": {
                "command": "uvx",
                "args": ["awslabs.aws-iac-mcp-server@latest"],
                "env": {
                    "AWS_PROFILE": "your-aws-profile",
                    "FASTMCP_LOG_LEVEL": "ERROR"
                },
                "disabled": False,
                "autoApprove": []
            }
        },
        "AWS Lambda MCP Server": {
            "id": "awslabs.lambda-tool-mcp-server",
            "config": {
                "command": "uvx",
                "args": ["awslabs.lambda-tool-mcp-server@latest"],
                "env": {
                    "AWS_PROFILE": "your-aws-profile",
                    "AWS_REGION": "us-east-1",
                    "FUNCTION_PREFIX": "your-function-prefix",
                    "FUNCTION_LIST": "your-first-function, your-second-function",
                    "FUNCTION_TAG_KEY": "your-tag-key",
                    "FUNCTION_TAG_VALUE": "your-tag-value",
                    "FUNCTION_INPUT_SCHEMA_ARN_TAG_KEY": "your-function-tag-for-input-schema"
                }
            }
        },
        "AWS Serverless MCP Server": {
            "id": "awslabs.aws-serverless-mcp-server",
            "config": {
                "command": "uvx",
                "args": [
                    "awslabs.aws-serverless-mcp-server@latest",
                    "--allow-write",
                    "--allow-sensitive-data-access"
                ],
                "env": {
                    "AWS_PROFILE": "your-aws-profile",
                    "AWS_REGION": "us-east-1"
                },
                "disabled": False,
                "autoApprove": []
            }
        },
        "AWS Pricing MCP Server": {
            "id": "awslabs.aws-pricing-mcp-server",
            "config": {
                "command": "uvx",
                "args": ["awslabs.aws-pricing-mcp-server@latest"],
                "env": {
                    "FASTMCP_LOG_LEVEL": "ERROR",
                    "AWS_PROFILE": "your-aws-profile",
                    "AWS_REGION": "us-east-1"
                },
                "disabled": False,
                "autoApprove": []
            }
        },
        "CloudWatch MCP Server": {
            "id": "awslabs.cloudwatch-mcp-server",
            "config": {
                "command": "uvx",
                "args": ["awslabs.cloudwatch-mcp-server@latest"],
                "env": {
                    "AWS_PROFILE": "your-aws-profile",
                    "FASTMCP_LOG_LEVEL": "ERROR"
                },
                "transportType": "stdio",
                "disabled": False,
                "autoApprove": []
            }
        },
        "CloudWatch Application Signals MCP Server": {
            "id": "awslabs.cloudwatch-applicationsignals-mcp-server",
            "config": {
                "command": "uvx",
                "args": ["awslabs.cloudwatch-applicationsignals-mcp-server@latest"],
                "env": {
                    "AWS_PROFILE": "your-aws-profile",
                    "AWS_REGION": "us-east-1",
                    "FASTMCP_LOG_LEVEL": "ERROR"
                }
            }
        },
        "AWS Well-Architected Security Assessment Tool MCP Server": {
            "id": "awslabs.well-architected-security-mcp-server",
            "config": {
                "command": "uvx",
                "args": ["awslabs.well-architected-security-mcp-server@latest"],
                "env": {
                    "AWS_PROFILE": "your-aws-profile",
                    "AWS_REGION": "us-east-1",
                    "FASTMCP_LOG_LEVEL": "ERROR"
                }
            }
        },
        "Amazon DynamoDB MCP Server": {
            "id": "awslabs.dynamodb-mcp-server",
            "config": {
                "command": "uvx",
                "args": ["awslabs.dynamodb-mcp-server@latest"],
                "env": {
                    "FASTMCP_LOG_LEVEL": "ERROR"
                },
                "disabled": False,
                "autoApprove": []
            }
        },
        "AWS Data Processing MCP Server": {
            "id": "awslabs.aws-dataprocessing-mcp-server",
            "config": {
                "command": "uvx",
                "args": [
                    "awslabs.aws-dataprocessing-mcp-server@latest",
                    "--allow-write"
                ],
                "env": {
                    "FASTMCP_LOG_LEVEL": "ERROR",
                    "AWS_REGION": "us-east-1"
                }
            }
        },
        "AWS Step Functions Tool MCP Server": {
            "id": "awslabs.stepfunctions-tool-mcp-server",
            "config": {
                "command": "uvx",
                "args": ["awslabs.stepfunctions-tool-mcp-server@latest"],
                "env": {
                    "AWS_PROFILE": "your-aws-profile",
                    "AWS_REGION": "us-east-1",
                    "STATE_MACHINE_PREFIX": "your-state-machine-prefix",
                    "STATE_MACHINE_LIST": "your-first-function, your-second-function",
                    "STATE_MACHINE_TAG_KEY": "your-tag-key",
                    "STATE_MACHINE_TAG_VALUE": "your-tag-value",
                    "STATE_MACHINE_INPUT_SCHEMA_ARN_TAG_KEY": "your-function-tag-for-input-schema"
                }
            }
        },
        "AWS Network MCP Server": {
            "id": "awslabs.aws-network-mcp-server",
            "config": {
                "command": "uvx",
                "args": ["awslabs.aws-network-mcp-server@latest"],
                "env": {
                    "AWS_PROFILE": "your-aws-profile",
                    "AWS_REGION": "us-east-1"
                },
                "disabled": False,
                "autoApprove": []
            }
        },
        "AWS CloudFormation MCP Server": {
            "id": "awslabs.cfn-mcp-server",
            "config": {
                "command": "uvx",
                "args": ["awslabs.cfn-mcp-server@latest"],
                "env": {
                    "AWS_PROFILE": "your-aws-profile"
                },
                "disabled": False,
                "autoApprove": []
            }
        }
    }
    
    # Enable ALL servers by default
    for choice in templates:
        server_id = templates[choice]["id"]
        mcp_config["mcpServers"][server_id] = templates[choice]["config"]
            
    if mcp_config["mcpServers"]:
        target_file = dest_path / ".devsquad" / "mcp.json"
        console.print("[blue]Generating MCP Server configuration (Enabling all 13 servers)...[/]")
        create_file_safely(target_file, json.dumps(mcp_config, indent=2))
        console.print("[yellow]Note: You may need to link `.devsquad/mcp.json` to your IDE's specific MCP config file to activate the servers.[/]")

def manage_squad(dest_path: Path):
    target_dir = dest_path / ".devsquad"
    fired_dir = target_dir / "fired"
    addons_dir = target_dir / "_addons"
    
    action = questionary.select(
        "HR Manager: What is your objective?",
        choices=["Hire Specialist", "Fire Specialist", "Back"]
    ).ask()
    
    if action == "Back": return
    
    if action == "Fire Specialist":
        rules_dir = target_dir / "rules"
        active_specialists = [f.stem for f in rules_dir.glob("*.md")]
        if not active_specialists:
            console.print("[yellow]No active specialists found to fire.[/]")
            return
            
        target = questionary.select("Select employee to fire:", choices=active_specialists).ask()
        if target:
            # Move to fired
            emp_fired_dir = fired_dir / target
            emp_fired_dir.mkdir(parents=True, exist_ok=True)
            
            # Simple move for now (logic-only demo)
            for ftype in ["rules", "skills", "workflows"]:
                src_ftype = target_dir / ftype
                for asset in src_ftype.glob(f"{target}*.md"):
                    shutil.move(str(asset), str(emp_fired_dir / asset.name))
            
            console.print(f"[red]✓ {target} has been dismissed and moved to {fired_dir}[/]")
            
            # Update Registry
            settings_file = target_dir / "devsquad-settings.json"
            if settings_file.exists():
                try:
                    settings = json.loads(settings_file.read_text(encoding="utf-8"))
                    squad = settings.get("squad", {})
                    active = squad.get("active_agents", {})
                    
                    if target in active:
                        # 1. Remove from active agents
                        del active[target]
                        
                        # 2. Social Cleanup: Remove from others' collaborate lists
                        for other_name, other_data in active.items():
                            if "collaborates" in other_data and target in other_data["collaborates"]:
                                other_data["collaborates"].remove(target)
                                console.print(f"[yellow]  - Removed {target} from {other_name}'s collaboration path.[/]")
                        
                        settings_file.write_text(json.dumps(settings, indent=2), encoding="utf-8")
                        console.print(f"[green]✓ Removed and cleaned up {target} in devsquad-settings.json registry.[/]")
                    else:
                        console.print(f"[yellow]! Agent {target} not found in registry.[/]")
                except Exception as e:
                    console.print(f"[red]! Error updating registry: {e}[/]")
            
            console.print("[yellow]Note: Remember to update project.md to reflect this change.[/]")

    elif action == "Hire Specialist":
        choices = []
        # Priority 1: Fired
        if fired_dir.exists():
            choices.extend([f"Re-hire (Customized): {d.name}" for d in fired_dir.iterdir() if d.is_dir()])
        
        # Priority 2: Add-ons
        if addons_dir.exists():
            choices.extend([f"Hire Add-on (Template): {d.name}" for d in addons_dir.iterdir() if d.is_dir()])
            
        if not choices:
            console.print("[yellow]No candidates found in Pool or History.[/]")
            return
            
        selection = questionary.select("Select candidate to hire:", choices=choices).ask()
        if selection:
            is_rehire = selection.startswith("Re-hire")
            name = selection.split(": ")[1]
            src = fired_dir / name if is_rehire else addons_dir / name
            
            # Copy back
            for ftype in ["rules", "skills", "workflows"]:
                asset_src = src / ftype
                if asset_src.exists():
                    asset_dest = target_dir / ftype
                    asset_dest.mkdir(parents=True, exist_ok=True)
                    for asset in asset_src.glob("*.md"):
                        dest_file = asset_dest / asset.name
                        if dest_file.exists():
                            console.print(f"[yellow]  ! Skipping {asset.name} (Existing version preserved)[/]")
                        else:
                            shutil.copy2(asset, dest_file)
                            console.print(f"[green]  ✓ Onboarded {asset.name}[/]")
            
            status = "re-activated" if is_rehire else "onboarded"
            console.print(f"[green]✓ {name} has been {status} successfully![/]")
            
            # Update Registry
            settings_file = target_dir / "devsquad-settings.json"
            if settings_file.exists():
                try:
                    settings = json.loads(settings_file.read_text(encoding="utf-8"))
                    squad = settings.setdefault("squad", {})
                    active = squad.setdefault("active_agents", {})
                    pool = squad.get("talent_pool", {})
                    
                    # 1. Onboard new agent
                    agent_data = pool.get(name, {
                        "responsibility": "Specialized mission within the squad"
                    })
                    
                    active[name] = {
                        "status": "active",
                        "responsibility": agent_data.get("responsibility"),
                        "collaborates": agent_data.get("potential_peers", ["solution-architect", "project-manager"])
                    }
                    
                    # 2. Social Sync: Update existing peers
                    potential_peers = agent_data.get("potential_peers", [])
                    for peer in potential_peers:
                        if peer in active:
                            if "collaborates" not in active[peer]:
                                active[peer]["collaborates"] = []
                            if name not in active[peer]["collaborates"]:
                                active[peer]["collaborates"].append(name)
                                console.print(f"[green]  ✓ Linked {name} to {peer}'s collaboration path.[/]")
                    
                    # 3. Save
                    settings_file.write_text(json.dumps(settings, indent=2), encoding="utf-8")
                    console.print("[green]✓ Registered and synced in devsquad-settings.json.[/]")
                except Exception as e:
                    console.print(f"[red]! Error updating registry: {e}[/]")
            
            console.print("[yellow]Note: Remember to update project.md to reflect this change.[/]")

def ask_kb(project_path: Path, default=None):
    if default:
        return default
    
    confirm = questionary.confirm(
        "Step 5: Would you like to configure a Project Knowledge Base?",
        default=True
    ).ask()
    
    if not confirm:
        return None
        
    kb_path = questionary.text(
        "Enter the path to your Knowledge Base folder (relative to project root)",
        default="docs/kb"
    ).ask()
    
    if kb_path:
        full_path = project_path / kb_path
        if not full_path.exists():
            create = questionary.confirm(
                f"Directory {kb_path} does not exist. Create it?",
                default=True
            ).ask()
            if create:
                full_path.mkdir(parents=True, exist_ok=True)
                # Create default index
                index_file = full_path / "knowledge-base.md"
                if not index_file.exists():
                    index_file.write_text("# Project Knowledge Base\n\nWelcome to the knowledge base. List your modules here.", encoding="utf-8")
        return kb_path
    return None

def cmd_scan(project_path: Path):
    from dev_squad.scanner import RepositoryScanner
    from dev_squad.inventory_generator import InventoryGenerator
    
    console.print(f"\n[bold blue]🔍 Scanning repository at {project_path}...[/]")
    
    scanner = RepositoryScanner(root_dir=str(project_path))
    projects = scanner.scan()
    
    for metadata in projects:
        rel_path = Path(metadata['path']).relative_to(project_path)
        display_path = "." if str(rel_path) == "." else str(rel_path)
        console.print(f"[green]✓ Found {metadata['language']} project at `{display_path}` ({metadata['framework']} {metadata['version']})[/]")
        if metadata["gaps"]:
            console.print(f"  [yellow]! Found {len(metadata['gaps'])} architectural gaps.[/]")
        
    generator = InventoryGenerator(project_root=str(project_path), projects_metadata=projects)
    generator.generate()
    
    console.print(f"[bold green]✓ Project Inventory updated in .devsquad/knowledge/inventory/[/]\n")

def main():
    parser = argparse.ArgumentParser(description="DevSquad Installer Wizard")
    parser.add_argument("command", nargs="?", choices=["install", "scan"], default="install", help="Command to run")
    parser.add_argument("--project", "-p", help="Destination path for installation (default: asks user)")
    parser.add_argument("--ide", help=f"Target IDE ({', '.join(IDE_CHOICES.keys())})")
    parser.add_argument("--model", help=f"AI Model / Extension ({', '.join(MODEL_CHOICES.keys())})")
    parser.add_argument("--os", help=f"Operating System ({', '.join([o.lower() for o in OS_CHOICES])})")
    parser.add_argument("--kb", help="Path to Knowledge Base directory")
    args = parser.parse_args()

    # Handle direct scan command
    if args.command == "scan":
        project_dir = args.project or os.getcwd()
        dest_path = Path(project_dir).resolve()
        cmd_scan(dest_path)
        return

    try:
        print_header()
        
        # Project Destination (ask if not provided by flag)
        project_dir = ask_project(default=args.project)
        if not project_dir: return
        dest_path = Path(project_dir).resolve()
        
        if not dest_path.exists():
            console.print(f"[blue]Target path {dest_path} does not exist. Creating it...[/]")
            dest_path.mkdir(parents=True, exist_ok=True)
        
        if dest_path.exists() and (dest_path / ".devsquad").exists():
            # If already installed, offer Management Menu
            action = questionary.select(
                "Project detected. What would you like to do?",
                choices=[
                    "Scan Repository & Update Inventory",
                    "Manage Squad (Hire/Fire Specialists)", 
                    "Refresh/Reinstall Base Assets", 
                    "Exit"
                ]
            ).ask()
            
            if action == "Exit": return
            if action == "Scan Repository & Update Inventory":
                cmd_scan(dest_path)
                return
            if action == "Manage Squad (Hire/Fire Specialists)":
                manage_squad(dest_path)
                return
            # If "Refresh/Reinstall", continue to normal flow
        
        # OS
        sys_os = ask_os(default=args.os)
        if not sys_os: return
        
        # IDE
        ide = ask_ide(default=args.ide)
        if not ide: return
        
        # Model
        model = ask_model(default=args.model)
        if not model: return

        # Knowledge Base
        kb_path = ask_kb(dest_path, default=args.kb)
        
        print_architecture_brief()
        
        console.print(f"\\n[bold]Step 6: Projecting Brain Assets to {dest_path}...[/]")
        deploy_assets(dest_path, sys_os, ide, model)
        generate_mcp_config(dest_path)

        # Update Settings with KB info
        settings_file = dest_path / ".devsquad" / "devsquad-settings.json"
        if settings_file.exists():
            try:
                settings = json.loads(settings_file.read_text(encoding="utf-8"))
                infra = settings.setdefault("infrastructure", {})
                infra["knowledge_base"] = kb_path
                settings_file.write_text(json.dumps(settings, indent=2), encoding="utf-8")
                console.print(f"[green]✓ Knowledge Base path '{kb_path}' registered in settings.[/]")
            except Exception as e:
                console.print(f"[red]! Warning: Could not update settings with KB path: {e}[/]")
        
        console.print(f"\\n[green bold]Success! DevSquad is now configured for {sys_os}, {ide}, and {model}.[/]")
        console.print(f"Path: [cyan]{dest_path}[/]")
        console.print("Type [cyan]/squad.plan \\[your idea][/] in your IDE/CLI to start the collaborative process.")
        console.print("-" * 56)
    except KeyboardInterrupt:
        console.print("\\n[yellow]Installation cancelled by user.[/]")
        sys.exit(0)

if __name__ == "__main__":
    main()
