
# webcloud.py creates a class for turning a webpage's html text into a dictionary of the frequency of words in that text

from urllib.request import Request, urlopen
import scraper as sc

class webcloud:

    def __init__(self,url):
        self.url = url;
        self.common_words = sc.introscraper('https://en.wikipedia.org/wiki/Most_common_words_in_English','wikt:','"','<>\\/:=%.-",_–;#1234567890(){}[]').scrape();
    # webcloud.webtext() returns the html text from the webpage
    def webtext(self):
        req = Request(self.url);
        try:
            page = urlopen(req);
        except:
            return(None);
        html_bytes = page.read();
        html = html_bytes.decode("utf-8");
        return(html);

    # webcloud.cloud() returns a dictionary of the frequency of words in the webpage
    def cloud(self):
        text = self.webtext();
        if text is None:
            return(None);
        cloud = {};
        index = 0;
        banned = '<>\\/:=%.-",_–;#1234567890(){}[]'; #list all banned characters here
        punctuation = '!?.,*'; #list possible punctuation that could be at the end of a word
        while (index != -1):
            index = text.find(" ")
            word = text[0:(index)]
            blocked = 0;
            if word in self.common_words:
                blocked = 1;
            for k in punctuation:
                try:
                    if word[len(word)-1] == k:
                        word = word[0:len(word)-1];
                except:
                    pass
            for k in banned:
                if k in word:
                    blocked = 1;
            if blocked:
                text = text[len(word)+1:len(text)];
            else:
                if word in cloud:
                    cloud[word] += 1;
                else:
                    cloud[word] = 1;
                text = text[len(word)+1:len(text)]; 
        if text in cloud:
            cloud[text] += 1;
        else:
            cloud[text] = 1;
        return(dict(sorted(cloud.items(), key = lambda kv: kv[1],reverse = True)));
