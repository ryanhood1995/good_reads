# The purp[ose of this file is to run main.py repeatedly so that if a crash occurs, the program restarts.

from subprocess import Popen

filename = r'C:\Users\User\Data_Science_Projects\good_reads_scraping\main.py'
while True:
    print("\nStarting " + filename)
    p = Popen("python " + filename, shell=True)
    p.wait()
