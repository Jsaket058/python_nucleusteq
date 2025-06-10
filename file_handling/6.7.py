# 7. Write a program to read a CSV file and calculate column averages.

import csv

def calculate_column_averages(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        totals = {}
        counts = {}

        for row in reader:
            for key, value in row.items():
                if key != "Name":
                    try:
                        num = float(value)
                        totals[key] = totals.get(key, 0) + num
                        counts[key] = counts.get(key, 0) + 1
                    except ValueError:
                        continue  

        for key in totals:
            avg = totals[key] / counts[key]
            print(f"Average of {key}: {avg:.2f}")

calculate_column_averages('file_handling/data.csv')
