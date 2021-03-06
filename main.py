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



driver.get('https://sman17sby.simpan.id/index.php/login')

tulisan  = driver.find_element_by_class_name('copyright').text

print('[Tulisan Yang Harus Keluar]\nCopyright © 2014 - 2021 SMA NEGERI 17 SURABAYA by SansekertaIndonesia - QuickEdu School\n\n')
print('[Output]\n' + tulisan)
