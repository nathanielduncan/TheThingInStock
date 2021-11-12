from selenium import webdriver
    #selenium is the API that allows me to open a browser, find a object in the HTML and check its content

from selenium import webdriver
    #webdriver makes it so that the browser version being used by selenium is compatible

from twython import Twython
    #twython is the API that goes between regular python and twitters API

import time
    #used for sleep.(seconds)

#Auth is a local python file defining my personal security keys for the twitter account this program posts to.
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

#Build the connection to the twitter API, using twython
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

#These can be changed to look for different things at different intervals
url = "https://www.bestbuy.com/site/pokemon-pokemon-tcg-celebrations-ultra-premium-collection/6473336.p?skuId=6473336"
        #URL above can be changed for whatever site we are looking at. Only works for BestBuy.com 
        #Ultra box: https://www.bestbuy.com/site/pokemon-pokemon-tcg-celebrations-ultra-premium-collection/6473336.p?skuId=6473336

refreshrate = int(60)
        #refreshrate above can be changed for how often (in seconds) the stauts will be checked.

geckoLocation = 'C:\\Users\crazy\OneDrive\Documents\Coding\StockBot\geckodriver.exe'
        #geckoLocation should be the file path to the corrsponding geckodriver
        #download the one for your system here: https://github.com/mozilla/geckodriver/releases



#open the browser
browser = webdriver.Firefox(executable_path=geckoLocation)
browser.get(url)


while True:
    elem = browser.find_element_by_class_name("fulfillment-add-to-cart-button")

    if elem.text == "Sold Out":
        print("Sold Out, do nothing")

    else:
        message = 'It is in stock! GO ==> ' + url
        twitter.update_status(status=message)
        print("In Stock, tweet sent")
        break

    time.sleep(refreshrate)
    browser.refresh()

