import csv
import vt_connection as  vt_baglan
import os
import matplotlib.pyplot as plt
import pandas as pd
from pylab import *
class grafik_ciz():
      def __init__(self):
            baglanti=vt_baglan.Vt_Connection()
            imlec=baglanti.imlec
            imlec.execute("select * from icerik_girisler")
            with open("girisler_data.csv", "w") as csv_file:
                  csv_writer = csv.writer(csv_file, delimiter=",")
                  csv_writer.writerow([i[0] for i in imlec.description])#alan başlıkarını yaz ilk satıra
                  csv_writer.writerows(imlec)

            girisler=pd.read_csv("girisler_data.csv")

            veriler=girisler.groupby('tarih')['v_isi'].mean()#tarih bazında v isi sutunu ortlaması al


            title("Tarih Bazlı Giriş Yapanların Ortalama Vücut ısısı")
            xlabel("Vücut Isısı")

            axis([35, 37.5,None,None])#x ekseni aralığı
            ax=veriler.plot(kind='barh',figsize=(7, 5),color="blue", width=0.06,grid=True)#çizimi yap

            for i in ax.patches:#grafikleri tek tek al
                ax.text(i.get_width()+-.08, i.get_y()+.1,#yazılcak nokta belirleniyor
                        str(round(i.get_width(),2)), fontsize=10,color='red')# değeri yaz
            plt.show()
