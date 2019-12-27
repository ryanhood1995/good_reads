# ------------------------------------------------------------------------
# This script contains methods responsible for sending texts out.
#
# author: Ryan Hood
# email: ryanchristopherhood@gmail.com
# ------------------------------------------------------------------------

import phone_number
import boto3
import generate_message
import count_methods


def new_book_text():
    # Get the Phone Number.
    phone_number = phone_number.KATHRYN_PHONE_NUMBER

    # Get the message.
    message = generate_message.generate_full_message()

    # Send the text.
    client = boto3.client('sns')
    client.publish(PhoneNumber=phone_number, Message=message)

def new_years_text():
    # If this method gets called, then it must already have been determined that it's the New Year.
    # So do not check again.

    # Get the Phone Number.
    phone_number = phone_number.KATHRYN_PHONE_NUMBER

    # Generate the message.
    message = "Happy New Years!  This Year, You Have Read " + str(count_methods.get_count()) + " Books.  Now The Counter Will Be Reset.  Good Luck This Year!"

    # Send the text.
    client = boto3.client('sns')
    client.publish(PhoneNumber=phone_number, Message=message)
