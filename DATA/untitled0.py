# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 15:42:00 2023

@author: Kosel
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
import time
import openpyxl

# Excel dosyasını yükleyin (eğer varsa)
try:
    workbook = openpyxl.load_workbook("veri.xlsx")
    sheet = workbook.active
except FileNotFoundError:
    # Eğer dosya bulunamazsa, yeni bir çalışma kitabı oluşturun
    workbook = openpyxl.Workbook()
    sheet = workbook.active

edge_options = EdgeOptions()
edge_options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"  # Specify the path to msedge.exe

# Edge WebDriver'ı başlatın
driver = webdriver.Edge(options=edge_options, service=EdgeService("msedgedriver.exe"))

# Veri çekmek istediğiniz URL'yi belirtin
url = "https://www.transfermarkt.com.tr/ssc-neapel/startseite/verein/6195/saison_id/2022"

# URL'yi açın
driver.get(url)

# Sayfa yüklendiğinde 5 saniye bekleyin
time.sleep(5)

# Bekleme süresi ekleyebilirsiniz (örneğin, 10 saniye bekleyelim)
driver.implicitly_wait(10)

# Tabloyu bulun
table_xpath = "/html/body/div[1]/main/header/div[6]/div/ul[2]/li[2]"
table_rows = driver.find_elements(By.XPATH, table_xpath)

# Her bir satır için td'leri yazdırın
for row in table_rows:
    # Satırdaki td elemanlarını bulun
    cells = row.find_elements(By.TAG_NAME, "td")
    
    # Her bir td'nin içeriğini bir liste olarak saklayın
    attributes = [cell.text for cell in cells]
    
    # Her bir tr için yeni bir satır ekleyin
    sheet.append(attributes)

# Excel dosyasını kaydet
workbook.save("veri.xlsx")
print("veri kaydedildi")
# Tarayıcıyı kapatın
driver.quit()