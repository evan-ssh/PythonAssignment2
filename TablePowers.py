def main():
 while True:
    start_number = int(input("Start number: "))
    stop_number = int(input("Stop number: ")) + 1
    if start_number > stop_number:
       print("Start number cannot be greater than stop.")
       continue
    else:
        print(f"Number\n====")
        numbers(start_number, stop_number)
        print(f"Square\n====")
        square_number(start_number, stop_number)
        print(f"Cube\n====")
        cube_number(start_number, stop_number)
    

def numbers(start_number, stop_number):
    for x in range(start_number, stop_number):
       print(x) 
    print()       
      
def square_number(start_number, stop_number):
    for x in range(start_number, stop_number):
        square_number =  x ** 2
        print(square_number)
    print()
    
def cube_number(start_number, stop_number):
    for x in range(start_number, stop_number):   
        cubed_number = x ** 3
        print(cubed_number)
    print()

main()
