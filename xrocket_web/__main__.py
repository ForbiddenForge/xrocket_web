import logging

import click

from xrocket_web.webapp import create_webapp


@click.command()
@click.option('--port', default=5000)
def serve(port):
    app = create_webapp()
    app.run(port=port)
    










if __name__ == '__main__':
    serve()