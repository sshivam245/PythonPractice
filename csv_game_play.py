import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictReader
base_url = "https://quotes.toscrape.com"

def read_quotes(filename):
    with open(filename, "r")as file:
        csv_reader=DictReader(file)
        return list(csv_reader)


def start_game(quotes):
    quote = choice(quotes)
    remaning_guesses = 4
    print("here is a quote:")
    print(quote["text"])
    #print(quote["author"])
    guess = ""
    while guess.lower() != quote["author"].lower() and remaning_guesses>0: 
        guess = input(f"who said this quote? :chances remaning:   {remaning_guesses} \n")
        if guess.lower() == quote["author"].lower():
            print("you got it right")
            break
        remaning_guesses -=1
        if remaning_guesses ==3:
            res= requests.get(f"{base_url}{quote['bio-link']}")
            soup = BeautifulSoup(res.text,"html.parser")
        #   birth_date = soup.find(class_="author-born-date").get_text()
        # birth_place = soup.find(class_="author-born-location").get_text()
            print(f"try again ")

        elif remaning_guesses==2:
            print(f"here is a hint : the author first name starts with: {quote['author'] [0]}")
        elif remaning_guesses==1:
            last_initial = quote['author'].split(" ")[1][0]
            print(f"here is a hint : the author last name starts with: {last_initial}")
        else:
            print("sorry!!! ran out of guesses. the answer was {quote['author']}")

    again = ''
    while again.lower() not in ('y','yes','n','no'):
        again = input("would you like to play again (y/n)?")
    if again.lower() in ('yes', 'y'):
        return start_game(quotes)
    else:
        print("goooood byeeee ")

quotes = read_quotes ("quotes.csv")
start_game(quotes)
