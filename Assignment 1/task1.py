def interim_grade(Assessments):
    final_mark = round(sum(Assessment * weight / 100 for Assessment, weight in zip(Assessments, [20, 40, 40])))
    zero_count = Assessments.count(0)
    if final_mark >= 85:
        return "HD"
    elif final_mark >= 75:
        return "D"
    elif final_mark >= 65:
        return "C"
    elif final_mark >= 50:
        return "P"
    elif final_mark >= 45:
        if zero_count >= 2 or zero_count == len(Assessments):
            return "AF"
        elif zero_count == 0 and Assessments.count(min(Assessments)) == 1:
            return "SE" if Assessments.index(min(Assessments)) == 2 else "SA"
        else:
            return "F"
    else:
        return "AF" if zero_count >= 2 or zero_count == len(Assessments) else "F"

Assessments = list(map(float, input("Enter the student's assessment marks separated by a comma: ").split(",")))
print("Interim grade:", interim_grade(Assessments))
