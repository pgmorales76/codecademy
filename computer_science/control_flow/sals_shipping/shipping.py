# Allowing the user to input the package weight.
while True:
    try:
        package_weight = float(input("Enter the weight of your package, in pounds: "))
        if package_weight > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

"""
def print_shipping_cost(method, cost):
    print(f"Cost for {method}: ${{cost:.2f}}\n")
# Then call print_shipping_cost('Ground Shipping', cost_for_ground_shipping)
"""

# Ground Shipping
if package_weight <= 2:
  cost_for_ground_shipping = package_weight * 1.5 + 20
  print("Cost for Ground Shipping, when package weighs", package_weight, "pounds:", "${:.2f}".format(cost_for_ground_shipping), end='\n\n')
elif (package_weight > 2) and (package_weight <= 6):
  cost_for_ground_shipping = package_weight * 3 + 20
  print("Cost for Ground Shipping, when package weighs", package_weight, "pounds:", "${:.2f}".format(cost_for_ground_shipping), end='\n\n')
elif (package_weight > 6) and (package_weight <= 10):
  cost_for_ground_shipping = package_weight * 4 + 20
  print("Cost for Ground Shipping, when package weighs", package_weight, "pounds:", "${:.2f}".format(cost_for_ground_shipping), end='\n\n')
else:
  cost_for_ground_shipping = package_weight * 4.75 + 20
  print("Cost for Ground Shipping, when package weighs", package_weight, "pounds:", "${:.2f}".format(cost_for_ground_shipping), end='\n\n')

# Ground Shipping Premium
cost_for_ground_shipping_premium = 125.00
print("Cost for Ground Shipping Premium:", "${:.2f}".format(cost_for_ground_shipping_premium), end='\n\n')

# Drone Shipping
if package_weight <= 2:
  cost_for_drone_shipping = package_weight * 4.5
  print("Cost for Drone Shipping, when package weighs", package_weight, "pounds:", "${:.2f}".format(cost_for_drone_shipping), end='\n\n')
elif (package_weight > 2) and (package_weight <= 6):
  cost_for_drone_shipping = package_weight * 9
  print("Cost for Drone Shipping, when package weighs", package_weight, "pounds:", "${:.2f}".format(cost_for_drone_shipping), end='\n\n')
elif (package_weight > 6) and (package_weight <= 10):
  cost_for_drone_shipping = package_weight * 12
  print("Cost for Drone Shipping, when package weighs", package_weight, "pounds:", "${:.2f}".format(cost_for_drone_shipping), end='\n\n')
else:
  cost_for_drone_shipping = package_weight * 14.25
  print("Cost for Drone Shipping, when package weighs", package_weight, "pounds:", "${:.2f}".format(cost_for_drone_shipping), end='\n\n')

# Cheapest shipping method
cheapest = min(cost_for_ground_shipping, cost_for_ground_shipping_premium, cost_for_drone_shipping)
if cheapest == cost_for_ground_shipping:
    print("The cheapest option is Ground Shipping: ${:.2f}".format(cheapest), end='\n\n')
elif cheapest == cost_for_ground_shipping_premium:
    print("The cheapest option is Ground Shipping Premium: ${:.2f}".format(cheapest), end='\n\n')
else:
    print("The cheapest option is Drone Shipping: ${:.2f}".format(cheapest), end='\n\n')
