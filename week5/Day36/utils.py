

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid number!")
            
def show_menu():
    print("\n1. Add Student")
    print("2. View Students")
    print("3. View Courses")
    print("4. Exit")
