import requests
from random import choice 
from pyfiglet import figlet_format
from termcolor import colored 

progTitle = "JOKE GENERATOR    v1"
url = "https://icanhazdadjoke.com/search"


def asciiTitle(progName,color):
	title = figlet_format(progName)
	title = colored(title, color=color)
	print(title)

def getJSON(url, user_input):
		res = requests.get(
		url,
		headers={"Accept": "application/json"},
		params={"term": user_input}
	).json() 


		num_jokes = res["total_jokes"]
		results = res["results"]

		if num_jokes > 1:
			print(f"There are {num_jokes} jokes about {user_input}. Here's one: ")
			print(choice(results)["joke"])
		elif num_jokes == 1:
			print(f"There is only 1 joke about {user_input}")
			print(results[0]["joke"])
		else:
			print(f"Sorry, couldn't find a joke with your term {user_input}")


asciiTitle(progTitle,"blue")  

user_input = input("What would you like to search for? ")

getJSON(url, user_input)
