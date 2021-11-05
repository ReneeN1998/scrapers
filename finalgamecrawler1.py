import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
 
url_list=[]
#getting all the urls
with open ('testlinks10.csv') as urls:
    for url in urls:
        # create driver object
        driver = webdriver.Chrome("/home/test/chromedriver", options=chrome_options)
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
        # Get through the agecheck
        try:
            day = driver.find_element_by_id('ageDay')
            month = driver.find_element_by_id('ageMonth')
            year = driver.find_element_by_id('ageYear')
            day.send_keys('10')
            month.send_keys('februari')
            year.send_keys('2000')
            time.sleep(1)
            link = driver.find_element_by_link_text('Pagina weergeven')
            time.sleep(1)
            link.click()
        except:
            print('No age restriction')
    
        time.sleep(1)
        try: 
            title = driver.find_element(By.XPATH('.//*[@id="appHubAppName"]').text
        except:
            title = ''
        try: 
            price1 = driver.find_element_by_xpath('./html/body/div[1]/div[7]/div[5]/div[1]/div[3]/div[1]/div[5]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[1]').text
        except: 
            price1 = ''
        try: 
            price2 = driver.find_element_by_xpath('.//*[@id="game_area_purchase_section_add_to_cart_355119"]/div[2]/div/div[1]').text
        except:
            price2 = ''
        try: 
            discountprice = driver.find_element_by_xpath('/\.//*[@id="game_area_purchase"]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div').text
        except: 
            discountprice = ''
        try:
            free = driver.find_element_by_xpath('./html/body/div[1]/div[7]/div[5]/div[1]/div[3]/div[1]/div[5]/div[2]/div[1]/div[1]/div[2]/div/div[1]').text
        except:
            free = ''
        try:
            developer = driver.find_element_by_xpath('.//*[@id="developers_list"]/a').text
        except: 
            developer = ''
        try:
            publisher = driver.find_element_by_xpath('.//*[@id="game_highlights"]/div[1]/div/div[3]/div[4]/div[2]/a').text
        except: 
            publisher = ''
        try: 
            recent_review_summary = driver.find_element_by_xpath('.//*[@id="userReviews"]/div[1]/div[2]/span[1]').text
        except: 
            recent_review_summary = ''
        try: 
            number_recent_reviews = driver.find_element_by_xpath('.//*[@id="userReviews"]/div[1]/div[2]/span[2]').text
        except:
            number_recent_reviews = ''
        try: 
            genre = driver.find_element_by_xpath('.//*[@id="genresAndManufacturer"]').text
        except:
            genre = ''
        try: 
            release_date = driver.find_element_by_xpath('.//*[@id="game_highlights"]/div[1]/div/div[3]/div[2]/div[2]').text
        except: 
            release_date = ''
        try: 
            tags = driver.find_element_by_xpath('.//*[@id="glanceCtnResponsiveRight"]/div[2]/div[2]').text
        except: 
            tags = ''
        try: 
            alltime_reviews_summary = driver.find_element_by_xpath('.//*[@id="userReviews"]/div[2]/div[2]/span[1]').text
        except: 
            alltime_reviews_summary = ''
        try: 
            number_alltime_reviews = driver.find_element_by_xpath('.//*[@id="userReviews"]/div[2]/div[2]/meta[1]').text
        except: 
            number_alltime_reviews = ''
        try: 
            link2 = driver.find_element_by_xpath('//*[@id="tabletGrid"]/div[1]/div[5]/div[2]/div[4]/div/div[2]/div[2]')
            link2.click()
            time.sleep(1) 
            downbutton = driver.find_element_by_xpath('.//*[@id="tabletGrid"]/div[1]/div[5]/div[2]/div[4]/div/div[1]/div/div/div/div[1]/div/div/div[3]')
            actions = ActionChains(driver)
            actions.click(downbutton)
            for i in range(1500):
                actions.perform()
            downbutton = ''
            update_count = len(driver.find_elements_by_css_selector('div.apppartnereventspage_PartnerEvent_1KsYS.partnereventdisplay_InLibraryView_3_SEi'))
            close_button = driver.find_element_by_xpath('//*[@id="tabletGrid"]/div[1]/div[5]/div[2]/div[4]/div/div[1]/div/div/div/div[1]/div/div/div[1]')
            close_button.click()
        except:
            update_count = ''
        try:
            link3 = driver.find_element_by_css_selector('div.partnereventwebrowembed_LatestUpdateButton_1TRFt')
            link3.click()
            time.sleep(1) 
            downbutton = driver.find_element_by_css_selector('div.apppartnereventspage_ScrollButton_1t_97.apppartnereventspage_Down_3VePR.apppartnereventspage_AnimIn_240i5')
            actions = ActionChains(driver)
            actions.click(downbutton)
            for i in range(1500):
                actions.perform()
            downbutton = ''
            update_count2 = len(driver.find_elements_by_xpath('div.apppartnereventspage_PartnerEvent_1KsYS.partnereventdisplay_InLibraryView_3_SEi'))
        except: 
            update_count2 = ''
               
        url = {'title': title, 'price1': price1, 'price2': price2, 'discountprice':discountprice,
                'free': free,
                'alltime_reviews_summary': alltime_reviews_summary, 
                'number_alltime_reviews': number_alltime_reviews,
                'developer': developer, 'publisher': publisher,
                'recent_review_summary': recent_review_summary, 
                'number_recent_reviews': number_recent_reviews, 
                'genre': genre,
                'release_date': release_date, 
                'tags': tags, 'update_count': update_count, 'update_count2': update_count2
                }
        url_list.append(url)
        driver.close()
df = pd.DataFrame(url_list)

#Save data
df.to_csv('firstgames.csv', index = False, encoding='utf-8')



    
