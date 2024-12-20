def main():
    start_number = int(input("Start number: "))
    stop_number = int(input("Stop number: ")) + 1
    square_number(start_number, stop_number)
    cube_number(start_number, stop_number)
    
        

    
def square_number(start_number, stop_number):
    for x in range(start_number, stop_number):
        square_number =  x ** 2
        print(square_number)
    
def cube_number(start_number, stop_number):
    for x in range(start_number, stop_number):   
        cubed_number = x ** 3
        print(cubed_number)
    

main()
