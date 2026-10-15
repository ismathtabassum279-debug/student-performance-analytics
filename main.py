"""
Student Performance Analytics System
Run this file to analyze the students.csv dataset.
"""

from pathlib import Path
import pandas as pd
from functions import (
    SUBJECTS,
    process_student_records,
    get_overall_summary,
    get_subject_summary,
    get_top_performers,
)


def main():
    # Find students.csv in the same folder as this Python file.
    project_folder = Path(__file__).resolve().parent
    dataset_path = project_folder / "students.csv"

    # Stop with a clear message if the dataset file is missing.
    if not dataset_path.exists():
        print("Error: students.csv was not found. Keep it beside main.py.")
        return

    # Read the CSV data into a Pandas DataFrame.
    students = pd.read_csv(dataset_path)

    # Show a quick overview of the dataset.
    print("=" * 72)
    print("Student Performance Analysis")
    print("=" * 72)
    print(f"Number of student records: {len(students)}")
    print("\nDataset columns:")
    print(list(students.columns))
    print("\nFirst five records:")
    print(students.head().to_string(index=False))

    # Check whether required columns exist before doing calculations.
    required_columns = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance_Percent"]
    missing_columns = [column for column in required_columns if column not in students.columns]
    if missing_columns:
        print("\nError: Missing required columns:", ", ".join(missing_columns))
        return

    # Ensure marks and attendance are numeric and within valid ranges.
    numeric_columns = SUBJECTS + ["Attendance_Percent"]
    for column in numeric_columns:
        students[column] = pd.to_numeric(students[column], errors="coerce")

    if students[numeric_columns].isnull().any().any():
        print("\nError: Marks or attendance contain blank/non-numeric values.")
        return

    if ((students[SUBJECTS] < 0) | (students[SUBJECTS] > 100)).any().any():
        print("\nError: Subject marks must be between 0 and 100.")
        return

    if ((students["Attendance_Percent"] < 0) | (students["Attendance_Percent"] > 100)).any():
        print("\nError: Attendance must be between 0 and 100.")
        return

    # Calculate each student's total, average, grade, and result.
    results = process_student_records(students)

    print("\n" + "-" * 72)
    print("STUDENT MARKS SUMMARY")
    print("-" * 72)
    summary_columns = [
        "Student_ID", "Name", "Department", "Total_Marks",
        "Average_Marks", "Grade", "Result", "Attendance_Status"
    ]
    print(results[summary_columns].head(10).to_string(index=False))
    if len(results) > 10:
        print(f"Showing 10 of {len(results)} student records. Full results are saved in student_analysis_output.csv.")

    # Display class-level statistics.
    overall = get_overall_summary(results)
    print("\n" + "-" * 72)
    print("CLASS SUMMARY")
    print("-" * 72)
    print(f"Total students: {overall['student_count']}")
    print(f"Class average: {overall['class_average']}")
    print(f"Highest student average: {overall['highest_average']}")
    print(f"Lowest student average: {overall['lowest_average']}")
    print(f"Students passed: {overall['pass_count']}")
    print(f"Students failed: {overall['fail_count']}")
    print(f"Students with attendance of at least 75%: {overall['attendance_eligible_count']}")

    # Display subject-wise performance.
    print("\n" + "-" * 72)
    print("SUBJECT-WISE PERFORMANCE")
    print("-" * 72)
    subject_summary = get_subject_summary(results)
    print(subject_summary.to_string(index=False))
    best_subject = subject_summary.loc[subject_summary["Average"].idxmax()]
    print(f"\nBest-performing subject by average: {best_subject['Subject']} ({best_subject['Average']})")

    # Display the three highest-performing students.
    print("\n" + "-" * 72)
    print("TOP 3 PERFORMERS")
    print("-" * 72)
    top_students = get_top_performers(results, number=3)
    print(top_students[["Student_ID", "Name", "Department", "Average_Marks", "Grade"]].to_string(index=False))

    # Show department-level average performance.
    print("\n" + "-" * 72)
    print("DEPARTMENT-WISE AVERAGE")
    print("-" * 72)
    department_summary = (
        results.groupby("Department")["Average_Marks"]
        .mean()
        .round(2)
        .sort_values(ascending=False)
    )
    print(department_summary.to_string())

    # Save a new CSV containing the calculated results.
    output_path = project_folder / "student_analysis_output.csv"
    results.to_csv(output_path, index=False)
    print(f"\nDetailed analysis saved to: {output_path.name}")
    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
