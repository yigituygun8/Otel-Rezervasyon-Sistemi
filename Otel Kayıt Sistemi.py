# Oteller için müşteri kaydı yapan sistem
# Otel isimleri için herhangi bir rezervasyon sitesinden verileri çekeceğim (sadece Antalya) (BeautifulSoup4)

import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random

# Web Scraping
oteller = "https://www.tatilsepeti.com/antalya-otelleri"
html = urlopen(oteller)
soup = BeautifulSoup(html, "html.parser")
allrows = soup.find_all("h2")

# Captcha (Doğrulama)
captchalist = []
captcha = random.randint(1000000,9999999)
captchalist.append(captcha)

print("Otel Rezervasyon Sistemine Hoş Geldiniz!")
time.sleep(0.5)
print("Antalya'daki Oteller Sıralanıyor...")
print("-"*25)
time.sleep(1)

otelisimler = []
for cell in allrows[:30]:
    print(cell.text)
    otelisimler.append(cell.text)
    time.sleep(0.2)

otelisimler = str(otelisimler)

def otel():
    hangi_otel = input("Hangi Oteli Rezerve Etmek İstersiniz?:")
    hangi_otel = r"\n"+hangi_otel+r"\n"

    # OTEL İSİM KONTROLÜ 
    if hangi_otel in otelisimler:
        print("Kayıt Olmanız Gerekiyor")
        
    else:
        print("Otel Bulunamadı!")
        otel()
otel()
    
username = []
password = []
time.sleep(0.5)

def sign_in(loginusername, loginpassword):
    loginusername = str(input("İsminiz Nedir?: "))
    time.sleep(0.5)
    loginpassword = str(input("Soy İsminiz Nedir?: "))

    username.append(loginusername)
    password.append(loginpassword)
    
    print(captcha)
    time.sleep(0.5)
    def captcha_success(captchaverify):
        captchaverify = int(input("Doğrulamak İçin Yukarıdaki Sayıyı Giriniz: "))
        if captchaverify in captchalist:
            print("Başarıyla Kayıt Oluşturuldu")
            
        else:
            print("Tekrar Deneyiniz...")
            secondcaptcha = random.randint(1000000,9999999)
            captchalist.append(secondcaptcha)
            print(secondcaptcha)
            captchaverify2 = int(input("Yukarıdaki Sayıyı Giriniz: "))
            if captchaverify2 in captchalist:
                print("Başarıyla Rezervasyon Yapıldı")

            else:
                thirdcaptcha = random.randint(1000000,9999999)
                captchalist.append(thirdcaptcha)
                print(thirdcaptcha)
                captcha_success(captchaverify2)
    captcha_success(captcha)

sign_in(username, password)