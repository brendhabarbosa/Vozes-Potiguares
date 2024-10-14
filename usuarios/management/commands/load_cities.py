import json
from typing import Any
from django.core.management.base import BaseCommand
from usuarios.models import Cidade

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('./usuarios/static/data/cidades_rn.json', 'r', encoding='utf-8') as f:
            raw_json = f.read()

            data = json.loads(raw_json)

            for cidade in data:
                Cidade.objects.create(nome=cidade['municipio'])