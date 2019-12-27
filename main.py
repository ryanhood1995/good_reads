# ------------------------------------------------------------------------
# This is the main 'driver' code for the whole program.  It first scrapes
# the web for the most recently read book.  It scrapes again.  If the two
# results differ, then a new book was read.  Kathryn's phone number is
# retrieved and a congratulatory text message is sent.  Lastly, the
# 'last_book' is updated to prevent repeated messages, and the program sleeps
# for 20 seconds.
#
# Also, at each iteration it is checked if a a new year has elapsed and reacts
# accordingly.
#
# author: Ryan Hood
# email: ryanchristopherhood@gmail.com
# ------------------------------------------------------------------------

import scraping
import time
import send_text
import count_methods
import time_methods

# --------------------------------------------
# ------------------MAIN----------------------
# --------------------------------------------

# Get the most recent book read before infinite loop is entered.
current_last_book = scraping.get_most_recent_book()
while True:
    print("Checking goodreads for a new book")

    # Get the most recent book read.  On first iteration, it will be identical
    # to 'last_book'.
    new_last_book = scraping.get_most_recent_book()


    # Check to see if a new book was read.
    if (current_last_book != new_last_book):
        # If a new book was read, send a text, update the count, and update current last book read.
        print("New book was read.  Sending text, updating count, and updating last book read.")
        send_text.new_book_text()
        count_methods.increment_count()
        current_last_book = new_last_book



    # Check to see if it is a new year.
    if (time_methods.is_new_year()):
        # If it is a new year, start by send a text and restart the count.
        print("It is a New Year.  Sending text and restarting count.")
        send_text.new_years_text()
        count_methods.restart_count()



    # Sleep for a set amount of seconds.
    time.sleep(20)
