class Calculator:
	def add(self, first: int, second: int = 0, third: int = 0) -> int:
		return first + second + third

class Calculator22:
	def add(self, first: int, second: int = 0) -> int:
		return first + second

    
if __name__ == "__main__":
	a = Calculator22()

	print(a.add(5))
	print(a.add(5, 10))
	#print(a.add(5, 10, 15))
