def write(converted: str, filename: str):
    with open(f'{filename}.json', 'w', encoding='utf-8') as f:
        f.write(converted)