def main():
    start_number = int(input("Start number: "))
    stop_number = int(input("Stop number: ")) + 1

    for x in range(start_number, stop_number):
        square_number =  x ** 2
        print(square_number)
        

    for x in range(start_number, stop_number):   
        cubed_number = start_number ** 3
        print(cubed_number)
    
main()
