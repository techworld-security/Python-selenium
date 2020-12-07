from selenium import webdriver
import time

def main():
	driver = webdriver.Firefox()
	driver.get("https://www.instagram.com/accounts/login/")
	time.sleep(4)
	driver.find_element_by_name("username").send_keys("<your username here>")
	driver.find_element_by_name("password").send_keys("<your password here>")
	driver.find_element_by_xpath('//button[normalize-space()="Log In"]').click()
	time.sleep(5)
	driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']").click()
	time.sleep(5)
	driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()
    
if __name__ == "__main__":
	main()