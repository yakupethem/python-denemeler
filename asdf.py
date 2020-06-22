from xlrd import *

excel_dosya = open_workbook("C:\\Users\yakup\Desktop\python\hafta_3\hafta_3\maaslar.xlsx")

for sayfa in excel_dosya.sheets():
    # Bu satırda sayfa değişkenine bir xlrd.sheet objesi atandı.

    print("Çalışma sayfası: " + sayfa.name)

    # sayfadaki satır sayısına nrows ile ulaşıyoruz.
    for satir in range(sayfa.nrows):
        degerler = []

        # Sütün sayısına ncols üzerinden ulaşıyoruz
        for sutun in range(sayfa.ncols):
            # cell metodu bize bir hücre döndürüyor, value ile değer okuyoruz.
            degerler.append(str(sayfa.cell(satir, sutun).value))
        print("\t".join(degerler))


a = open_workbook("C:\\Users\yakup\Desktop\python\hafta_3\hafta_3\maaslar.xlsx")

# Index'e göre sayfaları alma
for i in range(a.nsheets):
    print( a.sheet_by_index(i))

# Isime göre sayfaları alma
for name in a.sheet_names():
    print (a.sheet_by_name(name))

for sayfa in a.sheets():
    print (sheet)