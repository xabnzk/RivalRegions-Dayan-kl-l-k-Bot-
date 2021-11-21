from selenium import webdriver
import time
from getpass import getpass

saniye_input =  input("Kaç Saniyede Bir Dayanıklığa Tıklanacak")

print("RR Hesabınızın Facebook'a Bağlı Olması Gerekmektedir.")
giris_face_isim_inputk = input("İsim Veya Telefon Numarası Giriniz(FaceBook İçin) =>")
giris_face_sifre_inputk = getpass("Şifre(FaceBook İçin) =>")

browser = webdriver.Chrome("chromedriver.exe")
time.sleep(2)
browser.get("https://rivalregions.com/")
time.sleep(5)

giris_yap = browser.find_element_by_xpath("//*[@id='sa_add2']/div[2]/a[1]/div")
giris_yap.click()

kullanici_adi = browser.find_element_by_xpath("//*[@id='email']")
kullanici_sifre = browser.find_element_by_xpath("//*[@id='pass']")

kullanici_adi.send_keys(giris_face_isim_inputk)
kullanici_sifre.send_keys(giris_face_sifre_inputk)

face_book_giris_tusu_ = browser.find_element_by_name("login")
face_book_giris_tusu_.click()
time.sleep(10)

Dayanıklılık_RR = browser.find_element_by_xpath("//*[@id='index_perks_list']/div[6]/div[1]")
Dayanıklılık_RR.click()

while True:
    yoga_pratigi_yap = browser.find_element_by_xpath("//*[@id='perk_target_4']/div[1]/div[1]/div")
    yoga_pratigi_yap.click()
    time.sleep(saniye_input)
    Dayanıklılık_RR_ = browser.find_element_by_xpath("//*[@id='index_perks_list']/div[6]/div[1]")
    Dayanıklılık_RR.click()