# Maintenance Log Tracker

A command-line tool for tracking and recording maintenance entries on machines.  
This utility allows users to enter and save machine maintenance details into a CSV file for long-term tracking and review.

---

## Features

- Add new maintenance entries interactively
- Store entries in a persistent CSV file
- Automatically creates the CSV file if it doesn't exist
- Clean, user-friendly console output
- Tracks:
  - Machine name
  - Maintenance date
  - Technician name
  - Maintenance performed
  - Hours since last service
  - Time of Entry

---

## Future Features

- Search entries by machine or technician name
- Automatically timestamp each log entry
- Export data in JSON format
- Add a command-line menu or UI
- Visualize maintenance data (e.g., Matplotlib or Pandas)

---

## Technologies Used

- Python 3.13.3
- `csv` module
- `os` module (for file checks)
- `datetime` module
- `datetime` package

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/GKoutilya/maintenance-log.git
