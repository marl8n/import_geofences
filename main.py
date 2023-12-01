import json
import re
from typing import Dict, List


def run():
    pattern = re.compile(r'^(\w+\s?\(.*\)),([\w|\s\-ÁÉÍÓÚ]*),([\w|\s\-ÁÉÍÓÚ]*),.*$')
    parsed: List[Dict[str, str]] = []
    with open('./geofences_csv/Lotes -Torre de control- EX-EMILIAS.csv', 'r') as f:
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

    new_file = open('01_Lotes-Torre_de_control-EX-EMILIAS.json', 'w')
    new_file.write(json.dumps(parsed))
    new_file.close()

if __name__ == '__main__':
    run()