# This is the day 16 Assignment. It is a file handling exercise. The code is in the file day16_exercise.py. The code is as follows:

print("Welcome to the Note Saver App!")

print("===== NOTE SAVER APP =====")

note = input("Type in your details note here: ")
file = open("note.txt", "w")
file.write(note + "\n")
file.close()

print("Your note has been saved to note.txt")
print()
# To read the saved notes, you can use the following code:
file = open("note.txt", "r")
saved_notes = file.read() 
print("Saved Notes:", saved_notes)


file.close()