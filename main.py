from selenium import webdriver
import os

NAME = "mark"
MAIL = "mark@mark.com"
PASSWORD = "!234Qwer"
IMAGE = os.getcwd()+"/3673909.jpg"



def registration_screen(driver):
    # Press on button "כניסה| הרשמה"
    driver.find_element_by_xpath("//li[@data-ember-action='636']").click()
    # Press on button "להרשמה"
    driver.find_element_by_class_name("text-btn").click()
    # Enter first name
    driver.find_element_by_xpath("//input[@type = 'text']").send_keys(NAME)
    # Enter email
    driver.find_element_by_xpath("//input[@data-parsley-type ='email']").send_keys(MAIL)
    # Enter password
    driver.find_element_by_id("valPass").send_keys(PASSWORD)
    # Enter password again
    driver.find_element_by_xpath("//input[@data-parsley-equalto ='#valPass']").send_keys(PASSWORD)
    # Press on radio button "אני מסכים"
    checkbox_element = driver.find_element_by_xpath("//input[@type = 'checkbox']")
    driver.execute_script("arguments[0].click();", checkbox_element)
    # Press button "הרשמה..."
    driver.find_element_by_xpath("//button[@type = 'submit']").click()

def login_screen(driver):
    # Press on button "כניסה| הרשמה"
    driver.find_element_by_xpath("//li[@data-ember-action='636']").click()
    # Enter email
    driver.find_element_by_xpath("//input[@data-parsley-type ='email']").send_keys(MAIL)
    # Enter password
    driver.find_element_by_xpath("//input[@type ='password']").send_keys(PASSWORD)
    # Press on button "BUYME-כניסה ל"
    driver.find_element_by_xpath("//button[@type = 'submit']").click()

def home_screen(driver):
    # Pick a price
    driver.find_element_by_link_text("סכום").click()
    driver.find_element_by_xpath("//li[@data-option-array-index='3']").click()
    # Pick a area
    driver.find_element_by_link_text("אזור").click()
    driver.find_element_by_xpath("//li[@data-option-array-index='2']").click()
    # Pick a category
    driver.find_element_by_link_text("קטגוריה").click()
    driver.find_element_by_xpath("//li[@data-option-array-index='2']").click()
    # Press the search button
    driver.find_element_by_class_name("ui-btn").click()

def business_screen(driver):
    # Pick a Buisness
    driver.find_element_by_link_text("מסעדת מגזינו").click()
    # Type a price
    driver.find_element_by_xpath("//input[@data-parsley-type='number']").send_keys("250")
    # Press button "לבחירה"
    driver.find_element_by_xpath("//button[@type = 'submit']").click()


def information_screen(driver):
    # Press radio button "למישהו אחר"
    driver.find_element_by_xpath("//label[@data='forSomeone']").click()
    # Enter receiver name
    driver.find_element_by_xpath("//input[@data-parsley-required-message='מי הזוכה המאושר? יש להשלים את שם המקבל/ת']").send_keys("Yuliya")
    # Enter sender name
    sender = driver.find_element_by_xpath("//input[@data-parsley-required-message='למי יגידו תודה? שכחת למלא את השם שלך']")
    sender.clear()
    sender.send_keys("Mark")
    # Enter a blessing
    blessing = driver.find_element_by_xpath("//textarea[@data-parsley-group='main']")
    blessing.clear()
    blessing.send_keys("Good Luck !!!")
    # Upload a picture
    driver.find_element_by_xpath("//input[@name='fileUpload']").send_keys(IMAGE)
    # Pick the event
    driver.find_element_by_link_text("לאיזה אירוע?").click()
    driver.find_element_by_xpath("//li[@data-option-array-index='1']").click()
    # Press radio button "מיד אחרי התשלום"
    driver.find_element_by_class_name("send-now").click()
    # Pick Email
    driver.find_element_by_class_name("icon-envelope").click()
    # Enter address
    driver.find_element_by_xpath("//input[@type='email']").send_keys("Yuliya@Yuliya.com")
    # Press save
    driver.find_element_by_class_name("btn-save").click()
    # submit
    driver.find_element_by_xpath("//button[@type = 'submit']").click()



def main():
    # opeen and read file with website name
    with open("website", "r") as web_file:
        web_site = web_file.read()
    # create Chrome driver
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    # default timeout of 10 sec
    driver.implicitly_wait(10)
    # open website
    driver.get(web_site)

    # use or registration or login function
    # registration_screen(driver)
    login_screen(driver)
    home_screen(driver)
    business_screen(driver)
    information_screen(driver)
    # close Chrome browser
    driver.quit()


if __name__ == '__main__':
    main()
