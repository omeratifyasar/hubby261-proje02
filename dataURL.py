import os
class DataURL:

  dataFile = "dataURL.txt"

  def __init__(self):
    fileTest = open(self.dataFile, 'a')
    fileTest.close()

  def dataWrite(self):
    dataOpen = open(self.dataFile, 'a')
    siteURL = input("Site adresini ön eki kullanarak giriniz: ")
    http = siteURL[:7]
    https = siteURL[:8]
    if http == "http://" or https == "https://":
        dataOpen.write(siteURL + "\n")
        dataOpen.close()
        print("Girdiğiniz URL kaydedilmiştir.")
    else:
        print("Lütfen URL ön ekini (/'https://' veya 'http://') giriniz.")

  def dataRead(self):
      dataOpen = open(self.dataFile, 'r')
      if os.stat(self.dataFile).st_size==0:
          print("Kaydedilmiş bir adres bulunmamaktadır!")
      else:
            for dataShow in dataOpen:
                print(dataShow)
      dataOpen.close()