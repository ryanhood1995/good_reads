# ------------------------------------------------------------------------
# This script contains methods responsible for constructing the message
# that will be sent over text.
#
# author: Ryan Hood
# email: ryanchristopherhood@gmail.com
# ------------------------------------------------------------------------

import random
import count_methods

MESSAGE_LIST = ['Congratulations On Reading Another Book!', "You're Doing Great So Far!", 'Keep It Going!',
                "There's Not Enough Books In The World For You!", 'Oh Look. Kathryn Read Another Book!',
                "You're A BookWorm!"]

# This method chooses a random message from the above list and returns it.
def generate_first_part():
    random_int = random.randint(0, len(MESSAGE_LIST)-1)
    first_part = MESSAGE_LIST[random_int]
    return first_part

# This method combines one half of the message from the above method and adds the running count of
# books read this year.  The final message is returned.
def generate_full_message():
    first_part = generate_first_part()
    final_message = first_part + "  You Have Read " + str(count_methods.get_count()) + " Books This Year."
    return final_message
