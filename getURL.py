import os
import urllib.request
from bs4 import BeautifulSoup

class GetURL:
    dataFile = "dataURL.txt"
    getFile = "getURL.txt"

    def __init__(self):
        fileTest = open(self.getFile, 'a')
        fileTest.close()

    def getWeb(self):
        print("Örümcek çalışıyor...")
        dataOpen = open(self.dataFile, 'r')
        getOpen = open(self.getFile, 'w')
        for dataGet in dataOpen:
            print("Şuanda ziyaret edilen URL: " + dataGet + "Girdiğiniz " + dataGet + "adresine örümcek gönderiliyor." )
            webSite = urllib.request.urlopen(dataGet)
            getBytes = webSite.read()
            webPage = getBytes.decode("utf8")
            webSite.close()
            soup = BeautifulSoup(webPage, 'html.parser')
            getOpen.write(dataGet.strip() + " - " + soup.title.contents[0] + "\n" + soup.get_text("<p>","title"))
        dataOpen.close()
        getOpen.close()
        print(" Örümcek gönderdildi. Girilen tüm URL adresleri ziyaret edildi ve çalışma tamamlandı!")

    def getList(self):
        getOpen = open(self.getFile, 'r')
        if os.stat(self.getFile).st_size == 0:
            print("Henüz ziyaret edilmiş adres bulunmuyor!")
        else:
            for dataShow in getOpen:
                print(dataShow)
        getOpen.close()


