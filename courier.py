# Ask user to input the packet price and distance (in kms) and store them in float data type.
package_price = float(input("Enter the price (in £): "))
distance = float(input("Please enter the total distance (in kms): "))

# Create different variables and store their prices appropriately.
# Delivery options
air = 0.36
freight = 0.25

# Insurance type
full_insurance = 50.00
limited_insurance = 25.00

# Gift type
gift = 15.00
no_gift = 0.00

# Priority type
priority = 100.0
standard_delivery = 20.00

# Ask user for their delivery preference out of air and freight options.
# Convert the input to lowercase and calculate the delivery price based on their chosen method and store it in
# respective variable with the help of conditional statements.
delivery_option = input("Please enter your delivery preference \n(Air / Freight): ")
if delivery_option.lower() == "air":
    delivery_price = air * distance
else:
    delivery_price = freight * distance

# Ask user for their insurance option out of full and limited options.
# Convert the input to lowercase and calculate the insurance price based on their chosen preference and store it in
# respective variable using conditional statements.
insurance_option = input("Please enter your insurance type \n(Full / Limited): ")
if insurance_option.lower() == "full":
    insurance_price = full_insurance
else:
    insurance_price = limited_insurance

# Ask user for their gift option out of gift and no gift options.
# Convert the input to lowercase and calculate the gift price based on their chosen preference and store it in
# respective variable using conditional statements.
gift_option = input("Please enter the gift type \n(Gift / No Gift): ")
if gift_option.lower() == "gift":
    gift_price = gift
else:
    gift_price = no_gift

# Ask user for their priority option out of priority and standard options.
# Convert the input to lowercase and calculate the priority price based on their chosen preference and store it in
# respective variable using conditional statements.
priority_option = input("Please enter your priority type \n(Priority / Standard): ")
if priority_option.lower() == "priority":
    priority_price = priority
else:
    priority_price = standard_delivery

# Calculate total by adding package price, delivery price, insurance price, gift price and priority price and print it.
total_cost = package_price + delivery_price + insurance_price + gift_price + priority_price
print(f"The total cost of package based on your selection is £{round(total_cost,2)} ")

