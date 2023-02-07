#print('Hello')
#print('Om Vinay Bhoge')
#print('DIV - B , ROLL NO - 2 , PRN NO - 1132220032')

#artist = ["Post Malone" , "Taylor Swift" , "Drake" , "MC Stan" , "Raga"]

#is_MC_Stan = False

marks = input("Enter a student's assessment marks (separated by comma):")
marks = [float(item) for item in  marks.split(',')]
final_marks = int((marks[0] * 0.2 + marks[1] * 0.4 + marks[2] * 0.4) + 0.5)

if((marks[0] == 0 and marks[1] == 0) or (marks[0] == 0 and marks[2] == 0) or (marks[1] == 0 and marks[2] == 0)):   
    if(final_marks <= 44):    
        grade = 'AF'
elif(final_marks <= 44):
    grade = 'F'
elif(marks[0] != 0 and marks[1] != 0 and marks[2] != 0):  
    if(final_marks >= 45 and final_marks <= 49):    
        if((marks[0] < 50 and marks[1] < 50) or (marks[1] < 50 and marks[2] < 50) or (marks[0] < 50 and marks[2] < 50)):    
            grade = 'F'
        elif((marks[0] < 50 and marks[1] > 50) or (marks[0] > 50 and marks[1] < 50)):  
            grade = 'SA'
        elif(marks[2] < 50):
             grade = 'SE'      
    elif(final_marks >= 50 and final_marks <= 64):
        grade = 'P'
    elif(final_marks >= 65 and final_marks <= 74):
        grade = 'C'
    elif(final_marks >= 75 and final_marks <= 84):
        grade = 'D'
    elif(final_marks >= 85):
        grade = 'HD'
elif((marks[0] == 0 or marks[1] == 0 or marks[2] == 0) and final_marks >= 45 and final_marks <= 49):
    grade = 'F'
    
print('Final marks: ',final_marks)
print('Grade: ',grade)