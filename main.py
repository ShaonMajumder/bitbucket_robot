#-*- coding:utf-8 -*-
import sys,os,os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from bot_utility import *


def bitbucket_login(browser):
	browser.get("https://bitbucket.org/product")
	browser.find_element_by_link_text("Log in").click()
	while True:
		try:
			wait = WebDriverWait(browser, 1)
			username_box = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="username"]')))
			break
		except NoSuchElementException:
			pass
		except TimeoutException:
			pass

	username_box.clear()
	username_box.send_keys(configs['bitbucket_email'])
	browser.find_element_by_xpath('//button[@id="login-submit"]').click()
	while True:
		try:
			wait = WebDriverWait(browser, 1)
			password_box = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]')))
			break
		except NoSuchElementException:
			pass
		except TimeoutException:
			pass
	
	password_box.clear()
	password_box.send_keys(configs['bitbucket_password'])
	browser.find_element_by_xpath('//button[@id="login-submit"]').click()


def open_repository_bitbucket(browser,repo_name):
	while True:
		try:
			wait = WebDriverWait(browser, 3)
			your_work = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@aria-label="Create"]')))
			#your_work = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Your work"]')))
			break
		except NoSuchElementException:
			pass
			#browser.get("https://bitbucket.org")
		except TimeoutException:
			pass
			#browser.get("https://bitbucket.org")

	your_work.click()
	browser.find_element_by_link_text("Repository").click()

	while True:
		try:
			wait = WebDriverWait(browser, 1)
			repo_name_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_name"]')))
			break
		except NoSuchElementException:
			pass
		except TimeoutException:
			pass
	
	repo_name_text.clear()
	repo_name_text.send_keys(repo_name)

	browser.find_element_by_xpath('//button[text()="Create repository"][@type="submit"]').click()
	"""
	while True:
		try:
			wait = WebDriverWait(browser, 1)
			create_repo_btn = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Create repository"][@type="submit"]')))
			break
		except NoSuchElementException:
			pass
		except TimeoutException:
			pass
	
	create_repo_btn.click()
	"""


	while True:
		try:
			wait = WebDriverWait(browser, 1)
			copy_btn = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@aria-label="Copy"]')))
			break
		except NoSuchElementException:
			pass
		except TimeoutException:
			pass

	copy_btn.click()

	

	win32clipboard.OpenClipboard()
	repo_link = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	return repo_link


def delete_repository_bitbucket(browser,repo_name):
	while True:
		print("Deleting repository",repo_name," from bitbucket")
		while True:
			try:
				wait = WebDriverWait(browser, 7)
				repo_title = wait.until(EC.visibility_of_element_located((By.XPATH,'//a[@title="'+repo_name+'"]')))
				break
			except NoSuchElementException:
				browser.get("https://bitbucket.org/dashboard/overview")
			except TimeoutException:
				browser.get("https://bitbucket.org/dashboard/overview")

		repo_title.click()

		while True:
			try:
				wait = WebDriverWait(browser, 1)
				settings = wait.until(EC.visibility_of_element_located((By.XPATH,'//span[text()="Settings"]')))
				break
			except NoSuchElementException:
				pass
			except TimeoutException:
				pass

		settings.click()



		while True:
			try:
				wait = WebDriverWait(browser, 1)
				del_repo_btn = wait.until(EC.visibility_of_element_located((By.XPATH,'//button[text()="Delete repository\n  "][@id="delete-repo-btn"]')))
				break
			except NoSuchElementException:
				pass
			except TimeoutException:
				pass


		del_repo_btn.click()

		while True:
			try:
				wait = WebDriverWait(browser, 1)
				delete_button = wait.until(EC.visibility_of_element_located((By.XPATH,'//button[@class="aui-button-danger aui-button aui-button-primary dialog-submit"][text()="Delete"]')))
				break
			except NoSuchElementException:
				pass
			except TimeoutException:
				pass

		delete_button.click()

		time.sleep(4)
		
		#Check if it is deleted
		browser.get("https://bitbucket.org/dashboard/repositories")
		try:
			wait = WebDriverWait(browser, 7)
			repo_title = wait.until(EC.visibility_of_element_located((By.XPATH,'//a[@title="'+repo_name+'"]')))
		except NoSuchElementException:
			break
		except TimeoutException:
			break
		#if deletation confirmed then exit by break



if __name__ == "__main__":
	browser = webdriver.Chrome(browser_url)
	bitbucket_login(browser)
	print(open_repository_bitbucket(browser,"bittus"))
	delete_repository_bitbucket(browser,"bittus")
	browser.close()
	quit()