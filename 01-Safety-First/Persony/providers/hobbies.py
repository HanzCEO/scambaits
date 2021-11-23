import random
from faker.providers import BaseProvider

hobbies = [
	'football', 'gaming', 'e-sport', 'swimming', 'fishing', 'cleaning', 'tidying', 'cooking', 'cycling',
	'motorcycling', 'skateboarding', 'soccer', 'badminton', 'camping', 'hiking', 'running'
]

class HobbyProvider(BaseProvider):
	def hobby(self):
		return random.choice(hobbies)
