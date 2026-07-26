# GPA Calculator based on Quality Point Table 
# Developed for 2 and 3 Credit Hour subjects

def get_quality_points(marks, credit):
    """Return Quality Points based on marks and credit hours (2 or 3)."""

    # For 2 Credit Hour subjects (out of 40 marks)
    qp_2cr = {
        16: 2.00, 17: 2.50, 18: 3.00, 19: 3.50,
        20: 4.00, 21: 4.33, 22: 4.67, 23: 5.00,
        24: 5.33, 25: 5.67, 26: 6.00, 27: 6.33,
        28: 6.67, 29: 7.00, 30: 7.33, 31: 7.67
    }

    # For 3 Credit Hour subjects (out of 60 marks)
    qp_3cr = {
        24: 3.00, 25: 3.50, 26: 4.00, 27: 4.50,
        28: 5.00, 29: 5.50, 30: 6.00, 31: 6.33,
        32: 6.67, 33: 7.00, 34: 7.33, 35: 7.67,
        36: 8.00, 37: 8.33, 38: 8.67, 39: 9.00,
        40: 9.33, 41: 9.67, 42: 10.00, 43: 10.33,
        44: 10.67, 45: 11.00, 46: 11.33, 47: 11.67
    }

    # Handle A-grade upper limits
    if credit == 2 and marks >= 32:
        return 8.00
    elif credit == 3 and marks >= 48:
        return 12.00

    # Return table value or 0 if marks not found
    if credit == 2:
        return qp_2cr.get(marks, 0)
    elif credit == 3:
        return qp_3cr.get(marks, 0)
    else:
        return 0


def calculate_gpa():
    print("========== GPA CALCULATOR ==========\n")
    total_subjects = int(input("Enter total number of subjects: "))

    total_qp = 0
    total_cr = 0

    for i in range(total_subjects):
        print(f"\nSubject {i + 1}:")
        marks = int(input("  Enter obtained marks: "))
        credit = int(input("  Enter credit hours (2 or 3): "))

        qp = get_quality_points(marks, credit)
        total_qp += qp
        total_cr += credit

        print(f"  → Quality Points: {qp:.2f}")

    if total_cr == 0:
        print("Invalid input! Total credit hours cannot be zero.")
        return

    gpa = total_qp / total_cr

    print("\n========== GPA SUMMARY ==========")
    print(f"Total Credit Hours : {total_cr}")
    print(f"Total Quality Points: {total_qp:.2f}")
    print(f"Final GPA           : {gpa:.2f}")
    print("=================================")


# Run the program
calculate_gpa()
