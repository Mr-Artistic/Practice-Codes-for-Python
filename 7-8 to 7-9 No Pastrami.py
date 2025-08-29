sandwich_orders = ['pastrami', 'cheese', 'butter', 'pastrami', 'ghee', 'mayo', 'pastrami']
finished_sandwiches = []

if 'pastrami' in sandwich_orders:
    print("\nSorry, we have ran out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while finished_sandwiches != sandwich_orders:
    if  sandwich_orders == []:
        break
    item = sandwich_orders.pop()
    finished_sandwiches.append(item)
    print(f"I am preparing your '{item} sandwich'")

print(f"\nThe following sandwiches were made:\n")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} Sandwich")