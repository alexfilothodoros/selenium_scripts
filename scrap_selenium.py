from selenium import webdriver
import re, requests, os, io, hashlib
from PIL import Image
from collections import OrderedDict



options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(executable_path='/Users/alex/Documents/chromedriver', options = options)
driver.get("some_url")
images = driver.find_elements_by_tag_name('img')
List = []
for image in images:
    c =  image.get_attribute('src')
    if c[-7] == 'b' :
        print(c)
        List.append(c)

driver.quit()      
List = list(OrderedDict.fromkeys(List))

def persist_image(folder_path:str,url:str):
    try:
        image_content = requests.get(url).content
    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")
    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        file_path = 'images/' + url[39:]
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=100)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")
    
for i in range(len(List)):
    persist_image('images', List[i])