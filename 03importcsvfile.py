import pandas as pd
from datetime import datetime, timedelta
import os

def process_attendance(daily_csv, monthly_csv, session_start, session_end="23:00"):
    # Load daily attendance sheet
    try:
        daily_df = pd.read_csv(daily_csv)
    except Exception as e:
        print(f"Error loading daily attendance CSV: {e}")
        return
    
    # Load or create the monthly attendance sheet
    if os.path.exists(monthly_csv):
        monthly_df = pd.read_csv(monthly_csv)
    else:
        monthly_df = pd.DataFrame(columns=["ID", "Name"])
    
    # Convert session start and end times to datetime
    session_start = datetime.strptime(session_start, "%H:%M")
    session_end = datetime.strptime(session_end, "%H:%M")
    session_duration = (session_end - session_start).total_seconds() / 60  # in minutes
    
    # Ensure daily_df has expected columns
    required_columns = {"Full Name", "User ID", "Join Time", "Leave Time"}
    if not required_columns.issubset(daily_df.columns):
        print("Error: Daily CSV is missing required columns")
        return
    
    # Convert join and leave times to datetime
    daily_df["Join Time"] = pd.to_datetime(daily_df["Join Time"], errors='coerce')
    daily_df["Leave Time"] = pd.to_datetime(daily_df["Leave Time"], errors='coerce')
    
    # Handle missing leave times by setting them to session_end
    daily_df["Leave Time"].fillna(session_end, inplace=True)
    
    # Calculate total attendance time per user
    attendance_summary = daily_df.groupby(["User ID", "Full Name"]).apply(
        lambda group: (group["Leave Time"] - group["Join Time"]).sum()
    ).reset_index()
    attendance_summary.columns = ["ID", "Name", "Total Duration"]
    attendance_summary["Total Duration"] = attendance_summary["Total Duration"].dt.total_seconds() / 60  # Convert to minutes
    
    # Determine if the student is present (>=80% of session duration)
    attendance_summary["Status"] = attendance_summary["Total Duration"].apply(
        lambda minutes: "Y" if minutes >= (0.8 * session_duration) else "N"
    )
    
    # Get the date column name
    attendance_date = datetime.now().strftime("%Y-%m-%d")
    
    # Merge with the monthly sheet
    if attendance_date not in monthly_df.columns:
        monthly_df[attendance_date] = "N"  # Default to absent
    
    for _, row in attendance_summary.iterrows():
        if row["ID"] in monthly_df["ID"].values:
            monthly_df.loc[monthly_df["ID"] == row["ID"], attendance_date] = row["Status"]
        else:
            new_entry = {"ID": row["ID"], "Name": row["Name"], attendance_date: row["Status"]}
            monthly_df = monthly_df.append(new_entry, ignore_index=True)
    
    # Save the updated monthly sheet
    updated_filename = "Monthly_Attendance_Updated.csv"
    monthly_df.to_csv(updated_filename, index=False)
    print(f"Attendance updated successfully in {updated_filename}")

# Example usage
process_attendance("daily_attendance.csv", "monthly_attendance.csv", "09:00", "17:00")



