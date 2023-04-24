from bs4 import BeautifulSoup
import requests
import json

def get_lessons(day, start, end):
  lessons = []
  for i in range(start, end):
    if i == start:
      lesson = " ".join(trs[i].find_all("td")[28].text.split())
    else:
      lesson = " ".join(trs[i].find_all("td")[27].text.split())
    lessons.append(lesson)
  print(day)
  print("\n".join(lessons))
  print()
  return lessons

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-Qk-0tbwz8BbZ9OZsLk3fJHOny7cs491VQanDGnNq_06fMFlvr2WNb6D7am6KCQ73BMyCWMk66kdU/pubhtml"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
all_rows = soup.find_all("tbody")

trs = all_rows[0].find_all("tr")
group = trs[4].find_all("td")[27].text

data = {}

lessons = get_lessons(trs[5].find_all("td")[0].text, 5, 9)
data[trs[5].find_all("td")[0].text] = lessons

lessons = get_lessons(trs[9].find_all("td")[0].text.strip(), 9, 13)
data[trs[9].find_all("td")[0].text.strip()] = lessons

lessons = get_lessons(trs[13].find_all("td")[0].text.strip(), 13, 17)
data[trs[13].find_all("td")[0].text.strip()] = lessons

lessons = get_lessons(trs[17].find_all("td")[0].text.strip(), 17, 21)
data[trs[17].find_all("td")[0].text.strip()] = lessons

lessons = get_lessons(trs[21].find_all("td")[0].text.strip(), 21, 25)
data[trs[21].find_all("td")[0].text.strip()] = lessons

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

with open("data.txt", "w", encoding="utf-8") as f:
    for key, value in data.items():
        f.write(key + ":\n")
        f.write("\n".join(value) + "\n\n")