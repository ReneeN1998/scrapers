import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--window-position=0,0")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-gpu")

 
url_list=[]
#getting all the urls
with open ('15d.csv') as urls:
    for url in urls:
        # create driver object
        driver = webdriver.Chrome("/home/test/chromedriver",options=chrome_options)
        time.sleep(3)
        # asses webpage
        driver.get("https://"+url.rstrip())
        driver.maximize_window()
        time.sleep(10)
        # accept cookies, if applicable
        try:
            driver.find_element_by_id('acceptAllButton').click()
            time.sleep(2)
        except:
            print('probably accepted the cookie already!')
        # Get through the agecheck
        try:
            day = driver.find_element_by_id('ageDay')
            month = driver.find_element_by_id('ageMonth')
            year = driver.find_element_by_id('ageYear')
            day.send_keys('10')
            month.send_keys('April')
            year.send_keys('2000')
            time.sleep(1)
            link = driver.find_element_by_css_selector('a.btnv6_blue_hoverfade.btn_medium')
            link.click()
            print('Age check passed')
        except:
            print('No age restriction')
        time.sleep(2)
        try: 
            title = driver.find_element_by_xpath('.//*[@id="appHubAppName"]').text
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
            number_recent_reviews = driver.find_element_by_xpath('//*[@id="review_histogram_recent_section"]/div[1]/div/span[2]').text
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
            number_alltime_reviews = driver.find_element_by_xpath('//*[@id="review_histogram_rollup_section"]/div[1]/div/span[2]').text
        except: 
            number_alltime_reviews = ''
        
        try:
            link3 = driver.find_element_by_css_selector('div.partnereventwebrowembed_LatestUpdateButton_1TRFt')
            link3.click()
            time.sleep(3) 
            downbutton = driver.find_element_by_css_selector('div.apppartnereventspage_ScrollButton_1t_97.apppartnereventspage_Down_3VePR.apppartnereventspage_AnimIn_240i5')
            actions = ActionChains(driver)
            actions.click(downbutton)
            time.sleep(3)
            for i in range(1000):
                actions.perform()
            downbutton = ''
            update_count = len(driver.find_elements_by_css_selector('div.apppartnereventspage_PartnerEvent_1KsYS.partnereventdisplay_InLibraryView_3_SEi'))
        except: 
            update_count = ''
          
        url = {'title': title, 'price1': price1, 'price2': price2, 'discountprice':discountprice,
                'free': free,
                'alltime_reviews_summary': alltime_reviews_summary, 
                'number_alltime_reviews': number_alltime_reviews,
                'developer': developer, 'publisher': publisher,
                'recent_review_summary': recent_review_summary, 
                'number_recent_reviews': number_recent_reviews, 
                'genre': genre,
                'release_date': release_date, 
                'tags': tags, 'update_count': update_count
                }
        url_list.append(url)
        driver.quit()
df = pd.DataFrame(url_list)

#Save data
df.to_csv('15d_games.csv', index = False, encoding='utf-8')
print('Finished!')
