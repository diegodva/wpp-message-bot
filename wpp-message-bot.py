# Packages Import
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
from datetime import datetime
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException

# Declare standard message as variable.
standard_msg = '''
Hello, {name}.

Take part in our Opinion Survey and help us understand how we can improve and also what we are doing really well!

Link: {link}

🚨 *Tip:* In case you are unable to click on the link, save our number and then click on the link. 😉

If you have already answered this survey, please disregard this message.
'''

#Read the csv file and transform in a DataFrame.
mailing_df = pd.read_csv('CSV_Example_File.csv')

# Create a Selenium Webdriver.
browser = webdriver.Chrome(executable_path='chromedriver.exe')

# Determines the page the browser will access.
browser.get('https:///web.whatsapp.com/')

# Validation every 1 second if the QR code has been scanned.
while len(browser.find_elements_by_id('side')) < 1:
    time.sleep(1)

# Creates a dictionary with the same mailing information, but with a sending log column.
send_log = {'email':[],'name_all':[],'name':[],'phone':[],'link':[], 'send_log':[]}

# Sending loop for the number of indexes in the mailing.
for i in mailing_df.index:
    # Turns worksheet row information into variables.
    email = mailing_df.loc[i, 'email']
    name_all = mailing_df.loc[i, 'name_all']
    name = mailing_df.loc[i, 'name']
    mobile = mailing_df.loc[i, 'phone']
    message_link =  mailing_df.loc[i, 'link']
    
    try:
        # Personalize the message with the name, link and encode the message to urllib.
        standard_msg_temp = urllib.parse.quote(standard_msg.format(name=name, link=message_link))

        # Opens the conversation link with the phone with the message already written.
        link = f'https://web.whatsapp.com/send?phone={mobile}&text={standard_msg_temp}'
        browser.get(link)

        # Validation every 1 second if the page has loaded.
        while len(browser.find_elements_by_id('side')) < 1:
            time.sleep(3)

        time.sleep(2)
        # Send the message.a
        browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').send_keys(Keys.ENTER)
        # Records the information used in the shipment and the time of shipment.
        send_log['email'].append(email)
        send_log['name_all'].append(name_all)
        send_log['name'].append(name)
        send_log['phone'].append(mobile)
        send_log['link'].append(message_link)
        send_log['send_log'].append('SENT AT: '+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        # Wait 10 seconds before repeating the process with the information on the next line.
        time.sleep(10)
        
    # Records the error if fail the send attempt (incorrect number, etc).
    except NoSuchElementException:
        send_log['email'].append(email)
        send_log['name_all'].append(name_all)
        send_log['name'].append(name)
        send_log['phone'].append(mobile)
        send_log['link'].append(message_link)
        send_log['send_log'].append('ERROR! '+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div').send_keys(Keys.ENTER)

browser.close()


# Creates a dictionary with the same mailing information, but with a sending log column.
send_log = {'email':[],'name_all':[],'name':[],'phone':[],'link':[], 'send_log':[]}

# Sending loop for the number of indexes in the mailing.
for i in mailing_df.index:
    # Turns worksheet row information into variables.
    email = mailing_df.loc[i, 'email']
    name_all = mailing_df.loc[i, 'name_all']
    name = mailing_df.loc[i, 'name']
    mobile = mailing_df.loc[i, 'phone']
    message_link =  mailing_df.loc[i, 'link']
    # Personalize the message with the name, link and encode the message to urllib.
    standard_msg_temp = urllib.parse.quote(standard_msg.format(name=name, link=message_link))
    print(standard_msg_temp)

# Declares the log shipping dictionary as a DataFrame.
send_log_df = pd.DataFrame.from_dict(send_log)

# Declaring as path variable that the files will be saved
user_path = 'C:/Users/diego/Downloads/'

# Defines the path and saves the log of submissions by wpp
datetime_stamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
send_log_filepath = Path(f'{user_path}send_log_wpp_{datetime_stamp}.csv')
send_log_filepath.parent.mkdir(parents=True, exist_ok=True)
send_log_df.to_csv(send_log_filepath, index=False)