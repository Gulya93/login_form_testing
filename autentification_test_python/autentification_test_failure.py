from selenium import webdriver
from selenium.webdriver.common.by import By



link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# validating correct information
input2 = browser.find_element(By.CLASS_NAME, 'form-control.second')
input2.send_keys("Finland")
input3 = browser.find_element(By.XPATH, '//input[@placeholder="Input your phone"]')
input3.send_keys("2345676543")

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
