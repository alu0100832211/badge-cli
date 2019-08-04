import click
import requests
import json
import base64
from PIL import Image

@click.group()
def cli():
    pass


@cli.command()
@click.argument('json_file', type=click.File('rb'))
@click.argument('image_file', type=click.File('rb'))
def create(json_file, image_file):
    openbadge_json = json.load(json_file)
    png = image_file.read()
    try:
        #https://tools.ietf.org/html/rfc2397
        prefix = 'data:image/{};base64,'.format(str(Image.open(image_file).format).lower())
        openbadge_json['image'] = prefix + base64.encodebytes(png).decode('utf-8')
        print(openbadge_json['image'])
        #openbadge_json['image'] = 'http://pepeppepepe.png'
        response=requests.post('http://vituin-chat.iaas.ull.es/api/badges/create', json=openbadge_json)
        click.echo(response.text)
    except Exception as error:
        print(str(error))
