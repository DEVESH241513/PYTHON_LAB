# Input inventory of Store 1
n1 = int(input("Enter number of products in Store 1: "))
store1 = {}

for i in range(n1):
    product = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    store1[product] = quantity


# Input inventory of Store 2
n2 = int(input("\nEnter number of products in Store 2: "))
store2 = {}

for i in range(n2):
    product = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    store2[product] = quantity


# Input inventory of Store 3
n3 = int(input("\nEnter number of products in Store 3: "))
store3 = {}

for i in range(n3):
    product = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    store3[product] = quantity


# Display individual inventories
print("\nStore 1 Inventory:", store1)
print("Store 2 Inventory:", store2)
print("Store 3 Inventory:", store3)


# Merge inventories using dictionary comprehension
all_products = set(store1) | set(store2) | set(store3)

total_inventory = {
    product: store1.get(product, 0)
    + store2.get(product, 0)
    + store3.get(product, 0)
    for product in all_products
}


# Display merged inventory
print("\nMerged Inventory:")
for product, quantity in total_inventory.items():
    print(product, ":", quantity)


# Check a particular product
search_product = input("\nEnter product to search: ")

if search_product in total_inventory:
    print("Total stock of", search_product, "is",
          total_inventory.get(search_product, 0))
else:
    print("Product not found in inventory.")


# Update stock using dictionary update operator
extra_stock = {"Pen": 10}
total_inventory.update(extra_stock)

print("\nInventory after update:", total_inventory)