#Bu program Python 3.X sürümüyle uyumlu çalışır
import os.path 
import webbrowser

print(""" ___           _             __  __       _
|_ _|_ __   __| | _____  __ |  \/  | __ _| | _____ _ __
 | || '_ \ / _` |/ _ \ \/ / | |\/| |/ _` | |/ / _ \ '__|
 | || | | | (_| |  __/>  <  | |  | | (_| |   <  __/ |
|___|_| |_|\__,_|\___/_/\_\ |_|  |_|\__,_|_|\_\___|_|

""")
print("Coded by:Crackmeci")
print("TURKHACKTEAM")

arkaplan= input("Arkaplan Rengi Giriniz:")
baslik = input("Başlık Giriniz(örn:hacked):")
resim = input("İndex Ana Görselinin Linkini Giriniz:")
genislik = input("Resim Genişliği Giriniz:")
yukseklik = input("Resmin Yüksekliğini Giriniz:")
mesaj = input("Mesajınızı Giriniz:")
favicon = input("Favicon Url'si Giriniz:")
font = input("Font Rengini Giriniz:")
fonttur = input("Font Türünü Giriniz:")
fontboy = input("Font Boyutunu Giriniz:")
alert = input("Site açılınca verilecek uyarı mesajını giriniz:")
kalinlik = input("Font kalın olsun mu(bold) olsun yazın:")
bos = ""


if arkaplan==bos:
    arkaplan = "#000000"
if baslik==bos:
    baslik = "Hacked By Turkhackteam"
if resim==bos:
    resim = "https://i.ytimg.com/vi/1JN8M1ofxSc/maxresdefault.jpg"
if mesaj==bos:
    mesaj = "Hacked By Turkhackteam"
if font==bos:
    font="#ffffff"
if favicon==bos:
    favicon = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/1280px-Flag_of_Turkey.svg.png"
if fonttur==bos:
    fonttur= "Tahoma"
if fontboy==bos:
    fontboy=18
if alert==bos:
    alert="Hacked By TURKHACKTEAM"
if kalinlik == "olsun":
    kalinlik = "strong"
index = """ 
<!DOCTYPE HTML>
<html>
<head>
<link rel="icon" href="{9}" type="image/x-icon" />
<title>{0}</title>
<meta charset="utf8">
</head>
<body bgcolor="{1}">
<script>
alert("{7}");
</script>
<center><img src="{2}" alt="" width="{10}" height="{11}"></img></center>
<center><{8}><font color="{3}" family="{4}" size="{5}">{6}</font></{8}></center>
</body>
<!--Bu index THT İndex Makerla Oluşturulmuştur-->
<!--
|_   _|   _ _ __| | _| | | | __ _  ___| | _|_   _|__  __ _ _ __ ___
  | || | | | '__| |/ / |_| |/ _` |/ __| |/ / | |/ _ \/ _` | '_ ` _ \
  | || |_| | |  |   <|  _  | (_| | (__|   <  | |  __/ (_| | | | | | |
  |_| \__,_|_|  |_|\_\_| |_|\__,_|\___|_|\_\ |_|\___|\__,_|_| |_| |_|
-->

</html>""".format(baslik,arkaplan,resim,font,fonttur,fontboy,mesaj,alert,kalinlik,favicon,genislik,yukseklik)
if os.path.exists("index.html"):
   dosya = open("index2.html","w")
   dosya.write(index)
   webbrowser.open_new_tab("index2.html")   
else:
    dosya = open("index.html","w")
    dosya.write(index)
    dosya.close()
    webbrowser.open_new_tab("index.html")

print("İndexiniz Başarıyla Oluşturulmuştur...")
