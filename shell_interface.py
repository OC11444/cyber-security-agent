import subprocess
import typer

def execute_shell_command(command: str):
    typer.echo("\n💻 Executing command...\n")
    try:
        result = subprocess.run(command, shell=True,
                                text=True, capture_output=True)
        typer.echo(result.stdout)
        if result.stderr:
            typer.secho(result.stderr, fg=typer.colors.RED)
    except Exception as e:
        typer.echo(f"❌ Error: {str(e)}")


def explain_command(command: str):
    typer.echo("\n📘 Explanation (AI-generated coming soon):")
    typer.echo(
        "For now, manually verify the command before running. Auto explanations will be added next.")


def run_final_command(command: str):
    execute_shell_command(command)
    explain_command(command)
