import urllib.request

url = "https://www.havadurumu15gunluk.net/havadurumu/alanya-hava-durumu-15-gunluk.html"
site = urllib.request.urlopen(url).read().decode('utf-8')

gunduz = '<td width="45">&nbsp;&nbsp;(-?\d+)°C</td>'
gece = '<td width="45">&nbsp;(-?\d+)°C</td>'
gun = '<td width="70" nowrap="nowrap">(.*)</td>'
tarih = '<td width="75" nowrap="nowrap">(.*)</td>'
aciklama = '<img src="/havadurumu/images/trans.gif" alt="Alanya Hava durumu 15 günlük" width="1" height="1" />(.*)</div>'

#gündüz sıcaklık değerlerini eşlemek için kullanıyoruz
comp_gunduz = re.compile(gunduz)

#gece sıcaklık değerlerini eşlemek için kullanıyoruz
comp_gece = re.compile(gece)

#Gün isimlerini eşleştirmek için
comp_gun = re.compile(gun)

#Tarihleri eşleştirmek için 
comp_tarih = re.compile(tarih)

#hava durumu açıklamalarını eşleştirmek için
comp_aciklama = re.compile(aciklama)

gunduz = []
gece = []
gun = []
tarih = []
aciklama = []

#re.findall kullanarak sitedeki metindekileri eşlemek için kulanılır ve dizilere kaydeder
for i in re.findall(gunduz, site):
    gunduz.append(i)

for i in re.findall(gece, site):
    gece.append(i)

for i in re.findall(gun, site):
    gun.append(i)

for i in re.findall(tarih, site):
    tarih.append(i)

for i in re.findall(aciklama, site):
    aciklama.append(i)

print("-" * 75)
print("                         Alanya HAVA DURUMU")
print("-" * 75)
for i in range(0, len(gun)):
    print("{} {},\n\t\t\t\t\tgündüz: {} °C\tgece: {} °C\t{}".format(tarih[i], gun[i], gunduz[i], gece[i], aciklama[i]))
    print("-" * 75)