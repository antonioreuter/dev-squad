import sys
import json
from pathlib import Path
import questionary
from rich.console import Console

console = Console()

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

def ask_os():
    return questionary.select(
        "Step 1: Select your Operating System",
        choices=["Linux", "macOS", "Windows"]
    ).ask()

def ask_ide():
    return questionary.select(
        "Step 2: Select your target IDE",
        choices=[
            "VSCode",
            "Windsurf",
            "Cursor",
            "Antigravity",
            "Terminal / CLI"
        ]
    ).ask()

def ask_model():
    return questionary.select(
        "Step 3: Select your AI Model / Agent Extension",
        choices=[
            "IDE Native (Built-in)",
            "Claude Code",
            "GitHub Copilot",
            "RooCode (Cline)"
        ]
    ).ask()

def ask_mcp():
    return questionary.checkbox(
        "Step 4: Select MCP Servers to Enable (Space to select, Enter to confirm)",
        choices=[
            "AWS Documentation MCP Server",
            "AWS IaC MCP Server",
            "AWS Lambda MCP Server",
            "AWS Serverless MCP Server",
            "AWS Pricing MCP Server",
            "CloudWatch MCP Server",
            "CloudWatch Application Signals MCP Server",
            "AWS Well-Architected Security Assessment Tool MCP Server",
            "Amazon DynamoDB MCP Server",
            "AWS Data Processing MCP Server",
            "AWS Step Functions Tool MCP Server",
            "AWS Network MCP Server",
            "AWS CloudFormation MCP Server"
        ]
    ).ask()

def create_file_safely(target_file: Path, content: str):
    if target_file.exists():
        console.print(f"[yellow]File {target_file} already exists. Skipping to avoid overwriting your settings.[/]")
    else:
        target_file.parent.mkdir(parents=True, exist_ok=True)
        target_file.write_text(content, encoding="utf-8")
        console.print(f"[green]✓ Created {target_file}[/]")

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

def deploy_assets(sys_os, ide, model):
    # Ensure root exists
    if not Path(".devsquad").exists():
        console.print("[red bold]Error: .devsquad directory not found in the current root.[/]")
        sys.exit(1)

    if ide == "Antigravity":
        console.print("[green]✓ Native structure already active in .devsquad/[/]")
    elif ide == "Windsurf":
        console.print("[blue]Projecting lightweight pointer to .windsurfrules...[/]")
        create_file_safely(Path(".windsurfrules"), POINTER_CONTENT)
    elif ide == "Cursor":
        console.print("[blue]Projecting lightweight pointer to .cursorrules...[/]")
        create_file_safely(Path(".cursorrules"), POINTER_CONTENT)
    elif ide in ["VSCode", "Terminal / CLI"]:
        if model == "Claude Code":
            console.print("[blue]Creating .claude/ directory...[/]")
            create_file_safely(Path(".claude/devsquad.md"), POINTER_CONTENT)
        elif model == "GitHub Copilot":
            console.print("[blue]Creating .github/ directory...[/]")
            create_file_safely(Path(".github/copilot-instructions.md"), POINTER_CONTENT)
        elif model == "RooCode (Cline)":
            console.print("[blue]Projecting lightweight pointer to .clinerules...[/]")
            create_file_safely(Path(".clinerules"), POINTER_CONTENT)
        else:
            console.print("[blue]Generating AGENT_INSTRUCTIONS.md...[/]")
            create_file_safely(Path("AGENT_INSTRUCTIONS.md"), POINTER_CONTENT)

def generate_mcp_config(mcp_choices):
    if not mcp_choices:
        return
        
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
    
    for choice in mcp_choices:
        if choice in templates:
            server_id = templates[choice]["id"]
            mcp_config["mcpServers"][server_id] = templates[choice]["config"]
            
    if mcp_config["mcpServers"]:
        target_file = Path(".devsquad/mcp.json")
        console.print("[blue]Generating MCP Server configuration...[/]")
        create_file_safely(target_file, json.dumps(mcp_config, indent=2))
        console.print("[yellow]Note: You may need to link `.devsquad/mcp.json` to your IDE's specific MCP config file to activate the servers.[/]")

def main():
    try:
        print_header()
        sys_os = ask_os()
        if not sys_os: return
        
        ide = ask_ide()
        if not ide: return
        
        model = ask_model()
        if not model: return
        
        mcp = ask_mcp()
        if mcp is None: return
        
        console.print("\n[bold]Step 5: Projecting Brain Assets...[/]")
        deploy_assets(sys_os, ide, model)
        generate_mcp_config(mcp)
        
        console.print(f"\n[green bold]Success! DevSquad is now configured for {sys_os}, {ide}, and {model}.[/]")
        console.print("Type [cyan]/squad.plan \\[your idea][/] in your IDE/CLI to start the collaborative process.")
        console.print("-" * 56)
    except KeyboardInterrupt:
        console.print("\n[yellow]Installation cancelled by user.[/]")
        sys.exit(0)

if __name__ == "__main__":
    main()
