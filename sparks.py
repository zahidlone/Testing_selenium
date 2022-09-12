from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

opt = Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=opt, executable_path="C:\Program Files (x86)\chromedriver.exe")
driver.get("https://www.thesparksfoundationsingapore.org/")



# checking for logo
logo = driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/img')
if (logo.is_displayed()):
    print("logo is displayed")
else:
    print("logo is not visible")

#checking for title
try:
    assert 'The Sparks Foundation' in driver.title
    print('Title is present')
except:
    print('Title is absent')

time.sleep(2)

#checking for navbar
navbar = driver.find_element_by_tag_name('nav')
if (navbar.is_displayed()):
    print("navbar is displayed")
else:
    print("navbar is not visible")

time.sleep(2)

#join_us_page
join_us = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[5]/a')
join_us.click()
time.sleep(3)

why_join_us = driver.get('https://www.thesparksfoundationsingapore.org/join-us/why-join-us/')
time.sleep(3)

name = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]')
email = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]')
role = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/select')
time.sleep(4)

# Scroll
driver.execute_script("arguments[0].scrollIntoView();", name)
time.sleep(4)

name.send_keys('Zahid Hussain Lone')
time.sleep(4)

email.send_keys('zahid@07')
time.sleep(4)

choose = Select(role)
choose.select_by_visible_text('Student')
time.sleep(4)

#checking for about_us page
about_us = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[1]/a')
time.sleep(3)
vision = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[1]/ul/li[1]/a')

actions = ActionChains(driver)
actions.move_to_element(about_us).click().move_to_element(vision).click().perform()
time.sleep(8)

#checking for programs
program = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[3]/a')
mentor = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[3]/ul/li[2]/a')

actions = ActionChains(driver)

actions.move_to_element(program).click().move_to_element(mentor).click().perform()
time.sleep(9)

driver.execute_script("window.scrollBy(0,600)", "")
time.sleep(10)

cls = driver.close()