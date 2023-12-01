import json
import re
from typing import Dict, List

def parse_csv_to_json(filename: str) -> str:
    if filename.endswith('Lotes -Torre de control- EX-EMILIAS.csv'): return ""
    # first group KWT
    # second group name
    # third group description
    pattern = re.compile(r'^(".*"),([\w\d\s\.\-º\(\)#áéíóúÁÉÍÓÚñÑ]*),([\w\d\s\.\-º\(\)#áéíóúÁÉÍÓÚñÑ]*),.*$')
    parsed: List[Dict[str, str]] = []
    # ./geofences_csv/Lotes -Torre de control- EX-EMILIAS.csv
    with open(filename, 'r') as f:
        lines = f.readlines()
        print(f"Begin process: {filename}")
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