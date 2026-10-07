# Assignment Name: Scholarship Eligibility Checker

"""
Thursday Individual Assignment
Build a tested decision application.
• Choose a real-world decision problem.
• Write the rules in plain English first.
• Use at least 3 inputs.
• Use correct input conversion.
• Use if/elif/else.
• Use at least one logical operator.
• Include at least one calculation where appropriate.
• Create at least 6 test cases.
• Include at least 2 boundary cases.
• Find and fix at least one bug.
• Make at least 3 meaningful Git commits.
• Write a short note explaining one bug you found and how you fixed it.
"""

# INPUT
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
level_of_study = int(input("Current Level: "))
cummulative_grade_point = float(input("Current CGPA: "))

# CONDITION FOR ELIGIBILITY
if level_of_study >= 200 and cummulative_grade_point >= 4.0:
    is_eligible = True
    continue_application = input("You are eligible for this scholarship. Continue with application? Yes/No: ")
    if continue_application == "yes":
        print("Application in progress....")
        print("Congratulation. Application successful.")
    else:
        print("Application terminated")
elif level_of_study >= 200 and cummulative_grade_point <= 4.0:
    is_eligible = False
    print("CGPA is low. Try again next year")
elif level_of_study <= 200 and cummulative_grade_point >= 4.0:
    is_eligible = False
    print("Scholarship not applicable to freshman. Try next year")
else: 
    is_eligible = False
    print("You are not qualified for this scholarship")