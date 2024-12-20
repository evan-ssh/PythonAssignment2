def main():

    number_of_cents = int(input("Enter number of cents (0-99): "))
    quarters = number_of_cents // 25
    money_left = number_of_cents - 25 * quarters
    print(money_left)
    dimes = money_left // 10
    money_left = money_left - 10 * dimes
    print(money_left)

    nickles =  money_left // 5
    money_left = money_left - 5 * nickles
    print(money_left)
    pennies = money_left // 1

    print(quarters)
    print(dimes)
    print(nickles)
    print(pennies)

main()
    