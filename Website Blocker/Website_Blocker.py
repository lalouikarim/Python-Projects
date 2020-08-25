import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path  = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites_list =["facebook.com", "www.facebook.com", "www.youtube.com", "youtube.com"]

start_working_hour = dt(dt.now().year, dt.now().month, dt.now().day, 13)
finish_working_hour = dt(dt.now().year, dt.now().month, dt.now().day, 17)

while True:
    if start_working_hour < dt.now() < finish_working_hour:
        print("Working Hours")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in websites_list:
                if website not in content:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Fun hours")
        '''
        #my method:
        with open(hosts_temp, "r") as file:
            content = file.readlines()
            with open("hosts_tmp", "w") as tmp_file:
                for line in content:
                    if line[10:len(line)-1]  not in websites_list:
                        tmp_file.write(line)
        with open("hosts_tmp", "r") as tmp_file:
            content = tmp_file.readlines()
            with open(hosts_temp, "w") as file:
                for line in content:
                    file.write(line)
        '''
        #a better method:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
