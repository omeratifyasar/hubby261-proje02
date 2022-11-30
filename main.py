import time
from getURL import GetURL
from dataURL import DataURL
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Yerli Web Örümceğine Hoşgeldiniz").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)


root.mainloop()






useDataURL = DataURL()
useGetURL = GetURL()

print("-:  Mini Örümceğe Hoş Geldiniz! :")
print("|------------------------------|")
print("")
time.sleep(2)

while True:
    print("Menü: 0)Çıkış 1)URL Listele 2)URL Ekle 3)Örümcek Gönder 4)Sonuçları Listele")
    menuSecim = (input("Tercihiniz: "))
    if menuSecim.isdigit():
        menuSecim = int(menuSecim)
        if menuSecim == 0:
            print("Mini Örümcek kapatılıyor...")
            time.sleep(1)
            break
        elif menuSecim == 1:
            useDataURL.dataRead()
        elif menuSecim == 2:
            useDataURL.dataWrite()
        elif menuSecim == 3:
            useGetURL.getWeb()
        elif menuSecim == 4:
            useGetURL.getList()
        elif menuSecim>=4:
            print("Lütfen 0 ile 4 arasında seçim yapın.")
    else:
        print("Lütfen 0 ile 4 arasında geçerli bir menü numarası giriniz.")

