def export_to_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
