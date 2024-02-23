import os
import chardet
import csv

def list_csv_files(folder_path: str) -> list:
    csv_files = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            csv_files.append(os.path.join(folder_path, file_name))
    return csv_files

def detect_encoding(filename: str) -> str:
    with open(filename, 'rb') as file:
        raw_data = file.read(1024)
    result = chardet.detect(raw_data)
    return result['encoding']

def detect_delimiter(filename: str, encoding: str) -> str:
    with open(filename, 'r', encoding=encoding) as file:
        sample = file.read(1024)
    sniffer = csv.Sniffer()
    return sniffer.sniff(sample).delimiter


archive = list_csv_files('data')

for i in archive:
    encoding = detect_encoding(i)
    print(encoding)
    delimiter = detect_delimiter(i, encoding)
    print(delimiter)
