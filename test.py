from bs4 import BeautifulSoup


with open('home.html') as file:
    content = file.read()
    
    
soup = BeautifulSoup(content, 'lxml')

first_h5_tags = soup.find('h5') # finds 1st h5 tag
h5_tags = soup.find_all('h5')
#print(h5_tags)

for tag in h5_tags:
    tagss = (tag.text)
    
courses = soup.find_all('div', class_="card")
for course in courses:
    name = course.h5.text
    price = course.a.text.split()[-1]
    print(f"{name}:{price}")    

