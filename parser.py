import argparse

parser = argparse.ArgumentParser()
parser.add_argument("class", help="select the name of the class")
parser.add_argument("-a", "--add-score", help="Add a score to class (default)")
args = parser.parse_args()