import csv
import os
from datetime import datetime

count = 0
action = ''
total_rows = 0

filename = "maintenance_log.csv"
fieldnames = ["Name of Machine", "Date of Maintenance", "Name of Technician", "Name of Maintenance", "Hours Since Last Service", "Entry Time"]
does_file_exist = os.path.exists(filename)

try:
    with open(filename, mode = 'a', newline = '') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not does_file_exist:
            writer.writeheader()
        
        while True:
            action = input("Would you like to add a maintenance entry? ").casefold()

            if action != "yes":
                break
            
            log = {
                "Name of Machine" : input("What machine? ").strip(),
                "Date of Maintenance" : input("When was the date of maintenance? ").strip(),
                "Name of Technician" : input("What is the name of the technician who worked on the machine? ").strip(),
                "Name of Maintenance" : input("What was the maintenance performed? ").strip(),
                "Hours Since Last Service" : input("How many hours has it been since the last service? ").strip()
            }
            log["Entry Time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            writer.writerow(log)
            count += 1

            print("New Entry Added.")
            print("-" * 40)
            for key, value in log.items():
                print(f"{key}: {value}")
            print("-" * 40)
except Exception as e:
    print("An Error Occured.")
    print(f"Error Details: {e}")

try:
    with open(filename, mode='r', newline='') as file:
        total_rows = sum(1 for _ in file) - 1
except:
    total_rows = 0

print(f"\nTotal entries recorded: {count}")
print(f"Total entries in file: {total_rows}")
print("Thanks and Goodbye!\n")