from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from splinter import Browser
import time
import pymongo

def scrape():
    #!which chromedriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest/'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    title=soup.find(class_='content_title').text.strip()
    teaser=soup.find(class_='article_teaser_body').text.strip()


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars/'
    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')
    result=None
    while result is None:
        try:
            browser.click_link_by_partial_text('more info')
            result='Positive'
        except:
            pass
    time.sleep(3)
    html=browser.html
    soup = bs(html, 'html.parser')
    result=None
    while result is None:
        try:
            browser.click_link_by_partial_href('largesize')
            result='Positive'
        except:
            pass
    html=browser.html
    soup = bs(html, 'html.parser')
    featured_image_url = soup.body.img['src']


    url= "https://twitter.com/MarsWxReport?lang=en"
    browser.visit(url)
    time.sleep(3)
    html=browser.html
    soup = bs(html, 'html.parser')
    pretweets=soup.find_all('span', class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
    notyet=None
    x=0
    while notyet is None:
        try:
            if pretweets[x].text.strip().split()[0]=="InSight":
                mars_weather=pretweets[x].text.strip()
                notyet='Positive'
        except:
            pass
        x=x+1


    url='https://space-facts.com/mars/'
    browser.visit(url)
    html=browser.html
    soup=bs(html, 'html.parser')
    contents=soup.find('table', class_='tablepress tablepress-id-p-mars').find_all('td',class_='column-1')
    values=soup.find('table', class_='tablepress tablepress-id-p-mars').find_all('td',class_='column-2')
    d={}
    col_1=[]
    col_2=[]
    for x in range(len(contents)):
        col_1.append(contents[x].text.strip())
        col_2.append(values[x].text.strip())
    d['Description']=col_1
    d['Value']=col_2
    dhtml=pd.DataFrame.from_dict(d)
    dhtml=dhtml.to_html(index=False)


    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    hemisphere_image_urls=[]
    hems=['Valles Marineris','Cerberus','Schiaparelli','Syrtis Major']
    for i in hems:
        browser.click_link_by_partial_text(i)
        hemisphere_image_urls.append({'title':i+ ' Hemisphere','img_url':browser.find_by_text('Sample')['href']})
        browser.back()

    browser.quit()
    
    results_dict={
        'news':{
            'title':title,
            'teaser':teaser
        },
        'feat_img':featured_image_url,
        'weather':mars_weather,
        'html_table':dhtml,
        'hemisphere_img':hemisphere_image_urls
    }

    return results_dict
