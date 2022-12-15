import requests
from bs4 import BeautifulSoup
import sqlite3
url = 'https://www.booking.com/city/ua/kiev.uk.html?aid=318615&label=Catch_All-UK-129118751204-dFnPUHvl_ACzxnEIIQGlDwS634117856097%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atidsa-1227182645462%3Alp9061015%3Ali%3Adec%3Adm%3Aag129118751204%3Acmp14590362430&sid=7185258c47b50e05faee223daaaac464'
base_url = "?aid=318615&amp;label=Catch_All-UK-129118751204-dFnPUHvl_ACzxnEIIQGlDwS634117856097%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atidsa-1227182645462%3Alp9061015%3Ali%3Adec%3Adm%3Aag129118751204%3Acmp14590362430&amp;sid=7185258c47b50e05faee223daaaac464"
base_url1 = 'https://www.booking.com/'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,'html.parser')
container = soup.find("div",id="bodyconstraint")
nan = container.find("div",class_= "lp-bui-section-wrap")
j = nan.find("div",class_="content__col")
jan = j.find("div").find_next('div').find_next('div').find_next('div').find_next('div')
gans = jan.find_all("div",class_="sr__card js-sr-card")
urls=[]
for i in gans:
    man = i.find("div","sr__card_content")
    man1 = man.find('div')
    man2 = man1.find('div')
    url = man2.select_one("header a")["href"]
    urls.append(base_url1+url+base_url)
args = []
for god in urls:
    response = requests.get(god)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    container = soup.find("div", id="bodyconstraint")
    nan = container.find("div",id="hotelTmpl")
    j=nan.find("div",class_="bui-grid bui-grid--size-small")
    gan = j.find("div", class_="k2-hp--gallery-header bui-grid__column bui-grid__column-9")
    june = gan.find("div",id="wrap-hotelpage-top")
    fon = june.find("div",id="hp_hotel_name")
    janh= gan.find("p",id="showMap2")
    han = gan.find("div",class_="clearfix bh-photo-grid bh-photo-grid--space-down fix-score-hover-opacity")
    description_ = nan.find("div",class_="hp_desc_main_content").find("div",id="property_description_content").find("p").find_next("p").text
    name_ = fon.select_one("h2").text
    adress_ = janh.find("span").find_next("span").text
    photo_ = han.find("a", class_="bh-photo-grid-item bh-photo-grid-photo1 active-image").find("img")["src"]
    args.append((name_,adress_,description_,photo_))
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()
cursor.executemany("INSERT INTO hello_hotels VALUES (?,?,?,?)", args)
conn.commit()
conn.close()