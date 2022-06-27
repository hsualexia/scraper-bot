# Scraping Bot
Scraping tool using Selenium to retrieve instagram users' followers

# How to use:
_*Tested with Chrome & 5k followers_
_**Ensure that your laptop does not go into sleep mode when this bot is running_
_***If you would like to repeat the scrape for an existing user, please remove existing user.csv_
1. Clone repository into specific directory, navigate to directory
2. Install requirements using terminal or command line. You should run this command ```pip install -r requirements.txt```.
3. Open run.py using a text editor and replace the 14th and 15th lines with your Instagram username and password (your personal account is not recommended).
4. Open a terminal or cmd again and run the bot using this command: ```python run.py```.
5. Enter the username of the person whose followers you want to scrape.

# What can be added upon request:
1. Check for repeated handles if the same targeted user has been scrapped again
2. Implement a safe stop
3. Reconsider how to handle larger number of followers
4. Implement to rename duplicated file names

#### Adapted from https://github.com/redianmarku/instagram-follower-scraper
