from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/front")
content = response.text
title_line = []
article_link = []

soup = BeautifulSoup(content, "html.parser")
title = soup.find_all(class_="storylink", name="a")
for data in title:
    line = data.getText()
    title_line.append(line)
    link_1 = data.get("href")
    article_link.append(link_1)

upvote = [score.getText() for score in soup.find_all(name= "span", class_ = "score")]

print(upvote)
print(title_line)
print(article_link)

