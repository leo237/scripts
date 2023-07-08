import random

## Experiment Settings -- Edit these numbers and see how the results change.
TOTAL_NUMBER_OF_PEOPLE_IN_ROOM = 23
NUMBER_OF_EPOCHS = 10000


## Other constants
MAX_DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Date:
	def __init__(self, day, month):
		self.day = day
		self.month = month

	def __eq__(self, that):
		if (self.day, self.month) == (that.day, that.month):
			return True
		return False

	def __hash__(self):
		'''
		Hash method that returns which day of the year it is, since Jan 01. 
		e.g Feb 1, will return 32 since it's the 32nd day of the year.
		'''
		return sum(MAX_DAYS_PER_MONTH[0:self.month -1]) + self.day

	def __repr__(self):
		'''
		Returns date in the MM/DD format. No, it's not because I'm in the US, 
		but because I prefer ISO 8601 format, but I'm not interested in the YYYY.
		'''
		return "{}/{}".format(self.month, self.day)

	@staticmethod
	def generate_random_date():
		'''
		Generates a random date.
		'''
		random_month = random.randint(1,12)
		random_day = random.randint(1, MAX_DAYS_PER_MONTH[random_month-1])
		return Date(random_day, random_month)



class BirthdayParadox:

	def __init__(self,total_number_of_people, epochs):
		self.total_number_of_people = total_number_of_people
		self.epochs = epochs

	def simulate_one_epoch(self):
		'''
		Generates 'n' random dates and finds out how many sets of common birthdays exist.
		'''
		list_of_people = [Date.generate_random_date() for _ in range(self.total_number_of_people)]
		common_birthdays = self.total_number_of_people - len(set(list_of_people))
		return common_birthdays

	def simulate(self):
		'''
		Runs the above method for 'x' epochs and calculates probability.
		Does not return anything. Prints the result.

		TODO: Can update to only perform simulation and the statistics can be potentially generated
		in another method. Not required right now.
		'''
		atleast_1_common_birthday = 0
		no_common_birthday = 0

		for i in range(self.epochs):
			common_birthdays = self.simulate_one_epoch()
			if common_birthdays >= 1:
				atleast_1_common_birthday +=1
			else:
				no_common_birthday +=1

		print(atleast_1_common_birthday/self.epochs)

BirthdayParadox(total_number_of_people=TOTAL_NUMBER_OF_PEOPLE_IN_ROOM, epochs=NUMBER_OF_EPOCHS).simulate()