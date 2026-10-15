"""
Reusable functions for the Student Performance Analytics System.
Each function performs one clear task so the code is easier to read and test.
"""

import numpy as np
import pandas as pd

SUBJECTS = ["Python", "Mathematics", "Statistics", "Data_Analysis"]
PASS_MARK = 40
MIN_ATTENDANCE = 75


def calculate_total_and_average(data):
    """Add total and average marks columns to a copy of the DataFrame."""
    data = data.copy()
    data["Total_Marks"] = data[SUBJECTS].sum(axis=1)
    data["Average_Marks"] = data[SUBJECTS].mean(axis=1).round(2)
    return data


def assign_grade(average):
    """Return a grade based on the student's average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= PASS_MARK:
        return "E"
    else:
        return "F"


def assign_result(row):
    """A student passes only if every subject mark is at least 40."""
    for subject in SUBJECTS:
        if row[subject] < PASS_MARK:
            return "Fail"
    return "Pass"


def process_student_records(data):
    """Calculate totals, averages, grades, and pass/fail status."""
    data = calculate_total_and_average(data)
    data["Grade"] = data["Average_Marks"].apply(assign_grade)
    data["Result"] = data.apply(assign_result, axis=1)
    data["Attendance_Status"] = np.where(
        data["Attendance_Percent"] >= MIN_ATTENDANCE,
        "Eligible",
        "Low Attendance"
    )
    return data


def get_overall_summary(data):
    """Return the main class-level statistics."""
    return {
        "student_count": len(data),
        "class_average": round(float(np.mean(data["Average_Marks"])), 2),
        "highest_average": round(float(data["Average_Marks"].max()), 2),
        "lowest_average": round(float(data["Average_Marks"].min()), 2),
        "pass_count": int((data["Result"] == "Pass").sum()),
        "fail_count": int((data["Result"] == "Fail").sum()),
        "attendance_eligible_count": int((data["Attendance_Status"] == "Eligible").sum()),
    }


def get_subject_summary(data):
    """Calculate average, highest, and lowest marks for each subject."""
    rows = []
    for subject in SUBJECTS:
        rows.append({
            "Subject": subject.replace("_", " "),
            "Average": round(float(data[subject].mean()), 2),
            "Highest": int(data[subject].max()),
            "Lowest": int(data[subject].min()),
        })
    return pd.DataFrame(rows)


def get_top_performers(data, number=3):
    """Return the top students ranked by average marks."""
    return data.sort_values(
        by=["Average_Marks", "Name"], ascending=[False, True]
    ).head(number)
