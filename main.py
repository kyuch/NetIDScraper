from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# leaves browser open after task completed
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#opens window, navigated to NetID Admin
driver.get("https://netid.rutgers.edu/adminAuthenticate.htm")
# switches to new tab, navigates to OR
driver.switch_to.new_window('tab')
driver.get("https://registry.rutgers.edu/viewCompletePerson.htm")