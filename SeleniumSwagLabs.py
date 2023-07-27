from selenium import webdriver
import time 

# Calls the path to chromedriver in my computer, please adjust this value accordingly

PATH = "D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Open browser and direct it to the URL

driver.get("https://www.saucedemo.com/")

# Find for an element that contains the username value

div_username_element = driver.find_element_by_id('login_credentials')

div_username_text = div_username_element.text

# Adjust the string so that it records all the username

start_index = div_username_text.index('Accepted usernames are:') + len('Accepted usernames are:')
usernames = div_username_text[start_index:].strip().split('\n')

# Print the list of usernames
print(usernames[0])

# Find for an element that contains the password value

div_password_element = driver.find_element_by_class_name('login_password')

div_password_text = div_password_element.text

# Adjust the string so that it records the password

start_password_index = div_password_text.index('Password for all users:') + len('Password for all users:')
password = div_password_text[start_password_index:].strip()

# Print the password

print(password)

# Find the username and password input elements

username_input = driver.find_element_by_id('user-name')
password_input = driver.find_element_by_id('password')

# Find the login button by its ID

login_button = driver.find_element_by_id('login-button')

# Input the username and password values into the respective input fields

username_input.send_keys(usernames[0])
password_input.send_keys(password)

time.sleep(2)

# Click the login button to submit the form

login_button.click()

# Get the XPath elements for Price and print it

div_backpack_elements_price = driver.find_element_by_xpath(
    '//div[@class="inventory_item_name" and text()="Sauce Labs Backpack"]/ancestor::div[@class="inventory_item"]/descendant::div[@class="inventory_item_price"]'
)

catalogue_price = div_backpack_elements_price.text

print(div_backpack_elements_price.text)

# Get the XPath elements to find the button

div_backpack_addcart_buttons = driver.find_element_by_xpath(
    '//div[@class="inventory_item_name" and text()="Sauce Labs Backpack"]/ancestor::div[@class="inventory_item"]/descendant::button[@class="btn btn_primary btn_small btn_inventory"]'
)

div_backpack_addcart_buttons.click()

time.sleep(2)

# Open Shopping Cart to finish shopping

div_shoppingcart_buttons = driver.find_element_by_id('shopping_cart_container')

div_shoppingcart_buttons.click()

# Find the Price of Sauce Labs Backpack in the cart items

div_cart_backpack_elements = driver.find_element_by_xpath(
    '//div[@class="inventory_item_name" and text()="Sauce Labs Backpack"]/ancestor::div[@class="cart_item"]/descendant::div[@class="inventory_item_price"]'
)

cart_price = div_cart_backpack_elements.text

print(div_cart_backpack_elements.text)

assert cart_price == catalogue_price, "Item Price is different"

time.sleep(2)

# Continue Checkout Process

div_checkout_button = driver.find_element_by_id('checkout')

div_checkout_button.click()

time.sleep(2)

first_name = 'John'
last_name = 'Doe'
zip_code = '1234'

first_name_input = driver.find_element_by_id('first-name')
last_name_input = driver.find_element_by_id('last-name')
zip_code_input = driver.find_element_by_id('postal-code')

first_name_input.send_keys(first_name)
last_name_input.send_keys(last_name)
zip_code_input.send_keys(zip_code)

time.sleep(2)

div_continue_checkout_button = driver.find_element_by_id('continue')

div_continue_checkout_button.click()

# Click Finish Button

div_finish_button =  driver.find_element_by_id('finish')

div_finish_button.click()

time.sleep(2)

div_backhome_button = driver.find_element_by_id('back-to-products')

div_backhome_button.click()

time.sleep(2)

driver.quit()
