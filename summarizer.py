from bs4 import BeautifulSoup
import urllib.request
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
nltk.download('punkt')

choice = input("What would you like to search for? ")
ignores = ["See also","References","Bibliography","Further reading","External links","Media related to Matches at Wikimedia Commons","The dictionary definition of Match at Wiktionary","Navigation menu","Personal tools","Namespaces","Variants","expanded","collapsed","Views","More","expanded","collapsed","Search","Navigation","Contribute","Tools","Print/export","In other projects","Languages"]

parser = 'html.parser'
resp = urllib.request.urlopen("https://en.wikipedia.org/wiki/"+ choice)
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
description = ''
for para in soup.find_all(['h1','h2','h3','p']):
    text = para.get_text()
    if "[edit]" in text:
        text = text.replace("[edit]", "")
    if text not in ignores:
        
        description += text


parser = PlaintextParser.from_string(description,Tokenizer("english"))
summarizer = LexRankSummarizer()
summary = summarizer(parser.document, 10)

for sentence in summary:
        print(sentence)