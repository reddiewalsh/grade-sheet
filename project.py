#!/usr/bin/python
import sys
import csv
from pathlib import Path
from parser import args

# path to grade sheets CSV 
# currently relative to project.py, but later I would like it relative to $HOME and set in a config file or ENV var
PATH_TO_GRADES = "sample_gradebook"


def main():
    try:
        grade_sheet = open_grade_sheet(args.class_name, PATH_TO_GRADES)
    except FileNotFoundError:
        sys.exit(f"Error: Class {args.class_name} not found in {PATH_TO_GRADES}")
    for student in grade_sheet:
        print(student)


def open_grade_sheet(name_of_class: str, path_to_file: str):
    with open(Path(path_to_file) / f"{name_of_class}.csv") as file:
        reader = csv.DictReader(file)
        return [x for x in reader]
    

if __name__ == "__main__":
    main()
