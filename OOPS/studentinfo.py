class studentinfo:
    def __init__(self , name , roll_no , marks):
        self.name = name
        self.roll_no = roll_no 
        self.marks = marks
        
        
    def total_marks(self):
        return sum(self.marks)
    
    def percentage (self):
        return (self.total_marks() / len(self.marks))  
    
    def display_details (self):
        print("Name: ", self.name)
        print("Roll No: ", self.roll_no)
        print("Marks: ", self.marks)
        print("Total Marks: ", self.total_marks())
        print("Percentage :" , self.percentage())
        
Student1 = studentinfo("Om" , 2 , [85 , 52 , 65 , 100 , 50])
Student1.display_details()