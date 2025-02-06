#!/usr/bin/python
import sys
import csv
from pathlib import Path
from parser import args

# path to grade sheets CSV
# currently relative to project.py, but later I would like it relative to $HOME and set in a config file or ENV var
PATH_TO_GRADES = "sample_gradebook"
# A sequence of keywords to be excluded from the calculated total score
EXCLUDED_ASSIGNMENTS = ("seat", "id", "name", "report", "speech", "oral")


def main():
    try:
        file_path = Path(PATH_TO_GRADES) / f"{args.class_name}.csv"
        gradesheet = open_gradesheet_csv(file_path)
    except FileNotFoundError:
        sys.exit(f"Error: Class {args.class_name} not found in {PATH_TO_GRADES}")
    if args.output is True:
        updated_gradesheet = calculate_scores(gradesheet)
        pdf_path = file_path.with_suffix(".pdf")
        write_gradesheet_pdf(updated_gradesheet, pdf_path)
        for i in updated_gradesheet:
            print(i)
    else:
        assignment = input("Enter Name of Assignment: ").strip().lower()
        max_score = get_score("Enter max score (5): ", default=5)
        default_score = get_score("Enter default score (0): ", max=max_score)
        updated_gradesheet = add_assignment(
            gradesheet, assignment, max=max_score, default=default_score
        )
        # This File Path Value is a placeholder for testing w/o overwriting the original file
        file_path = "TEST_PATH.csv"
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


def calculate_scores(class_list: list[dict]) -> list[dict]:
    # get a list of keys in dict
    key_names = [x for x in class_list[0].keys()]
    # Remove non-Assignments (seat, name, id, etc)
    try:
        for i in EXCLUDED_ASSIGNMENTS:
            key_names.remove(i)
    except ValueError:
        pass
    max_score = 0
    for assignment in key_names:
        # calculating the max possible points for all assignments
        try:
            max_score += int(class_list[0][assignment])
        except ValueError:
            # if a key contains data that is not an int, exit
            sys.exit(f"Key [{assignment}] contains invalid int value: {class_list[0][assignment]}")
    # loop through all valid students
    for student in class_list:
        valid_assignments = key_names
        student_max = max_score
        student_total = 0
        for assignment in valid_assignments:
            # check for -1 "excused" scores and remove from total possible points
            if student[assignment] == "-1":
                valid_assignments.remove(assignment)
                student_max -= int(class_list[0][assignment])
            # else add the students score to their total gained points
            else:
                try:
                    student_total += int(student[assignment])
                except ValueError:
            # if a key contains data that is not an int, exit
                    sys.exit(f"Key [{assignment}] contains invalid int value: {class_list[0][assignment]}")
        student["total"] = f"{student_total}/{student_max}"
        student_percent = (student_total / student_max) * 100
        student["percent"] = f"{round(student_percent, 2)}%"
    return class_list


def write_gradesheet_csv(class_list: list[dict], path: str):
    # Use list of key names as field names for DictWriter
    key_names = [x for x in class_list[0].keys()]
    with open(path, 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, key_names)
        writer.writeheader()
        for line in class_list:
            writer.writerow(line)


def write_gradesheet_pdf(class_list: list[dict], path: str): ...


if __name__ == "__main__":
    main()
