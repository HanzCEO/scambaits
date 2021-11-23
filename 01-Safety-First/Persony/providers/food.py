import random
from faker.providers import BaseProvider

foods = [
	'noodle', 'satay', 'bread', 'chocolate', 'burger', 'hotdog', 'chicken nugget', 'bacon',
	'artificial chicken nugget', ''
]

deserts = {
	'ingredients': [
		'strawberry', 'milk', 'orange'
	],
	'implementations': [
		'cocktail', 'juice', 'dragon breath', 'cup'
	]
}

drinks = []

vegetables = []

class FoodProvider(BaseProvider):
	def food(self):
		return random.choice(foods)

	def desert(self):
		ingredients = random.choice(deserts['ingredients'])
		implementations = random.choice(deserts['implementations'])
		return (ingredients + ' ' + implementations).title()

	def drink(self):
		return random.choice(drinks)

	def vegetable(self):
		return random.choice(vegetables)
