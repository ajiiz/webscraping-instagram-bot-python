from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstaBot:
    def __init__(self, name, surname, email, username, password):
        self.bot = webdriver.Chrome()
        self.fullName = str(name + " " + surname)
        self.email = email
        self.username = username
        self.password = password
    def register(self):
        bot = self.bot
        bot.get("https://instagram.com/")

password = "Asdfg12345"
username = "Hi there"
email = "eddd@yahhoo.com"
name = "eddy"
surname = "hunden"
ptr = InstaBot(name, surname, email, username, password)
ptr.register()



