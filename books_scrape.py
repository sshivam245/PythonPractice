from multiprocessing import connection
import sqlite3
from tkinter.tix import INTEGER
import requests
from bs4 import BeautifulSoup


def scrape_books(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    books = soup.find_all("article")
    all_books = []
    for book in books:
       books_data = (get_title(book),get_price(book),get_rating(book))
       all_books.append(books_data)
    save_books(all_books)

def save_book(all_books):
    connection = sqlite3.connect("books.db")
    c = connection.cursor()
    c.execute(''' CREAT TABLE books
        (title TEXT,price REAL, rtings INTEGER)''')
    c.executemany("INSERT INTO books VALUES(?,?,?)", all_books)
    connection.commit()
    connection.close()

def get_title(book):
    return book.find("h3").find("a")["title"]

def get_price(book):
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("£","").replace("Â",""))

def get_rating(book):
    ratings = {"zero":0 , "one":1, "two":2, "three":3, "four":4, "five":5}
    para = book.select(".star-rating")[0]
    rating = para.get_attribute_list("class")[-1]
    return ratings[rating]

scrape_books("http://books.toscrape.com/catalogue/category/books/history_32/index.html")







