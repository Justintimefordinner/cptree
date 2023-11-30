import typer
import pathlib


from __init__ import __version__

from cptree import DirectoryTree

app = typer.Typer()


@app.command()
def main(
    output: str = typer.Option("", "--file-output", "-o", help="File output"),
    version: bool = typer.Option(False, "--version", "-v", help="Show the version"),
    directory: str = typer.Argument("ROOT_DIR", help="Directory"),
):
    if version:
        typer.echo(f"CP Tree v{__version__}")
        return

    root_dir = pathlib.Path(directory)
    if not root_dir.is_dir():
        typer.echo("The specified root directory doesn't exist")
        raise typer.Exit(code=1)

    tree = DirectoryTree(root_dir, dir_only=not output, output_file=output)
    tree.generate()


if __name__ == "__main__":
    app()
