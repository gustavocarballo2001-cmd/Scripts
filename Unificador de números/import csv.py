import csv
import sys

# Cambia el nombre de archivo según tu caso
input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.csv'
output_file = sys.argv[2] if len(sys.argv) > 2 else 'output.csv'

with open(input_file, newline='', encoding='utf-8') as csvfile_in, \
     open(output_file, 'w', newline='', encoding='utf-8') as csvfile_out:
    reader = csv.DictReader(csvfile_in)
    writer = csvfile_out

    for row in reader:
        nombre = row.get('first_name', '').strip() or row.get('name', '').strip()
        apellido = row.get('last_name', '').strip() or row.get('Apellido', '').strip()
        celular = row.get('phone_number', '').strip()

        # Mantiene el número completo del CSV (+ y código de país), limpiando solo formato.
        celular_normalizado = ''.join(ch for ch in celular if ch.isdigit() or ch == '+')
        if celular_normalizado.count('+') > 1:
            celular_normalizado = '+' + celular_normalizado.replace('+', '')
        elif '+' in celular_normalizado and not celular_normalizado.startswith('+'):
            celular_normalizado = '+' + celular_normalizado.replace('+', '')
        linea_final = f"{nombre} {apellido},{celular_normalizado}\n"
        writer.write(linea_final)