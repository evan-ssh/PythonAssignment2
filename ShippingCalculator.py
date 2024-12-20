def main():
    cost_of_items = float(input("Cost of items ordered"))
    if cost_of_items >= 75.00:
        shipping_cost = 0
    elif cost_of_items < 75.00 and cost_of_items > 50 :
        shipping_cost = 9.95
    elif cost_of_items < 50 and cost_of_items > 30:
        shipping_cost = 7.95
    elif cost_of_items < 30:
        shipping_cost = 5.95
    else:
        print("Number must be greater than 0")
    
    
    
    print(f"Cost of items ordered: ")
    print(f"Shipping cost: ")
    print(f"Total cost: ")
