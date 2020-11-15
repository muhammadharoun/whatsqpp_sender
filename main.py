from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from time import sleep


# https://api.whatsapp.com/send?phone=+972599704270


class Sender:
    def __init__(self):
        global id_number
        id_number = int(input('Enter the id you want to start from : '))
        global finsh
        finsh = int(input('How many number u want to send msg : '))
        finsh += id_number



    def connect_database(slef,user,password):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="mydatabase"
        )
        global mycursor
        mycursor = mydb.cursor()

    def scan_qr(self):
        # chrome_options = webdriver.ChromeOptions()
        # prefs = {"profile.default_content_setting_values.notifications" : 2}
        # chrome_options.add_experimental_option("prefs",prefs)
        global driver
        _browser_profile = webdriver.FirefoxProfile()
        _browser_profile.set_preference("dom.webnotifications.enabled", False)
        driver = webdriver.Firefox(firefox_profile=_browser_profile)
        
        # driver = webdriver.Chrome('/home/msf/Desktop/whatsapp_sender/chromedriver',chrome_options=chrome_options) 
        
        
        
        driver.get("https://web.whatsapp.com/") 
        sleep(7)

    def open_chat(self,number):
        api_link = f'https://web.whatsapp.com/send?phone={number}'
        driver.get(api_link)
        sleep(0.2)
        driver.find_element_by_xpath('//*[@id="action-button"]')
        driver.click()
        sleep(0.1)
        driver.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a')
        driver.click()


    def send_message(self,message):
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        driver.send_keys(message)
        driver.submit()
        

    def read_database(self,id_number):
        mycursor.execute("SELECT * FROM customers")
        global myresult
        myresult = mycursor.fetchall()
        for i in myresult:
            if id_number in i:
                num = int(myresult.index(i))
        myresult = myresult[num:finsh]


if __name__ == "__main__":
    myresult = [(1,'+970599704270','sasdsssss')]

    test = Sender()
    test.scan_qr()
    for i in myresult:
        test.open_chat(i[1])
        test.send_message(i[2])

