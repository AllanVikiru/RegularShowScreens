# bot for scraping the screens

import os  # os module
import requests  # creates requests to web pages
from bs4 import BeautifulSoup  # downloading and parsing HTML content in web pages

# declaration of website with images
url = 'https://regularshowscreens.wordpress.com/'

# download page for parsing
page = requests.get(url)  # sends get request to web page
site = BeautifulSoup(page.text, 'html.parser')  # creating HTML for site requested

# locates all images with 'img' tag
images = site.findAll('img')

# create screens folder
if not os.path.exists('screens'):
    os.makedirs('screens')

# move to new directory
os.chdir('screens')

# image file numbers variable e.g. screen-0
x = 0

# write images
for image in images:
    try:
        url = image['src']  # extract source url for each image
        response = requests.get(url)  # send get request
        if response.status_code == 200:  # if response == OK
            with open('screen-' + str(x) + '.jpg', 'wb') as img:  # create new image file
                img.write(requests.get(url).content)  # write request content onto image file
                img.close()  # save file
                print("Got one!")
                x += 1
                # fetch 5 images
                if x == 5:
                    quit("Got 'em!")
    except Exception as e:
        quit(e)
        pass
