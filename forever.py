from subprocess import Popen

filename = r'C:\Users\User\Data_Science_Projects\good_reads_scraping\send_text.py'
while True:
    print("\nStarting " + filename)
    p = Popen("python " + filename, shell=True)
    p.wait()
