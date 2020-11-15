from selenium import webdriver 
from time import sleep
import mysql.connector



######################################################################
mydb = mysql.connector.connect(                                      #
host="localhost",                                                    #
user="root",                                                         #
password="",                                                         #
database="db1"                                                       #
)                                                                    # #                                                                    #
table_name = 'new'                                                   #
  				                                     # #                                                                    #
sleep_time = 4          # time between msg                           #
                                                                     #
######################################################################


class Sender:

    def __init__(self):
        global id_number
        id_number = int(input('Enter the id you want to start from : '))
        if id_number == 0 :
            id_number += 1
        global finsh
        finsh = int(input('How many number u want to send msg : '))
        finsh += id_number

    def scan_qr(self):
        global driver
        driver = webdriver.Firefox(executable_path='geckodriver.exe')  
        driver.get("https://web.whatsapp.com/") 
        sleep(5)

    def open_chat(self,number):
        api_link = 'https://web.whatsapp.com/send?phone={0}'.format(number)
        driver.get(api_link)
        sleep(0.2)

        
    def send_message(self,message):
        d = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        d.send_keys(message)
        sleep(0.2)
        d = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button/span')
        d.click()
        
        
    def read_database(self,id_number):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM {0}".format(table_name))
        global myresult
        myresult = mycursor.fetchall()
        for i in myresult:
            if id_number in i:
                num = int(myresult.index(i))
        myresult = myresult[num:finsh]
        return myresult

         
    def update_to_sucsess(self,number):
        mycursor = mydb.cursor()
        sql = "UPDATE {0} SET status_wp = 'sucsess' WHERE id = {1};".format(table_name,number)
        mycursor.execute(sql)
        mydb.commit()

    def update_to_field(self,number):
        mycursor = mydb.cursor()
        sql = "UPDATE {0} SET status_wp = 'field' WHERE id = {1};".format(table_name,number)
        mycursor.execute(sql)
        mydb.commit()

if __name__ == "__main__":
    test = Sender()
    myresult = test.read_database(id_number)
    test.scan_qr()
    for i in myresult:
        try:
            test.open_chat(i[2])
            sleep(2)
            test.send_message(i[3])
            test.update_to_sucsess(i[0])
            sleep(sleep_time)
        except:
            test.update_to_field(i[0])

