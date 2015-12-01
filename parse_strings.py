my_name = "Abla"
list(my_name)

string = "1,2,3,4,5"
my_list = []
for el in string.split(','):
	my_list.append(int(el))

print my_list

string = "One fish two fish red fish blue fish"
my_list = []
for item in string.split('fish'):
    my_list.append(item)

print my_list

