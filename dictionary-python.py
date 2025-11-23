laptop = {"brand": "Apple", "model": "MacBook Pro", "price": 2022, "is_stoke": True}
laptop["price"] = 2023
laptop["color"] = "Space Gray"
print(laptop)
for key, value in laptop.items():
    print(key, ":", value)
