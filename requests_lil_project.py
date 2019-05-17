import requests
import random  # use randint(a, b) to generate a random number between a and b
import pyfiglet

header = pyfiglet.figlet_format("DAD JOKES 3000!")
print(header)

topic = input("Hey, sup!? Do you wanna hear a joke?\nType in a topic:  ")

url = "https://icanhazdadjoke.com/search"

# response = requests.get(url)
# response = requests.get(url, headers={"Accept": "text/plain"})
response = requests.get(
						url, 
						headers = {"Accept" : "application/json"},
						params = {"term" : topic}
						)

data = response.json()
length = len(data["results"])

if length >= 1:
	number = random.randint(0, length-1)

if length == 0:
	print(f"Sorry, I don't have any joke about {topic}. Better lucky next time.")
elif length == 1:
	print(f"OK, I have one joke about it. Here it goes:\n\t-->> {data['results'][0]['joke']}")
else:
	print(f"Alright, I have {length} jokes about {topic}.\nHere's one of them: \n\t-->> {data['results'][number]['joke']}")
# 	for joke in data["results"]:
# 		print(f"\t-->> {joke['joke']}")