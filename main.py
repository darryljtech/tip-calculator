# Collect inputs for calculation
bill_total = input("What is the bill total?: \n")

split = input("How many people are splitting the tip?: \n")

percentage_tip = input("What percentage would you like to give?: \n")

# Calculate the percentage tip

tip_total = int(bill_total) * (int(percentage_tip) / 100)

final_tip = (round(tip_total, 2)) / float(split)

print(f"You each will pay {final_tip}")

