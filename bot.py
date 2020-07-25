from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

def amountOfAccounts():
    amount = int(input("How many accounts? "))
    accounts = []
    for i in range(amount):
       account = input("Whats the account name? ")
       accounts.append(account)
    return accounts

class InstaBot:
    def __init__(self, username, password):
        self.bot = webdriver.Chrome(ChromeDriverManager().install())
        self.username = username
        self.password = password
        self.bot.get("https://www.instagram.com")
    def login(self):
        bot = self.bot
        bot.implicitly_wait(5)
        usernameInput = bot.find_element_by_name("username")
        usernameInput.send_keys(self.username)
        passwordInput = bot.find_element_by_name("password")
        passwordInput.send_keys(self.password)
        passwordInput.submit()
        bot.implicitly_wait(5)
        saveSubmit = bot.find_element_by_class_name("A086a")
        saveSubmit.submit()
        time.sleep(5)

    def likePosts(self,accounts):
        bot = self.bot
        time.sleep(10)
        print(accounts)
        for i in range(len(accounts)):
            bot.get("https://www.instagram.com/"+accounts[i])
            for k in range(3):
                bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
            posts = bot.find_elements_by_class_name("_9AhH0")
            print(len(posts))
            for m in range(len(posts)):
                posts[m].click()
                time.sleep(1)
                like = bot.find_element_by_class_name("fr66n")
                like.click()
                webdriver.ActionChains(bot).send_keys(Keys.ESCAPE).perform()
# MAIN
print("Login into instagram \n")
username = input("username: ")
password = input("password: ")

accounts = amountOfAccounts()
print(accounts)

ptr = InstaBot(username, password)
ptr.login()
ptr.likePosts(accounts)