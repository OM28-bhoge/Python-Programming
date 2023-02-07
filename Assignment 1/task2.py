def convert_to_final_grade(assessment_marks):
    total = sum(assessment_marks)
    if total >= 180:
        return "HD"
    elif total >= 150:
        return "D"
    elif total >= 120:
        return "C"
    elif total >= 100:
        return "P"
    elif total >= 50:
        return "SA"
    else:
        return "AF"

def get_supplementary_mark(assessment_marks):
    total = sum(assessment_marks)
    if total < 100:
        supplementary_mark = int(input("What is this student's supplementary exam mark: "))
        if supplementary_mark >= 50:
            return "SP"
        else:
            return "F"
    else:
        return convert_to_final_grade(assessment_marks)

def get_grade_point_value(final_grade_letter):
    if final_grade_letter == "HD":
        return 4.0
    elif final_grade_letter == "D":
        return 3.0
    elif final_grade_letter == "C":
        return 2.0
    elif final_grade_letter == "P":
        return 1.0
    elif final_grade_letter == "SP":
        return 0.5
    else:
        return 0

def main():
    student_marks = []
    while True:
        marks = input("Enter a student's assessment marks (separated by comma), type in letter N to finish: ")
        if marks == "N":
            break
        marks = [int(mark) for mark in marks.split(",")]
        student_marks.append(marks)
    
    final_grades = []
    total_grade_points = 0
    for assessment_marks in student_marks:
        final_grade = get_supplementary_mark(assessment_marks)
        final_grades.append(final_grade)
        grade_point_value = get_grade_point_value(final_grade)
        total_grade_points += grade_point_value
    
    print("Final grades:", final_grades)
    print("Total grade points:", total_grade_points)

if __name__ == "__main__":
    main()