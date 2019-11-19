import requests
from bs4 import BeautifulSoup
import os
from time import sleep
import random
from random import randint

default_name_for_file = "agents.txt"
counter = 0
content = []

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
      if random.randrange(num): continue
      line = aline
    return line


def file_open(ff):
    try:
        with open(ff, "r") as f:
            user_a_h = (random_line(f)).rstrip()
            return user_a_h

    except EnvironmentError:
        print("[ ERR ]: Probably trying to open file that doesn't exist")
        return False


def scrapper(url): # Edit this code for scrapping multiple pages
    try:
        r = my_session.get(url, timeout=7)
        html_content = r.text
        html_soup = BeautifulSoup(html_content, 'html.parser')

        a = html_soup.find()
        # Your Code HERE


    except Exception as e:
        print(e)
        return False


user_agent = file_open(default_name_for_file)
if user_agent == False:
    print("[ ERR ]: Please set right file path/name and try again")

else:
    my_session = requests.Session()
    my_session.headers.update({'User-Agent':user_agent})
    print(my_session.headers)

    while True:
        if counter == randint(50, 150):
            user_agent = file_open(default_name_for_file)
            print("")
            print("[INFO] Changing User-Agent")
            my_session.headers.update({'User-Agent':user_agent})
            print(f"[INFO] Changed User-Agent to: {my_session.headers}")
            print("")

            print("")
            print("[INFO] Changing IP")
            os.system("torghost switch")
            sleep(randint(15, 20))
            counter = 0

        scrapped_page = scrapper(url)
        if scrapped_page == False:
            continue

        content.append(scrapped_page)
        counter += 1
        # Your Code HERE
