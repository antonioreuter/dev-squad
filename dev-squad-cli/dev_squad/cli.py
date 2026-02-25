import argparse
import json
import shutil
import sys
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
        source_dir = Path(__file__).parent / "assets" / ".devsquad"
        
        if source_dir.exists():
            shutil.copytree(source_dir, target_dir)
            console.print("[green]✓ DevSquad brain successfully deployed.[/]")
        else:
            console.print("[red bold]Error: internal .devsquad assets not found in the CLI package.[/]")
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
                    "STATE_MACHINE_LIST": "your-first-state-machine, your-second-state-machine",
                    "STATE_MACHINE_TAG_KEY": "your-tag-key",
                    "STATE_MACHINE_TAG_VALUE": "your-tag-value",
                    "STATE_MACHINE_INPUT_SCHEMA_ARN_TAG_KEY": "your-state-machine-tag-for-input-schema"
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

def main():
    parser = argparse.ArgumentParser(description="DevSquad Installer Wizard")
    parser.add_argument("--project", "-p", help="Destination path for installation (default: asks user)")
    parser.add_argument("--ide", help=f"Target IDE ({', '.join(IDE_CHOICES.keys())})")
    parser.add_argument("--model", help=f"AI Model / Extension ({', '.join(MODEL_CHOICES.keys())})")
    parser.add_argument("--os", help=f"Operating System ({', '.join([o.lower() for o in OS_CHOICES])})")
    args = parser.parse_args()

    try:
        print_header()
        
        # Project Destination (ask if not provided by flag)
        project_dir = ask_project(default=args.project)
        if not project_dir: return
        dest_path = Path(project_dir).resolve()
        
        if not dest_path.exists():
            console.print(f"[blue]Target path {dest_path} does not exist. Creating it...[/]")
            dest_path.mkdir(parents=True, exist_ok=True)
        
        # OS
        sys_os = ask_os(default=args.os)
        if not sys_os: return
        
        # IDE
        ide = ask_ide(default=args.ide)
        if not ide: return
        
        # Model
        model = ask_model(default=args.model)
        if not model: return
        
        print_architecture_brief()
        
        console.print(f"\n[bold]Step 5: Projecting Brain Assets to {dest_path}...[/]")
        deploy_assets(dest_path, sys_os, ide, model)
        generate_mcp_config(dest_path)
        
        console.print(f"\n[green bold]Success! DevSquad is now configured for {sys_os}, {ide}, and {model}.[/]")
        console.print(f"Path: [cyan]{dest_path}[/]")
        console.print("Type [cyan]/squad.plan \\[your idea][/] in your IDE/CLI to start the collaborative process.")
        console.print("-" * 56)
    except KeyboardInterrupt:
        console.print("\n[yellow]Installation cancelled by user.[/]")
        sys.exit(0)

if __name__ == "__main__":
    main()
