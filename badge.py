import click
import requests
import json
import base64

@click.group()
def cli():
    pass


@cli.command()
@click.option("--json", nargs=1, type=click.File('rb'))
@click.option("--image", nargs=1, type=click.File('rb'))
#@click.argument('json_file', type=click.File('rb'))
#@click.argument('image_file', type=click.File('rb'))
def new(json_file, image_file):
    print(json_file)
    print(image_file)
#    openbadge_json = json.load(json_file)
#    png = image_file.read()
#    try:
#        #openbadge_json['image'] = base64.b64encode(png)
#        openbadge_json['image_url'] = "pepe"
#        response=requests.post('http://vituin-chat.iaas.ull.es/api/badges/create', json=openbadge_json)
#        click.echo(response.text)
#        print(openbadge_json)
#    except Exception as error:
#        print(str(error))
#
