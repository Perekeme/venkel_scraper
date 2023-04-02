from selenium import webdriver
import pickle
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_experimental_option('detach', True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=options)
browser.get("https://www.venkel.com/")
cookies = pickle.load(open("cookies.pkl", "rb"))
# browser.delete_all_cookies()
for cookie in cookies:
    try:
        browser.add_cookie(cookie)
    except Exception as e:
        print(e)
browser.maximize_window()    # to maximise window because of login button


# browser.refresh()


_user_Email = "israelmensah92@gmail.com"
_user_Password = "perekeme123"


""""
        excellll
"""

excel_file = "Venkel Scraper - Input Sample.xlsx"
df_excel = pd.read_excel(excel_file)
df_excel_query = df_excel["Query"]
# print(df_excel_query)

listt = df_excel_query.tolist()
# print(listt)

""""
        excellll
"""

button_element = WebDriverWait(browser, 50).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div[1]/div/div[2]/div[2]/div[1]/div/div/ul/li[5]/a')))

_login = browser.find_element(
    By.XPATH, '//*[@id="header"]/div[1]/div/div[2]/div[2]/div[1]/div/div/ul/li[5]/a')
_login.click()
# debug  print("login clicked" )

_input_email = browser.find_element(By.ID, 'email')
# browser.implicitly_wait(10)
_input_password = browser.find_element(By.ID, 'pass')
# browser.implicitly_wait(10)
_login2 = browser.find_element(By.ID, 'send2')
# browser.implicitly_wait(10)
# debug  print(_input_id)
# debug  print(_input_password)

# to login as a user
_input_email.send_keys(_user_Email)
_input_password.send_keys(_user_Password)
_login2.click()
time.sleep(15)


# cookies = browser.get_cookies()
# pickle.dump(cookies, open("cookies.pkl","wb"))

# cookies = pickle.load(open("cookies.pkl","rb"))
# # browser.delete_all_cookies()
# for cookie in cookies:
#     try:
#         browser.add_cookie(cookie)
#     except Exception as e:
#         print(e)
# cookies = pickle.load(open("cookies.pkl", "rb"))
# # the reason that I delete the cookies is because I found duplicated cookies by inspect the cookies with browser like step 2
# browser.delete_all_cookies()

# for cookie in cookies:
#     browser.add_cookie(cookie)


# browser.implicitly_wait(10)
# debug print(_login2)

# # Wait for login process to complete.
# WebDriverWait(driver=browser, timeout=10).until(
#     lambda x: x.execute_script("return document.readyState === 'complete'")
# )
# # Verify that the login was successful.
# error_message = "Incorrect username or password."
# # Retrieve any errors found.
# errors = browser.find_elements(By.CLASS_NAME, "flash-error")

# # When errors are found, the login will fail.
# if any(error_message in e.text for e in errors):
#     print("[!] Login failed")
# else:
#     print("[+] Login successful")
# # Close the drive


# get_url = browser.current_url
# updated_url = get_url[:23]
# updated_url = "https://www.venkel.com/catalogsearch/result/?q={0}".format(item)

# get_url = "https://www.venkel.com/C0201X6S160-104KNP"
# print(get_url)
# browser.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS)
# https://www.venkel.com/C0201X6S160-104KNP
# C0201X6S160-104KNP


# _input_search = browser.find_element(By.ID, 'search')
# _search_btn = browser.find_element(By.CLASS_NAME, 'search-button')
# _input_search.send_keys("C0201X6S160-104KNP")
# _search_btn.click()


# for item in listt:
#     updated_url = "https://www.venkel.com/catalogsearch/result/?q={0}".format(item)
# print("about to move t o next page")
browser.get("https://www.venkel.com/C0201X6S160-104KNP")
# print("moved to next page")

# time.sleep(120)
button_element2 = WebDriverWait(browser, 200).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'product-collateral')))  # you should only use classname, using xpath will cause errors

# print(button_element2)
# detail=[]
try:
#     table1=  browser.find_element(
#         By.CLASS_NAME, 'table-bordered')
#     print(table1)

#     rows= table1.find_elements(By.TAG_NAME,"tr")
#     print(rows)

#     for row in rows:
#         detail.append(row.find_element(By.XPATH,"./td").text)
#     print(detail)    

    part_number = browser.find_element(
        By.XPATH, '//*[@id="product_addtocart_form"]/div[5]/table/tbody/tr[1]/td').text
    description = browser.find_element(
        By.XPATH, '//*[@id="product_addtocart_form"]/div[5]/table/tbody/tr[2]/td').text
    qty_avail = browser.find_element(
        By.XPATH, '//*[@id="product_addtocart_form"]/div[5]/table/tbody/tr[3]/td').text
    reel_size = browser.find_element(
        By.XPATH, '//*[@id="product_addtocart_form"]/div[5]/table/tbody/tr[4]/td').text
    moq = browser.find_element(
        By.XPATH, '//*[@id="product_addtocart_form"]/div[5]/table/tbody/tr[5]/td').text
    standard_lead = browser.find_element(
        By.XPATH, '//*[@id="product_addtocart_form"]/div[5]/table/tbody/tr[6]/td').text

    print(f'{part_number} \n {description}\n {qty_avail}\n {reel_size}\n {moq}\n {standard_lead}')
except Exception as e:
    print(e, "Main Error")
