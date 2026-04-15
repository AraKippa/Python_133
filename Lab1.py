
#***************************************************************
# Author: (Sam M)
# Lab: (Lab 1)
# Date: (4/14/2026)
# Description: Shopping list total calculator
# Input: taxRate, shipping cost, item cost
# Output: subtotal, tax, shipping, grand total
# Sources: Lab 1 specifications
#***************************************************************
## changed variables from mixed case to formal Python format

def main():
    tax_rate = 0.0
    shipping = 0.0
    total_cost = 0.0

    total_cost = get_item_costs()
    tax_rate, shipping = get_other_costs()
    print_receipt(total_cost, tax_rate, shipping)

    print("Thank you!")

# getItemCosts() prompts a user for a list of item
# costs and returns the sum
def get_item_costs():
    item_cost = 0.0
    total_cost = 0.0
    more = 'y'

    while more == 'y':
        item_cost = float(input("Enter item cost $ "))
        total_cost = total_cost + item_cost
        more = input("Do you have more items (y/n): ")

    return total_cost

# getOtherCosts() prompts a user for the tax rate
# and shipping costs and returns both inputs
def get_other_costs():
    tax_rate = 0.0
    shipping = 0.0

    tax_rate = float(input("\nEnter tax rate (i.e. .075 for 7.5%): "))
    shipping = float(input("Enter shipping costs $ "))

    return tax_rate, shipping
## re-ordered tax_rate and shipping to match run order

# printReceipt() accepts total cost, tax rate, and
# shipping costs and calculates and prints the tax
# amount, and total cost
def print_receipt(total_cost, tax_rate, shipping):
    print("\nSubtotal: $ ", format(total_cost, ".2f"))
    print("Tax: $", format((tax_rate * total_cost), ".2f"))
# added calc to calculate tax rate * subtotal to get total tax
    print("Shipping: $", format(shipping, ".2f"))
    print("------------------------")
    print("Please pay: $", format(total_cost + (tax_rate * total_cost) + shipping, ".2f"))
# added calc to calc total tax (tax rate * total cost) could be another function but trying to
# keep changes small

main()