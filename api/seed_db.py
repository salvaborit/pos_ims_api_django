#!/usr/bin/python3

import requests
import json
import os
import django
from models import Terminal, Client, Model
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_react_api.settings')
django.setup()

with open('terminales.json', 'r') as fp:
    terminal_list = json.load(fp)

for terminal in terminal_list:
    # Get the client and model instances
    client = Client.objects.get(id=terminal['client'])
    model = Model.objects.get(id=terminal['model'])
    # Create a new Terminal object
    new_terminal = Terminal(serial_number=terminal['serial_number'],
                            part_number=terminal['part_number'],
                            id_pos2000=terminal['id_pos2000'],
                            client=client,
                            model=model)
    # Serialize the object to json
    data = json.dumps(new_terminal.__dict__)
    # Make a post request to the api endpoint
    resp = requests.post('http://localhost:8000/api/terminals/', json=data)
    print(resp.status_code)
    print(resp.json())
