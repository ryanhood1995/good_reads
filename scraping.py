# ------------------------------------------------------------------------
# This file scrapes Kathryn Van Dinh's goodreads read-books feed.  It then
# gets the most recent book read and returns it.
#
# author: Ryan Hood
# email: ryanchristopherhood@gmail.com
# ------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup
from csv import writer

def get_most_recent_book():
    # Get the HTML for Kathryn's goodreads page.
    response = requests.get('https://www.goodreads.com/review/list/42742492-kathryn-van-dinh?shelf=read')

    # Create a BeautifulSoup object for 'response'
    soup = BeautifulSoup(response.text, 'html.parser')

    # 'class_ = 'value'' is the closest place in the HTML to the most recent book.
    posts = soup.find_all(class_ = 'value')

    # The actual value of the most recent book is at index 3.
    most_recent_book = posts[3].get_text()

    # The string is messy, so let's trim the new line characters and extra spaces.
    most_recent_book = most_recent_book.strip()
    return most_recent_book
