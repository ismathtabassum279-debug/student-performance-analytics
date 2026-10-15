# Project Documentation

## 1. Project Title
Student Performance Analytics System

Student Name: Ismath Tabassum  
Course: Python with AI  
Training Provider: EWB Courses

## 2. Objective
This project reads student marks and attendance from a CSV file. It calculates totals, averages, grades and pass/fail results. It also shows class performance, subject averages and the top three students.

## 3. Technologies Used
- Python
- Pandas
- NumPy
- CSV file for storing the data

## 4. Dataset Description
The `students.csv` file contains 20 sample student records. Each record has a student ID, name, department, marks in four subjects and an attendance percentage. The marks and attendance values are between 0 and 100. These are sample records made for this project.

## 5. Implementation
1. The program reads `students.csv` with Pandas.
2. It checks whether the required columns are present and whether marks and attendance contain valid numbers.
3. It calculates each student's total and average marks.
4. It assigns a grade using `if` and `elif` conditions.
5. It checks each subject with a loop. A student passes only when every subject mark is 40 or above.
6. NumPy is used to label attendance of 75% or above as `Eligible`; lower attendance is labelled `Low Attendance`.
7. The program calculates class statistics, subject-wise results, top performers and department averages.
8. The processed results are saved to `student_analysis_output.csv`.

## 6. Key Features
- Reads student data from a CSV file.
- Calculates total and average marks.
- Assigns grades from A+ to F.
- Finds pass and fail results.
- Shows highest, lowest and average performance.
- Calculates average, highest and lowest marks for each subject.
- Displays the top three students.
- Shows department-wise average marks.
- Checks for missing columns and invalid marks or attendance.
- Saves the processed data to a new CSV file.

## 7. Output / Screenshots
Run `python main.py` and take screenshots of:
- The dataset preview.
- The student marks summary.
- The class and subject summaries.
- The top three performers and department averages.

Add your screenshots here before submitting the project.

The student summary printed in the terminal shows up to 10 rows so the output stays readable. The full set of records is saved in `student_analysis_output.csv`. No charts are used.

## 8. Final Outcome
The program analyses the 20 sample records and displays useful information about student marks, grades, results, attendance, subjects and departments. It also saves the calculated results to a CSV file.

## 9. Challenges & Learning
After running the project, update this section with what you personally found difficult and learned. Possible topics include reading CSV files, using Pandas DataFrames, writing functions, applying conditions, using loops and checking data values. Keep only the points that describe your own experience.

## 10. GitHub Repository
Repository URL: Add your GitHub repository link here after uploading the project.

Before submitting, check that the repository includes `main.py`, `functions.py`, `students.csv`, `requirements.txt`, `README.md` and this documentation file. Submit the repository link through the EWB Google Form.
