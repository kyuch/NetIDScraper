from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# leaves browser open after task completed
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://netid.rutgers.edu/adminAuthenticate.htm")
"""
this will not work -- it does not open a new window/tab,
it just changes the website of current window
"""
driver.get("https://registry.rutgers.edu/viewCompletePerson.htm")