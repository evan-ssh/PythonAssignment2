def main():
 while True:
    start_number = int(input("Start number: "))
    stop_number = int(input("Stop number: ")) + 1
    if start_number > stop_number:
       print("Start number cannot be greater than stop.")
       continue
    else:
        square_number(start_number, stop_number)
        cube_number(start_number, stop_number)
    

def numbers():
   pass        

    
def square_number(start_number, stop_number):
    for x in range(start_number, stop_number):
        square_number =  x ** 2
        print(square_number)
    
def cube_number(start_number, stop_number):
    for x in range(start_number, stop_number):   
        cubed_number = x ** 3
        print(cubed_number)
    

main()
