import faker
import random, string

from faker_music import MusicProvider
from providers import *

class Struct:
	def __init__(self, **entries):
		self.__dict__.update(entries)

nl = '\n'
fake_providers = [MusicProvider, HobbyProvider, FoodProvider, GameProvider, ClassSubjectProvider]
months = [
	'january', 'february', 'march', 'april',
	'may', 'june', 'july', 'august',
	'september', 'october', 'november', 'december'
]

def main():
	print("Defaults to en_US")
	localization = input("Localization: ") or 'en_US'
	fake = faker.Faker(localization)

	# Time to add some custom providers
	for provider in fake_providers:
		fake.add_provider(provider)

	profile = Struct(**fake.profile())

	print(f"""
PERSONAL DETAIL
==============================
Full Name : {profile.name}
Address   : {padLeft(profile.address)}
Residence : {padLeft(profile.residence)}
Birth     : {profile.birthdate}
Gender    : {'Male' if profile.sex == 'M' else 'Female'}

ADMINISTRATION DETAIL
==============================
SSN       : {profile.ssn}
Blood Type: {profile.blood_group}
Job       : {profile.job}
Company   : {profile.company}
Lcn. Plate: {fake.license_plate()}

INTERNET LIFE
==============================
Websites  : {(nl + (' ' * 12)).join(profile.website)}
Email     : {profile.mail}
Dis. Email: {generateDisposableEmail(profile.username)}
Username  : {profile.username}
Password  : {generatePassword()}
IPv4      : {fake.ipv4_public()}
IPv6      : {fake.ipv6()}
MAC       : {fake.mac_address()}
UUID      : {fake.uuid4()}

SOCIALS
==============================
Phone No. : +{fake.msisdn()}

FAVORITES
==============================
Color     : {camelToSpace(fake.color_name())}
Number    : {random.randint(0, 31)}
Month     : {months[random.randint(0, 11)].title()}
Food      : {fake.food()}
Desert    : {fake.desert()}
Game      : {fake.game()}
Class Subj: {fake.class_subject()}
Hobby     : {fake.hobby().title()}
Music Genr: {fake.music_genre_object()['genre']}
Music Inst: {random.choice(fake.music_instrument_object()['instruments'])}

FINANCE
==============================
VISA      : {padLeft(fake.credit_card_full('visa').split(nl)[2:])}
Mastercard: {padLeft(fake.credit_card_full('mastercard').split(nl)[2:])}
Discover  : {padLeft(fake.credit_card_full('discover').split(nl)[2:])}
ISBN-10   : {fake.isbn10()}
ISBN-13   : {fake.isbn13()}
IBAN      : {fake.iban()}
BBAN      : {fake.bban()}
SWIFT     : {fake.swift(11)}
Main SWIFT: {fake.swift(11, primary=True)}
""")

def generatePassword():
	letters = string.ascii_letters + string.punctuation
	return ''.join([random.choice(letters) for i in range(18)])

def generateDisposableEmail(pre):
	domains = ['1secmail.com', '1secmail.org', '1secmail.net']
	atdomain = '@' + random.choice(domains)

	pre = list(pre)
	random.shuffle(pre)
	pre = ''.join(pre)

	return ''.join([random.choice(string.ascii_lowercase) for i in range(3)]) + pre + atdomain

def padLeft(str):
	if type(str) is list:
		return (nl + (' ' * 12)).join(str)
	return str.replace(nl, nl + (' ' * 12))

def camelToSpace(str):
	for i in range(len(str)):
		if str[i] >= 'A' and str[i] <= 'Z' and str[i-1] != ' ':
			# Insert space and let the capital letter
			str = str[:i] + ' ' + str[i:]

	# Remove first space and done!
	return str[1:]

if __name__ == '__main__': main()
