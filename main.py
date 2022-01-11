
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class Mylist(list):


	def __init__(self, list):
		self.list = list

	def getArray(self, array, output):
		for item in array:
			if isinstance(item, list):
				self.getArray(item, output)
			else:
				print(item)
				output.append(item)
		return output

	def __next__(self):
		output = []
		if len(self.list) == 0:
			raise StopIteration

		return self.getArray(self.list, output)

FlatIterator = Mylist(nested_list)
FlatIterator.__next__()

flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)




