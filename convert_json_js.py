import json
import os

def main():
    json_path = r"c:/Users/ACER/Documents/development/isi kayu/wood_data.json"
    js_output_path = r"c:/Users/ACER/Documents/development/isi kayu/app/data.js"
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        js_content = f"const woodData = {json.dumps(data, indent=2)};"
        
        with open(js_output_path, 'w', encoding='utf-8') as f:
            f.write(js_content)
            
        print(f"Successfully created {js_output_path}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
