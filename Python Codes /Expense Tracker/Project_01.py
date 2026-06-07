def add_expense(expenses_list):
    amount = int(input("Enter the expense amount: "))
    expenses_list.append(amount)
    return

def view_expenses(expenses_list):
    print(expenses_list)
    return

def total_expense(expenses_list):
    print(sum(expenses_list))
    return

def delete_expense(expenses_list):
    amount = int(input("Enter the expense amount you want to delete: "))
    try:
        expenses_list.remove(amount)
    except:
        print(amount, "isn't present in the list")

def expense_record_maker(expenses_list):
   f = open("expense.txt", "w")
   for expense in expenses_list:
    f.write(str(expense) + "\n")
   f.close()
   return

def expense_record_reader(expenses_list):
    f = open("expense.txt", "r")
    expenses_list = f.read()
    print(expenses_list)
    f.close()
    return

def quit(nothing):
    exit()

def main():
    expense_list =[]
    while True:
        print("1. Add expenses \n2. View expenses \n3. Total expense \n4. Delete expense \n5. Make expense record \n6. Read expense record \n7. Exit")
        function_list =[add_expense, view_expenses, total_expense, delete_expense, expense_record_maker, expense_record_reader, quit]
        choice = int(input("Enter your choice: "))
        try:
            function_list[choice-1](expense_list)
        except:
            print("Please choose from valid choices")

if __name__ == "__main__":
    main()

"""
Developer Notes:
1. First i got stuck how to proceed then i made all the dunction with argument pass in them and main fucntion fully functional

2. then i made all fucntion working 


"""

    