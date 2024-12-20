def main():
 while True:
    cost_of_items = float(input("Cost of items ordered: "))
    if cost_of_items >= 75.00:
        shipping_cost = 0
    elif cost_of_items < 75.00 and cost_of_items > 50 :
        shipping_cost = 9.95
    elif cost_of_items < 50 and cost_of_items > 30:
        shipping_cost = 7.95
    elif cost_of_items < 30 and cost_of_items > 0:
        shipping_cost = 5.95
    elif cost_of_items < 0:
        print("Must enter a positive number")
        continue

    total_cost = cost_of_items + shipping_cost
    
    print(f"Cost of items ordered: {cost_of_items:.2f}")
    print(f"Shipping cost: {shipping_cost:.2f}")
    print(f"Total cost: {total_cost:.2f}")
main()