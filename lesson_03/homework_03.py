# Заданий текст з книги "Аліса в країні чудес"
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

print("=== Task 01 ===")
print(alice_in_wonderland)

print("\n=== Task 02 ===")
single_quote_positions = [pos for pos, char in enumerate(alice_in_wonderland) if char == "'"]
print("Positions of single quotes:", single_quote_positions)

print("\n=== Task 03 ===")
print(alice_in_wonderland)


# task 04
blacksea = 436402
azovsea = 37800
togethersea = blacksea + azovsea
print("\n=== Task 04 ===")
print("Task 04 answer:", togethersea)

# task 05
total_storage = 375291
storage1_2 = 250449
storage2_3 = 222950
storage3 = total_storage - storage1_2
storage2 = storage2_3 - storage3
storage1 = storage1_2 - storage2

print("\n=== Task 05 ===")
print("Task 05 answers:")
print("Storage 1:", storage1)
print("Storage 2:", storage2)
print("Storage 3:", storage3)

# task 06
month_pay = 1179
total_month = 18
laptop_price = month_pay * total_month
print("\n=== Task 06 ===")
print("Task 06 answer:", laptop_price)

# task 07
answers_task_07 = [
    8019 % 8,
    9907 % 9,
    2789 % 5,
    7248 % 6,
    7128 % 5,
    19224 % 9
]
print("\n=== Task 07 ===")
print("Task 07 answers:", answers_task_07)

# task 09
photos = 232
photos_per_page = 8
pages_needed = photos // photos_per_page
if photos % photos_per_page > 0:
    pages_needed += 1

print("\n=== Task 09 ===")
print("Task 09 answer:", pages_needed)

# task 10
distance_km = 1600
fuel_per_100km = 9
tank_capacity = 48

fuel_needed = (distance_km / 100) * fuel_per_100km
refills_needed = fuel_needed // tank_capacity
if fuel_needed % tank_capacity > 0:
    refills_needed += 1

print("\n=== Task 10 ===")
print("Task 10 answers:")
print("Fuel needed:", fuel_needed, "liters")
print("Refills needed:", int(refills_needed))

print("test")