from bs4 import BeautifulSoup
import requests 
import time

def find_jobs():
    content = requests.get("https://duunitori.fi/tyopaikat?haku=python").text
    soup = BeautifulSoup(content, 'lxml')
    #print(content)
    domain = "https://duunitori.fi"

    count = 0
    jobs = soup.find_all('a', class_= 'job-box__hover gtm-search-result')
    for job in jobs: 
        company = job['data-company']
        link_to = job['href']
        description = job.text
        address = domain + link_to
        print(f"{company}---{description}\n{address}\n\n")
        count += 1
    print(f"Total openings: {count}")

if __name__ == "__main__":
    while True:
        find_jobs()
        minutes = 1
        print(f"Waiting  10 seconds...")
        time.sleep(minutes*60)