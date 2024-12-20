def main():
    cost_meal = float(input("Cost of meal:"))

    tip_amount_15 = cost_meal * 0.15
    total_amount_15 = cost_meal + tip_amount_15
    print(f"Tip amount: {tip_amount_15:.2f}")
    print(f"Total amount: {total_amount_15:.2f}")

    tip_amount_20 = cost_meal * 0.20
    total_amount_20 = cost_meal + tip_amount_20
    print(f"Tip amount: {tip_amount_20:.2f}")
    print(f"Total amount: {total_amount_20:.2f}")

    tip_amount_25 = cost_meal * 0.25
    total_amount_25 = cost_meal + tip_amount_25
    print(f"Tip amount: {tip_amount_25:.2f}")
    print(f"Total amount: {total_amount_25:.2f}")
main()