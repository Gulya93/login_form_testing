from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# validating correct information
input1 = browser.find_element(By.CLASS_NAME, 'form-control.first')
input1.send_keys("Ivan")
input2 = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
input2.send_keys("efe@dd")

# send the correct form
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()


# find element with welcome text
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
# recording variable welcome_text the text from the element welcome_text_elt
welcome_text = welcome_text_elt.text

# cheking results
assert "Congratulations! You have successfully registered!" == welcome_text


browser.quit()
