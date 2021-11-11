import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")

url_list=[]
#getting all the urls
with open ('testupdates.csv') as urls:
    for url in urls:
        # create driver object
        driver = webdriver.Chrome(options=chrome_options)
        time.sleep(1)
        # asses webpage
        driver.get("https://"+url.rstrip())
        time.sleep(1)
        driver.maximize_window()
        # accept cookies, if applicable
        try:
            driver.find_element_by_id('acceptAllButton').click()
            time.sleep(1)
        except:
            print('probably accepted the cookie already!')
        driver.execute_script("document.body.style.zoom='20%'")
        scroll_pause_time = 0.3
        screen_height = driver.execute_script("return window.screen.height;")   
        i = 1

        while True:
            driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
            i += 1
            time.sleep(scroll_pause_time)
            scroll_height = driver.execute_script("return document.body.scrollHeight;")  
            if (screen_height) * i > scroll_height:
                break
        time.sleep(1)
        try: 
            title = driver.title
        except: 
            title = ''
        try: 
            update_count2 = len(driver.find_elements_by_css_selector('div.eventcalendar_CalendarRow_398u2'))
        except: 
            update_count2 = ''
            
        url = {'title': title, 'update_count2': update_count2
                }
        url_list.append(url)
        driver.quit()
df = pd.DataFrame(url_list)

#Save data
df.to_csv('testupdatesdata.csv', index = False, encoding='utf-8')
print('Finished!')


