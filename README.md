# TheThingInStock
A Twitter bot that tweets when that item goes in stock.

This program currently looks at BestBuy.com, one product at a time, to see if it is in stock. It checks every minute, and sends a tweet when it is in stock.

auth.py should contain the security keys that are connected to the twitter account that is to be posted to. My twitter account keys are not uploaded to this file. They will need to be replaced with your keys to run.

To run, geckodriver will need to be downloaded to your system. Be sure to get the version that matches for your system.
	There is a variable in StockBot.py called geckoLocation that needs to contain a string fo the file location of geckodriver.exe.