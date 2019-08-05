import requests
import base64
import json

from badge_cli.slack_badges_bot_client import config

def badge(json_file, image_file):
    try:
        openbadge_json = json.load(json_file)
        if image_file:
            image_bytes = image_file.read()
            prefix = 'data:image/{};base64,'.format(str(Image.open(image_file).format).lower())
            openbadge_json['image'] = prefix + base64.encodebytes(png).decode('utf-8')

        r=requests.post(config.API_URL, json=openbadge_json)

        return r.text
    except Exception as error:
        return error

