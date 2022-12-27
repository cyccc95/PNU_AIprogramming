import LGstudent

def main():
  ## Calculate and display a student's semester letter grade
  name = input("Enter student's name: ")
  midterm = float(input("Enter grade on midterm exam: "))
  final = float(input("Enter grade on final exam: "))
  # Create an instance of an LGstudent object
  st = LGstudent.LGstudent(name, midterm, final)
  print("\nNAME\tGRADE")
  # Display student's name and semester letter grade
  print(st)

main()