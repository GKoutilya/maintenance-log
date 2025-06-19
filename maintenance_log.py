import csv
import os
from datetime import datetime

count = 0

def add_entry(writer):
    global count
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

    print(f"\nTotal entries recorded: {count}")

def view_entries():
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            if not rows:
                print("No entries found.")
                return

            for row in rows:
                print("-" * 40)
                for key, value in row.items():
                    print(f"{key}: {value}")
            print("-" * 40)

    except Exception as e:
        print("An Error Occurred.")
        print(f"Error Details: {e}")

def search_by_machine(machine_name, filename):
    found = False
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Name of Machine"].lower() == machine_name.lower():
                    found = True
                    print("-" * 40)
                    for key, value in row.items():
                        print(f"{key}: {value}")
                    print("-" * 40)
            
            if not found:
                print(f"No maintenance entries found for machine: '{machine_name}'.")

    except Exception as e:
        print("An Error Occured.")
        print(f"Error Details: {e}")

def count_rows():
    try:
        with open(filename, mode='r', newline='') as file:
            return sum(1 for _ in file) - 1
    except:
        return 0

filename = "maintenance_log.csv"
fieldnames = ["Name of Machine", "Date of Maintenance", "Name of Technician", "Name of Maintenance", "Hours Since Last Service", "Entry Time"]
does_file_exist = os.path.exists(filename)

try:
    with open(filename, mode = 'a', newline = '') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not does_file_exist:
            writer.writeheader()
        
        while True:
            try:
                action = int(input("What would you like to do?\n1. Add a new maintenance entry\n2. View All Entries\n3. Search logs by machine\n4. Quit\n"))
            except ValueError:
                print("Please enter a valid number (1–4).")
                continue

            if action == 4:
                break
            
            if action == 1:
                add_entry(writer)

            if action == 2:
                view_entries()

            if action == 3:
                machine_name = input("What machine? ")
                search_by_machine(machine_name, filename)

except Exception as e:
    print("An Error Occured.")
    print(f"Error Details: {e}")


print(f"\nTotal new entries this session: {count}")
print(f"Total entries in file: {count_rows()}")
print("Thanks and Goodbye!\n")