products = {
    "car items": [
        {"name": "car cover", "price": 1200, "stock": 5},
        {"name": "car perfume", "price": 250, "stock": 10},
        {"name": "car washer", "price": 500, "stock": 3}
    ],
    "school items": [
        {"name": "notebook", "price": 50, "stock": 100},
        {"name": "pen", "price": 10, "stock": 200}
    ]
}


print(" 1st prgram ") # Display the price of each product
for category, items in products.items():
    print("\n", category)
    for product in items:
        print(product["name"], "- ₹", product["price"])


print("2nd prgra") # Display the price of each product
for items in products.values():
    for product in items:
        if product["stock"] < 5:
            product["stock"] = 20

print("\nStock Updated")


print("3rd program") # Write a function to calculate the total store valuation
total = 0
for items in products.values():
    for product in items:
        total += product["price"] * product["stock"]

print("Total Store Value = ₹", total)

print("4th program")
keyword = "car"

for items in products.values():
    for product in items:
        if keyword in product["name"]:
            print("\nFound Product")
            print(product)


print("5th program") #  category with the highest total value
highest_category = ""
highest_value = 0

for category, items in products.items():
    value = 0

    for product in items:
        value += product["price"] * product["stock"]

    if value > highest_value:
        highest_value = value
        highest_category = category

print("\nHighest Value Category:", highest_category)
print("Value = ₹", highest_value)