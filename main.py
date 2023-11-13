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


# put the part below in a function or something so user can call multiple times
def get_netid_mgmt_info(id):
    # switch to netid mgmt tab
    driver.switch_to.window(mgmt)
    # waits for netID input box to be visible
    while len(driver.find_elements("id", 'netID')) < 1:
        continue

    # HTML input id is netID for box
    netID_box = driver.find_element("id", 'netID')
    # input netid argument, press enter. results should load
    netID_box.send_keys(id + Keys.ENTER)
    # make sure that LDAP Attributes are visible
    while len(driver.find_elements("id", 'row-netID')) < 1:
        continue
    # collect data
    return_string = "LDAP Attributes\n"
    return_string = return_string + driver.find_element("id", 'row-netID').text + "\n"
    return_string = return_string + driver.find_element("id", 'row-RcpID').text + "\n"
    return_string = return_string + driver.find_element("id", 'row-firstName').text + "\n"
    return_string = return_string + driver.find_element("id", 'row-lastName').text + "\n"
    return_string = return_string + driver.find_element("id", 'row-netidStatus').text + "\n"
    return_string = return_string + driver.find_element("id", 'row-passwordChangeDate').text + "\n"
    return_string = return_string + driver.find_element("id", 'lockAttr').text + "\n"
    return_string = return_string + driver.find_element("id", 'campusServiceAttr').text + "\n"
    return_string = return_string + driver.find_element("id", 'sorSource').text + "\n"
    return_string = return_string + driver.find_element("id", 'phi').text + "\n"
    return_string = return_string + driver.find_element("id", 'enrolled').text + "\n"
    return_string = return_string + driver.find_element("id", 'optedIn').text + "\n"
    return_string = return_string + driver.find_elements("id", 'optedIn')[1].text + "\n\n"
    return_string = return_string + "CAS Interrupt Service(CIS) Campaigns\n"
    return_string = return_string + driver.find_element("id", 'campaigns').text + "\n\n"
    return_string = return_string + "RAD Admin Attributes\n"
    return_string = return_string + driver.find_element("id", 'radAdminLdap').text + "\n"
    return_string = return_string + driver.find_element("id", 'radAdminRad').text + "\n"
    return_string = return_string + driver.find_element("id", 'radAdminLdap').text + "\n\n"
    return_string = return_string + "NetID Application Related data\n"
    return_string = return_string + driver.find_element("id", 'row-activationDate').text + "\n"
    return_string = return_string + driver.find_element("id", 'row-passwordChangeDate').text + "\n"
    return_string = return_string + driver.find_element("id", 'row-termsOfUse').text + "\n\n"
    return_string = return_string + "Security Questions and Answers\n"
    return_string = return_string + driver.find_element("id", 'row-netidHolder').text + "\n"
    return_string = return_string + driver.find_element("id", 'row-netidHolderEnrollment').text + "\n"
    return_string = return_string + driver.find_element("id", 'row-netidHolderOptIn').text + "\n"
    return_string = return_string + driver.find_element("id", 'row-netidHolderLocked').text + "\n"
    return_string = return_string + driver.find_element("id", 'row-netidLockoutDate').text + "\n\n"
    return_string = return_string + "Kerberos Status\n"
    return_string = return_string + driver.find_elements("id", 'row-netidLockoutDate')[1].text + "\n"
    return_string = return_string + driver.find_element("id", 'kerberos').text + "\n"
    # print statement here as test
    print(return_string)
    return return_string

if __name__ == '__main__':

    get_netid_mgmt_info("agk83")




