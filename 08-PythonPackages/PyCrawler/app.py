import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")
print(type(questions[0]))
print(type(questions[0].attrs))
print(type(questions[0]["id"]))
print(type(questions[0].get("id", 0)))
print(type(questions[0].select(".question-hyperlink")))
# get the title of first quesion
print(type(questions[0].select_one(".question-hyperlink").getText()))

# get all the questions:
for question in questions:
    print(type(question.select_one(".question-hyperlink").getText()))
    print(question.select_one(".vote-count-post").getText())
