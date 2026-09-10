""" Abstraction hides implementation details and exposes only the operations that an object must provide. In Python, abstraction is commonly implemented with the abc module: 
1. ABC is the base class for an abstract class. 
2. @abstractmethod marks a method that child classes must implement. 
3. An abstract class cannot be instantiated directly.
 4. A concrete child class can be instantiated only after implementing every abstract method.
 The caller can use the common send() operation without knowing how an email or SMS is delivered.
   Each child class handles its own implementation details. """

import os
os.system("cls")

from abc import ABC ,abstractmethod


class Notification(ABC):
	"""Define the common contract for every notification type."""

	@abstractmethod
	def send(self, message: str, recipient: str) -> None:
		"""Send a message using the notification provider."""
		raise NotImplementedError

	def log(self, message: str) -> None:
		"""A normal method shared by all notification types."""
		print(f"Notification logged: {message}")


class EmailNotification(Notification):
	def send(self, message: str, recipient: str) -> None:
		self.log(message)
		print(f"Email sent to {recipient}: {message}")


class SmsNotification(Notification):
	def send(self, message: str, recipient: str) -> None:
		self.log(message)
		print(f"SMS sent to {recipient}: {message}")


def notify(notification, message: str, recipient: str) -> None:
	"""Use the abstraction without depending on a specific child class."""
	notification.send(message, recipient)


if __name__ == "__main__":
	# Notification() would raise TypeError because it is abstract.
	email = EmailNotification()
	sms = SmsNotification()

	notify(email, "Your order has shipped", "ram@example.com")
	notify(sms, "Your verification code is 1234", "+91-9876543210")
