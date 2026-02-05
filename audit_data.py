import json
import os

def main():
    json_path = r"c:/Users/ACER/Documents/development/isi kayu/wood_data.json"
    
    if not os.path.exists(json_path):
        print("JSON file not found.")
        return

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        print("--- MAHONI VERIFICATION ---")
        mahoni_data = data.get('mahoni', {})
        
        # Check Sample 1: D10 L100
        # Row 2, Col 2 in CSV logic
        val_10_100 = mahoni_data.get('10', {}).get('100')
        print(f"Mahoni D10 / P100: {val_10_100} (Expect 0.01 or 0,01)")
        
        # Check Sample 2: D30 L200
        val_30_200 = mahoni_data.get('30', {}).get('200')
        print(f"Mahoni D30 / P200: {val_30_200} (Expect 0.16 or 0,16)")
        
        # Check Sample 3: D40 L300
        val_40_300 = mahoni_data.get('40', {}).get('300')
        print(f"Mahoni D40 / P300: {val_40_300}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
