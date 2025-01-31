import sys
import os

def extract_logs(file_path, target_date):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = f"{output_dir}/output_{target_date}.txt"

    with open(file_path, "r", encoding="utf-8") as log_file, open(output_file, "w", encoding="utf-8") as out_file:
        for line in log_file:
            if line.strip().startswith(target_date):
                out_file.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)
    
    date_to_extract = sys.argv[1]
    log_file_path = "logs_2024.log"

    extract_logs(log_file_path, date_to_extract)

    print(f"Logs extracted to output/output_{date_to_extract}.txt")