# Class Participation Gradesheet (CS50P Final Project)

#### Video Demo: <URL HERE: TODO>

### Description:

##### Introduction:

Hello, my name is Edward Walsh. I am an American that is currently living and working in Taiwan as an English Teacher. This project is a tool that I have created for my own personal use as a teacher. 

##### The Problem:

Each semester I am required to track student participation for around 20 different classes. There is no software provided for this task and each class is required to have a paper copy of the participation scores of each student on a class-by-class basis. Creating and managing these "score grids" is a time consuming and repetitive process. I need a solution that can allow me to enter the grades of each student rapidly and output a nicely formated  "score grid" with each student's daily score as well as a calculated total percentage.

##### The Solution: 

This grade sheet application is based on around reading and writing CSV files. Each CSV file represents a single class. Each use of the application will allow the user to either rapidly add scores/marks to each student for a single assignment, or (if the -o flag is passed) to output a PDF that can be printed out as the required hard-copy, or as reference.

>NOTE: As the application is still at a very early stage of development, edits and alterations to student scores must be made by manually manipulating the CSV file. This should change in the future, as I plan on building on this application as my needs change and other, more vital features are implemented.

##### How to Use:

###### Installation:

To install this application:

1. CD into whichever directory you'd like to install the application.
1. Clone this repository:
    ```bash
    git clone https://github.com/reddiewalsh/grade-sheet.git 
    ```
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

###### Creating a Gradesheet:

Currently the application does not create a gradesheet for you. This is because I am provided with an excel spreadsheet with student information for each class. Creating a gradesheet from this point is simply deleting columns I don't require and exporting to CSV format.

If you would like to use this application you will need a valid gradesheet.csv file. The correct format will have a header row with at least one column: "seat". The "seat" values can be any integer you would like, but each "seat" number should be unique. If you sort your students alphabetically, you would probably have "Aaron A. Aaronson" in "seat" 1, while "Zoey Z. Zimmerman" would probably be in the last "seat". The CSV also requires a special "seat" number 0. This is used by the program to record the maximum possible scores for each assignment and calculate the total/percentage scores.

I'm  using the term "seat" to avoid confusion, as Student ID or Student Number is also used in my school as a unique identifier, but doesn't provide much context to who the student is. Later I would like to make this a configurable option to allow for more choices.


###### Adding an Assignment:

1. Type in the command followed by the name of the class you are working on:
    The name of the class is the same as the name of your CSV file, but you should not include the ~.csv~ extension. 
	```bash
	python project.py <CLASS_NAME>
	```
2. The application will prompt you for the name of your assignment. The name of your assignment can be anything you'd like, but try to keep the names short. Otherwise, you will waste a lot of space on your PDF when you export the class.
3. The application will prompt you for a maximum score (default = 5): 
   Please enter the maximum score students could achieve on this assignement. If you leave this blank, a maximum score of 5 will be set automatically. The number 5 was chosen specifically for my class, as most of my scores in classes will be for small homework assignments and classroom participation scores. However, you are free to set any whole number you'd like.
4. The Application will then prompt you for a default score (default = 0):
   The default score is what the application will use when a student's score is left blank/skipped. It defaults to zero, but a possible used case for setting the default to another number is if the majority or large portion of the scores are a specific number, you could set that score as the default to quickly enter students' grades with the <Enter> key.




