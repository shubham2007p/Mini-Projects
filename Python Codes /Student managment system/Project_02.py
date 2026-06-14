
def add_student(students_data , student_data):
    for key,value in student_data.items():
        print(f"{key}:'{value}'")
        answer = input("if satisfied give 'y' else enter your details: ")
        if answer not in "yY":
            student_data[key] = answer
    print(student_data)
    confirm = input("To confirm 'y' else 'n'")
    if confirm in "yY":
        if student_data["Roll no."] in students_data.keys():
            print("Student Exists")
        else:
            students_data[student_data["Roll no."]] = student_data 
            print("ADDED SUCCESSFULLY")   
    else:
        print("Please Try again")
def remove_student(students_data, student_data):
    roll_no = input("Enter roll number of Student: ")
    if roll_no in students_data.keys():
        del students_data[roll_no]
        print("Deleted Succesfully")
    else:
        print("Not found")
    

def search_student(students_data, student_data):
    roll_no = input("Enter roll number of Student: ")
    if roll_no in students_data.keys():
        print(students_data[roll_no])
    else:
        print("Not found")




def main():
    student_data = {"name":None , "Roll no.": None , "Branch":None , "CGPA":None}
    students_data = {}
    while True:
        print("1. Add student\n2. Remove student\n3. Search student\n4. Terminate")
        function_list = [None,add_student, remove_student, search_student]
        choice = int(input("Enter your choice: "))
        if choice==4:
            exit()
        try:
            function_list[choice](students_data, student_data)
        except:
            print("Please choose from valid choices")
if __name__ == "__main__":
    main()