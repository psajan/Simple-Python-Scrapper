import requests
from bs4 import BeautifulSoup
import json
import re
import tkinter as tk

def get_consultancies():
    url = "https://ecan.org.np/members/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('section', attrs = {'class':'members many-blogs'}) 
    print(table)
    datas = []
    for consultancy in table.find_all("div", attrs={'class': 'member'}):
        name = consultancy.find("div", attrs={"class": "title mt-sm"}).text.strip()
        address = consultancy.find("div", attrs={"class": "address mb-md"}).text.strip()
        phone = ""
        rating = ""
        image = ""
        comments = ""
        location = consultancy.find("div", attrs={"class": "destination num mt-md"}).text.strip()        
        consultancyData = {
            "Name": name,
            "Address": address,
            "City": "",
            "Location": location,
            "Average Rating": rating,
            "Comments": comments,
            "Image": image,
            "Contact Number": phone
        }
        datas.append(consultancyData)
    
    # Save the list of dictionaries to a JSON file
    with open("consultancies.json", "w") as file:
        json.dump(datas, file, indent=4)
    print("Consultancies saved to consultancies.json")

# Create the UI
root = tk.Tk()
root.title("Educational Consultancies in Nepal")

button = tk.Button(root, text="Get Consultancies", command=get_consultancies)
button.pack(pady=10)

root.mainloop()
