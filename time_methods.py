# ------------------------------------------------------------------------
# This script contains methods responsible for keeping track of time.  It is also
# capable of updating a day_and_month.txt file which is in the same directory.
#
# author: Ryan Hood
# email: ryanchristopherhood@gmail.com
# ------------------------------------------------------------------------

from datetime import date

# A simple method which returns a list with the current day and month.
def get_day_and_month():
    today = date.today()
    month = str(today.month)
    day = str(today.day)
    return [day, month]

# This method compares an old date with a new date to determine if it has been a new year recently.
def is_new_year():
    # First step is to get the up-to-date date.
    new_day_and_month = get_day_and_month()

    # Next step is to get the old date.
    date_file = open(r"day_and_month.txt", "r")
    old_day_and_month = date_file.read().splitlines()

    # Now, we see if the old date is 12/31 and the new date is 01/01.  If so, it is a new year.
    if (new_day_and_month == ['1', '1'] and old_day_and_month == ['31', '12']):
        return True
    return False

# This method updates the day_and_month.txt file with the most up to date version.
def update_old_day_and_month():
    current_day_and_month = get_day_and_month()
    current_day = current_day_and_month[0]
    current_month = current_day_and_month[1]

    date_file = open(r"day_and_month.txt", "w")
    date_file.write(current_day)
    date_file.write("\n")
    date_file.write(current_month)
