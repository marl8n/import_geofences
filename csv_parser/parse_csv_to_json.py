import json
import re
from typing import Dict, List
from os.path import is_file

def validate(filename: str):
    if not is_file(filename): raise NameError(f'{filename}: is not a valid file')

def parse(filename: str) -> str:
    validate(filename)

    pattern = re.compile(r'^(\w+\s?\(.*\)),([\w|\s\-ÁÉÍÓÚ]*),([\w|\s\-ÁÉÍÓÚ]*),.*$')
    parsed: List[Dict[str, str]] = []
    # ./geofences_csv/Lotes -Torre de control- EX-EMILIAS.csv
    with open(filename, 'r') as f:
        lines = f.readlines()
        print("Begin process")
        for line in lines:
            result = re.match(pattern, line.strip())

            if not result: continue

            wkt = result.group(1)
            name = result.group(2)
            description = result.group(3)

            parsed.append({
                "wkt": wkt,
                "name": name,
                "description": description
            })

        print("End process")
        return json.dumps(parsed)