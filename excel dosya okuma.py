from xlrd import open_workbook  #xl modülünden open fonksiyonu
excel_dosya = open_workbook("maaş.xlsx")

for sayfa in excel_dosya.sheets():
   # Bu satırda sayfa değişkenine bir xlrd.sheet objesi atandı.

   print ("Çalışma sayfası: " + sayfa.name)

   # sayfadaki satır sayısına nrows ile ulaşıyoruz.
   for satir in range(sayfa.nrows):
       degerler = []

       # Sütün sayısına ncols üzerinden ulaşıyoruz
       for sutun in range(sayfa.ncols):
           # cell metodu bize bir hücre döndürüyor, value ile değer okuyoruz.
           degerler.append(str(sayfa.cell(satir, sutun).value))  #append ekle demek
       print("\t".join(degerler))  #t tab boşluk 3 boşluk bırakır

