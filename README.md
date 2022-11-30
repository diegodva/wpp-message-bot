# wpp-message-bot
### Python bot utilized to automatically send personalized messages by whatsapp web utilizing Selenium web scraper. With cliclable link and emojis.

* To create a virtual env: `python -m venv venv`
* To activate the virtual env: `source venv/bin/activate`
* To install the dependencies: `pip install -r requirements.txt`
* Update the information on the csv file.
  * The phone number must have the DDI+DDD+Number as this example: 5511900000000
* Download the webdriver.
  * It is necessary to download the browser's web driver in the update you are using and save it on the same folder as the code. I used Google Chrome in my case.
  * Google Chrome Webdriver Dowload: https://chromedriver.chromium.org/downloads
  * (To check your Google Chrome version, go to Settings > Help > About Google Chrome).
* To run the code: `python wpp-message-bot.py`
