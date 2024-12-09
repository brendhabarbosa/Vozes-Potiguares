import json
from typing import Any
from django.core.management.base import BaseCommand
from usuarios.models import Cidade

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('./usuarios/static/data/cidades_rn.json', 'r', encoding='utf-8') as f:
            raw_json = f.read()

            data = json.loads(raw_json)

            BRASAO_PADRAO = '/static/IMG/image 1.png'

            for cidade in data:
                brasao_path = cidade.get('brasao', BRASAO_PADRAO)

                Cidade.objects.create(nome=cidade['municipio'], brasao=brasao_path)