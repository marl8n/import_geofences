import json
import re
from typing import Dict, List

def parse_csv_to_json(filename: str) -> str:
    parsed: List[Dict[str, str]] = []
    pattern = None

    if not filename.endswith('Lotes -Torre de control- EX-EMILIAS.csv'):
        # first group KWT
        # second group name
        # third group description
        # with ""
        pattern = re.compile(r'^(".*"),([\w\d\s\.\-º\(\)#áéíóúÁÉÍÓÚñÑ]*),([\w\d\s\.\-º\(\)#áéíóúÁÉÍÓÚñÑ]*),.*$')
    else:
        # without ""
        pattern = re.compile(r'^([A-Z]+\s\({1,2}.*\){1,2}),([\w\d\s\.\-º\(\)#áéíóúÁÉÍÓÚñÑ]*),.*$')

    if not pattern: return ""

    # ./geofences_csv/Lotes -Torre de control- EX-EMILIAS.csv
    with open(filename, 'r', encoding='utf-8-sig' ) as f:
        lines = f.readlines()
        print(f"Begin process: {filename}")
        idx = 0
        for line in lines:
            result = re.match(pattern, line.strip())

            if not result: continue

            wkt = result.group(1).replace('"', '')
            name = result.group(2)

            idx += 1

            parsed.append({
                "rowId": idx,
                "wkt": wkt,
                "name": name,
            })

        print("End process")
        return json.dumps(parsed)