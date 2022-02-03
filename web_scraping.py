import requests
from bs4 import BeautifulSoup
from csv import writer

response=requests.get(" https://www.rithmschool.com/blog")
print(response.text)
soup=BeautifulSoup(response.text, "html.parser")
articles=soup.find_all("article")

with open("blog_data.csv", "w") as csv_files:
    csv_writter= writer(csv_files)
    csv_writter.writerow(["title", "link", "date"])
    for articles in articles:
        a_tag = articles.find("a")
        title= a_tag.get_text()
        url= (a_tag['href'])
        date = articles.find("time")["datetime"]
        csv_writter.writerow([title, url, date])