import csv

names = [
    {"Make": "Toyota", "Model": "Corolla", "Trim": "XLE", "Year": "2023", "License Plate": "3FRG423", "Status": "Available"},
    {"Make": "Honda", "Model": "Accord", "Trim": "Sport", "Year": "2004", "License Plate": "4FJG343", "Status": "Available"},
    {"Make": "Kia", "Model": "Forte", "Trim": "LX", "Year": "1999", "License Plate": "5TYH858", "Status": "Maintenance"},
    {"Make": "Porsche", "Model": "911", "Trim": "Turbo", "Year": "2010", "License Plate": "6GGD221", "Status": "Rented"},
]

with open("view.csv", mode="w") as csvfile:
    fieldnames = names[0].keys()  # Using 'names' instead of 'view'
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  # Write header row
    writer.writerows(names)

