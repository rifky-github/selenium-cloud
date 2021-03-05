from selenium import webdriver
import os

# PATH = "C:\\Users\\xrifk\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
# driver = webdriver.Chrome(executable_path=PATH)



driver.get('https://brainly.co.id/tugas/8600866')

tulisan  = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/div[1]/article/div/div/div[2]/div/div/h1/span[1]').text

print('[Tulisan Yang Harus Keluar]\n"Kerak samudra lebih dinamis dibandingkan kerak benua. kerak samudra selalu mengalami pembaruan oleh aktivitas"\n\n')
print('[Output]\n' + tulisan)