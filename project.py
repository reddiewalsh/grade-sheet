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
        file_path = Path(PATH_TO_GRADES) / f"{args.class_name}.csv"
        gradesheet = open_gradesheet_csv(file_path)
    except FileNotFoundError:
        sys.exit(f"Error: Class {args.class_name} not found in {PATH_TO_GRADES}")
    if args.output is True:
        updated_gradesheet = calculate_score(gradesheet)
        write_gradesheet_pdf(updated_gradesheet, file_path.replace("csv", "pdf"))
    else:
        assignment = input("Enter Name of Assignment: ").strip().lower()
        max_score = get_score("Enter max score (5): ", default=5)
        default_score = get_score("Enter default score (0): ", max=max_score)
        updated_gradesheet = add_assignment(
            gradesheet, assignment, max=max_score, default=default_score
        )
        write_gradesheet_csv(updated_gradesheet, file_path)
        for row in updated_gradesheet:
            print(row)


def open_gradesheet_csv(path_to_file: str) -> list[dict]:
    """Reads a CSV file and returns a list of students as dict objects"""
    with open(path_to_file) as file:
        reader = csv.DictReader(file)
        return [x for x in reader]


def get_score(message: str, max: int = 100, default: int = 0) -> int:
    """Prompt the user for a score. Scores of -1 are allowed and are considered excused"""
    while True:
        try:
            score = input(message)
            if score == "":
                score = default
            score = int(score)
        except ValueError:
            pass
        except KeyboardInterrupt:
            sys.exit("Status: Exited without saving")
        else:
            if -2 < score <= max:
                break
    return score


def add_assignment(
    class_list: list[dict], assignment_name: str, max=100, default=0
) -> list[dict]:
    """Add an assignment score for each student in the class"""
    for student in class_list:
        if int(student["seat"]) > 0:
            student[assignment_name] = get_score(
                f"Enter Score for {student['seat']}: ",
                max=max,
                default=default,
            )
        else:
            student[assignment_name] = max
    return class_list


def calculate_score(class_list: list[dict]) -> list[dict]:
    ...
    # check for -1 "excused" scores and add to excused list
    # add all valid scores together (drop the -1)
    # add all max scores together


def write_gradesheet_csv(class_list: list[dict], path: str):
    # Use list of key names as field names for DictWriter
    key_names = class_list[0].keys()


def write_gradesheet_pdf(class_list: list[dict], path: str): ...


if __name__ == "__main__":
    main()
