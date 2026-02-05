import csv
import json
import os

def parse_value_preserve_format(value):
    if not value or value.strip() == '':
        return None
    
    # Remove quotes and whitespace
    clean_value = value.strip().strip('"')
    
    # Standardize: Ensure comma is used as decimal separator
    # If it has a dot and no comma, replace dot with comma (maoni.csv style: 0.01 -> 0,01)
    # If it already has comma (jati.csv style: 0,150), keep it as is.
    if '.' in clean_value:
        clean_value = clean_value.replace('.', ',')
        
    return clean_value

def convert_csv_to_json(file_path):
    data = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
        # Header row contains lengths
        headers = rows[0]
        lengths = [h.strip() for h in headers[1:] if h.strip()]
        
        for row in rows[1:]:
            if not row or not row[0].strip():
                continue
                
            diameter = row[0].strip()
            row_data = {}
            for i, length in enumerate(lengths):
                if i + 1 < len(row):
                    val = parse_value_preserve_format(row[i+1])
                    if val is not None:
                        row_data[length] = val  # Store as string
            
            if row_data:
                data[diameter] = row_data
                
    return data

def main():
    base_dir = r"c:/Users/ACER/Documents/development/isi kayu"
    output_file = os.path.join(base_dir, "wood_data.json")
    
    result = {}
    
    # Process jati.csv
    jati_path = os.path.join(base_dir, "jati.csv")
    if os.path.exists(jati_path):
        print(f"Processing {jati_path}...")
        result['jati'] = convert_csv_to_json(jati_path)
        
    # Process maoni.csv
    maoni_path = os.path.join(base_dir, "maoni.csv")
    if os.path.exists(maoni_path):
        print(f"Processing {maoni_path}...")
        result['mahoni'] = convert_csv_to_json(maoni_path)
        
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
        
    print(f"JSON data saved to {output_file}")

if __name__ == "__main__":
    main()
