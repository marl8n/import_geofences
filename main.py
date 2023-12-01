from csv_parser.parse_csv_to_json import parse_csv_to_json
from writer.write_json import write
from os import listdir

def run():
    base_csv_dir = './geofences_csv'
    filenames = [f for f in listdir(base_csv_dir)]

    for f in filenames:
        parsed = parse_csv_to_json(f'{base_csv_dir}/{f}')
        formatted_name = f.replace('.csv', '')
        write(parsed, f'{formatted_name}.json')

if __name__ == '__main__':
    run()