
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class Mylist(list):

	def __iter__(self):
		return self

	def __next__(self):
		if len(self) == 0:
			raise StopIteration

		return self.pop()

FlatIterator = Mylist(nested_list)
FlatIterator.reverse()
for item in FlatIterator:
	for key in item:
		print (key)
