import argparse

parser = argparse.ArgumentParser()
parser.add_argument("class_name", metavar="CLASS", help="select the name of the class")
parser.add_argument("-o", "--output", help="print scoresheet to PDF")
args = parser.parse_args()