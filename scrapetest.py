import scraper as s

url = "https://coinmarketcap.com"
sindx1 = '<p font-weight="semibold" color="text" font-size="1" class="sc-1eb5slv-0 iJjGCS">'
sindx2 = '</p>'
banned = '<>\\/:=%.-",_–;#1234567890(){}[]'
    
subs = s.introscraper(url,sindx1,sindx2,banned).scrape();

urlA = 'https://coinmarketcap.com/currencies/';
urlB = '/';
indexstart = '<div class="priceValue___11gHJ">'
indexend = '</div>'

cryptodata = s.extroscraper(urlA,subs,urlB,indexstart,indexend).scrape();
print(cryptodata);
