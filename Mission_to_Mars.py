# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
# We are searching to elements with a specific combo of tag div and attribute list_text
#Secondly we are telling our browser to wait one second beofre searching for components
browser.is_element_present_by_css('div.list_text', wait_time=1)


html = browser.html
news_soup = soup(html, 'html.parser')
#Slide_elem is the variable assigned to look for the div tag and all the nested element insideit 
#div.list_text selects div tag with the class of list_text
#The select_one, the first matching element returned will be a list element with a class of slide and all elements in it
slide_elem = news_soup.select_one('div.list_text')


#Searching for article title
#Asking our slide_elem variable to find specific info of context title under div
slide_elem.find('div', class_='content_title')


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
#Using find instead of find all to get the first one since there are many article_teaser_body elements
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images
# 


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# Find the relative image url
#'img' is the tag with a class of 'fancybox-image' and get the link inside these tags
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base URL to create an absolute URL
# This includes the base url plus the link for the most recent image in the cell above
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Table Data from Mars Facts Website

# Creating a DF from the HTML table. the read_html specifically searches for tables and the index of 0 means to pull the first instance
df = pd.read_html('https://galaxyfacts-mars.com')[0]
# this specifies the columns
df.columns=['description', 'Mars', 'Earth']
# this specifies that description is the first column
df.set_index('description', inplace=True)
df


# In order to keep the updated html data as the website refreshes, we have this html ready code
df.to_html()


#This tells the automated browsing system to stop
browser.quit()


