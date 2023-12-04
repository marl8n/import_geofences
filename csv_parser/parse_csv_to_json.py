import json
import re
from typing import Dict, List

from geofences_utils.parsers import parse_wkt_to_csv

def parse_csv_to_json(filename: str) -> str:
    parsed: List[Dict[str, str]] = []
    pattern = re.compile(r'^(".*"),([\w\d\s\.\-º\(\)#áéíóúÁÉÍÓÚñÑ]*),([\w\d\s\.\-º\(\)#áéíóúÁÉÍÓÚñÑ]*),.*$')

    with open(filename, 'r', encoding='utf-8-sig' ) as f:
        lines = f.readlines()
        print(f"Begin process: {filename}")
        idx = 0
        for line in lines:
            result = re.match(pattern, line.strip())

            if not result: continue

            wkt = result.group(1).replace('"', '')
            name = result.group(2)

            vertex_csv = parse_wkt_to_csv(wkt)

            if result.group(3):
                name = f'{name} - {result.group(3)}'

            idx += 1

            parsed.append({
                "rowId": idx,
                "wkt": wkt,
                "name": name,
                "vertexCsv": vertex_csv,
            })

        print("End process")
        return json.dumps(parsed)