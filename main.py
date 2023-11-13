from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
# leaves browser open after task completed
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# opens window, navigated to NetID Admin
driver.get("https://netid.rutgers.edu/adminAuthenticate.htm")
# mgmt is the name of the NetID management tab
mgmt = driver.current_window_handle
# switches to new tab, navigates to OR
driver.switch_to.new_window('tab')
driver.get("https://registry.rutgers.edu/viewCompletePerson.htm")
# reg is the name of the OR tab
reg = driver.current_window_handle
driver.switch_to.window(mgmt)


# put the part below in a function or something so user can call multiple times
def get_netid_mgmt_info(id):
    # waits for netID input box to be visible
    while(len(driver.find_elements("id", 'netID')) < 1):
        continue

    # HTML input id is netID for box
    netID_box = driver.find_element("id", 'netID')
    # input netid argument, press enter. results should load
    netID_box.send_keys(id + Keys.ENTER)


if __name__ == '__main__':

    get_netid_mgmt_info("agk83")




