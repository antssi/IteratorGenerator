nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

def generator(new_list):
	for k in new_list:
		for i in k:
			yield i

my_generator = generator(nested_list)

for i in my_generator:
	print(i)