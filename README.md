# Student Performance Analytics System

This is a Python project that analyses student marks and attendance using Pandas and NumPy.

## Files
- `main.py` — starts the program and prints the results.
- `functions.py` — contains functions for calculations and student results.
- `students.csv` — sample data for 20 students.
- `requirements.txt` — packages needed to run the program.
- `Project_Documentation.md` — project report.

## Rules used
- Four subjects are scored out of 100: Python, Mathematics, Statistics and Data Analysis.
- Total marks are the sum of the four subjects.
- Average marks are the mean of the four subjects.
- A student passes only if every subject mark is at least 40.
- Grades: A+ (90 and above), A (80–89.99), B (70–79.99), C (60–69.99), D (50–59.99), E (40–49.99), F (below 40).
- Attendance of 75% or more is labelled `Eligible`. This is separate from the marks-based pass/fail result.

## Run the project
Install Python, open a terminal in this folder and run:

```bash
pip install -r requirements.txt
python main.py
```

The terminal shows the main analysis. The student summary displays up to 10 rows. All processed student records are saved to `student_analysis_output.csv`. The project does not use charts.

## GitHub
Upload the Python files, dataset, README and documentation to your repository. Add your repository URL to the documentation and submit it through the EWB Google Form.
