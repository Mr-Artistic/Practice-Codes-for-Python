buffet = ('Roti', 'Sabzi', 'Rice', 'Dal', 'Jalebi',)

print("\nOur restaurant offers the following items in the buffet:\n")
for menu in buffet:
    print(menu)

# Tuple cannot be changed --> buffet.append('Kheer')

buffet = ('Paratha', 'Sabzi', 'Rice', 'Dal', 'Gulab Jamun',)

print("\nOur restaurant has modified some items in the buffet, below is the final list:\n")
for menu in buffet:
    print(menu)