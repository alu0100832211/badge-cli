import click
import requests
import json
import base64

@click.group()
def cli():
    pass


@cli.command()
@click.argument('json_file', type=click.File('rb'))
@click.argument('image_file', type=click.File('rb'))
def new(json_file, image_file):
    openbadge_json = json.load(json_file)
    png = image_file.read()
    try:
        openbadge_json['image'] = base64.b64encode(png)
        response=requests.post('http://vituin-chat.iaas.ull.es/api/newbadge', json=openbadge_json)
        click.echo(response.text)
    except Exception as error:
        print(str(error))

