# ------------------------------------------------------------------------
# This script contains methods responsible for maintaing the current book
# count.  count.txt is a file that contains a single line containing a single
# integer.  count.txt should be in the same directory as the project.
#
# author: Ryan Hood
# email: ryanchristopherhood@gmail.com
# ------------------------------------------------------------------------

def get_count():
    count_file = open(r"count.txt", "r")
    lines = count_file.readlines()
    current_count = int(lines[0])
    return current_count

def increment_count():
    # Set-up the file for reading.
    count_file_reading = open(r"count.txt", "r")
    lines = count_file_reading.readlines()
    current_count = int(lines[0])
    count_file_reading.close()

    # Set-up the file for overwriting.
    count_file_writing = open(r"count.txt", "w")
    count_file_writing.write(str(current_count+1))
    count_file_writing.close()

def restart_count():
    count_file = open(r"count.txt", "w")
    count_file.write("0")
    count_file.close()
