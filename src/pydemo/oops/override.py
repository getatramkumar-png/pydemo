import os
os.system("cls")
class Parent:
	def show_message(self) -> None:
		print("Message from the parent class")


class Child(Parent):
	def show_message(self) -> None:
		#super().show_message()
		print("Message from the child class")


if __name__ == "__main__":
	parent = Parent()
	child = Child()

	parent.show_message()
	child.show_message()
