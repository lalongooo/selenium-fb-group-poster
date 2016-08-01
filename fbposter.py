
# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

group_links = [
	# Your Facebook Groups links.
	# IMPORTANT: You must be a member of the group, being ADMIN nor required.
	"https://www.facebook.com/groups/ayearofrunning/", # A group of Mark Zuckerberg
]

def main():

	# Your Facebook account user and password
	usr = ""
	pwd = ""
	message = "Checkout an amazing selenium script for posting in Facebook Groups!\nhttps://github.com/lalongooo/selenium-fb-group-poster"
	attach_image = True
	image_path = "/path/to/the/photo/you/want/to/upload"

	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.cache.disk.enable", False)
	profile.set_preference("browser.cache.memory.enable", False)
	profile.set_preference("browser.cache.offline.enable", False)
	profile.set_preference("network.http.use-cache", False)

	driver = webdriver.Firefox()
	driver.implicitly_wait(15) # seconds

	# Login to Facebook
	driver.get("http://www.facebook.org")
	elem = driver.find_element_by_id("email")
	elem.send_keys(usr)
	elem = driver.find_element_by_id("pass")
	elem.send_keys(pwd)
	elem.send_keys(Keys.RETURN)
	driver.implicitly_wait(5)

	for group in group_links:

		# Go to the Facebook Group
		driver.get(group)

		# Click the post box
		post_box=driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
		post_box=driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
		post_box=driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
		sleep(10)
		post_box=driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
		post_box=driver.find_element_by_xpath("//*[@name='xhpc_message_text']")

		# Enter the text we want to post to Facebook
		post_box.send_keys(message)
		sleep(10)

		if attach_image:
			# Click on the add media button
			addMedia = driver.find_element_by_xpath("//*[@data-testid='media-attachment-selector']")
			addMedia.click()

			# Provide picture file path
			driver.find_element_by_xpath("//div[text()='Upload Photos/Video']/following-sibling::div/input").send_keys(image_path)

		# Get the 'Post' button and click on it
		buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Post') and starts-with(local-name(), 'button')]")
		button = buttons[0]
		button.send_keys(Keys.RETURN)
		sleep(10)

	# driver.close()

if __name__ == '__main__':
  main()