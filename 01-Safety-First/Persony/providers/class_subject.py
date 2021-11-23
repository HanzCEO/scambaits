import random
from faker.providers import BaseProvider

subjects = [
	'Math', 'Al-Kimiyya', 'Alchemy', 'Medicine'
]

class ClassSubjectProvider(BaseProvider):
	def class_subject(self):
		return random.choice(subjects)
