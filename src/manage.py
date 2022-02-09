import datetime
import typer
import uvicorn

app = typer.Typer()


@app.command()
def runserver(host: str = 'localhost', port: int = 8080):
    """Runs server at host `host` and port `port`.

    Args:
        host (str, optional): Host where to run server. Defaults to 'localhost'.
        port (int, optional): Port where to run server. Defaults to 8080.
    """

    typer.secho(f'[{datetime.datetime.now()}]\tStarting server...', fg=typer.colors.YELLOW)
    uvicorn.run('main:app', host=host, port=port)
    typer.secho(f'[{datetime.datetime.now()}]\tServer finished its work.', fg=typer.colors.YELLOW)


if __name__ == '__main__':
    app()
