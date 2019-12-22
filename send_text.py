# ------------------------------------------------------------------------
# This is the main 'driver' code for the whole program.  It first scrapes
# the web for the most recently read book.  It scrapes again.  If the two
# results differ, then a new book was read.  Kathryn's phone number is
# retrieved and a congratulatory text message is sent.  Lastly, the
# 'last_book' is updated to prevent repeated messages, and the program sleeps
# for 20 seconds.
#
# author: Ryan Hood
# email: ryanchristopherhood@gmail.com
# ------------------------------------------------------------------------


import phone_number
import boto3
import scraping
import time

MESSAGE = 'Congratulations On Reading Another Book.  Keep It Going!'

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

    if (current_last_book != new_last_book):
        # If not the same, a new book was read.  Get the phone number...
        phone_number = phone_number.KATHRYN_PHONE_NUMBER

        # ... and send the text message.
        client = boto3.client('sns')
        client.publish(PhoneNumber=phone_number, Message=MESSAGE)

        # Update the 'current_last_book' to avoid repeated messages.
        current_last_book = new_last_book

    # Sleep for a set amount of seconds.
    time.sleep(20)
