import LGstudent

def main():
  ## Calculate and display student's semester letter grades
  listOfStudents = [] # To holds objects each for a student
  carryOn = 'Y'

  while carryOn == 'Y': # Repeat until user says 'N'
    st = LGstudent.LGstudent()
    # Obtain student's name and grades
    name = input("Enter student's name: ")
    midterm = float(input("Enter student's grade on midterm exam: "))
    final = float(input("Enter student's grade on final exam: "))
    # Create an instance of an LGstudent object
    st = LGstudent.LGstudent(name, midterm, final)
    listOfStudents.append(st) # Insert object into list
    carryOn = input("Do you want to continue (Y/N)? ")
    carryOn = carryOn.upper()
  print("\nNAME\tGRADE")
  # Display students, names and semester letter grades
  for pupil in listOfStudents:
    print(pupil)

main()