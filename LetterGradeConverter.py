def main():
 while True:
    get_grade = int(input("Enter Numerical grade: "))
    if get_grade > 88 and get_grade < 100:
        print("A")
    elif get_grade < 88 and get_grade > 80:
        print("B")
    elif get_grade < 80 and get_grade > 67:
        print("C")
    elif get_grade < 67 and get_grade > 60:
        print("D")
    elif get_grade < 60:
        print("F")
    go_again = input("Continue? (y/n): ").lower()
    if go_again != "y":
      return False
       
main()
