# my_name = "Abla"
# list(my_name)

# string = "1,2,3,4,5"
# my_list = []
# for el in string.split(','):
# 	my_list.append(int(el))

# print my_list

# string = "One fish two fish red fish blue fish"
# my_list = []
# for item in string.split('fish'):
#     my_list.append(item)

# print my_list

str = "item:apples,quantity:4,price:1.50\n"
split_str = str.split(",")
print split_str

quantity_list = split_str[1].split(":")
print quantity_list
print quantity_list[1]
quantity = int(quantity_list[1])

amount_list = split_str[2].split(":")
print amount_list
price = amount_list[1].strip() 
print price

price_float = float(price)

print price_float
print price_float*quantity
