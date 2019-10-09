#Created by Daniel Baigel 11/10/18
#python web scraping script to scrape news headlines from different sources

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime as dt
import csv
from textblob import TextBlob
import sys
#create a bunch of soup, one for each news source
#then scrape the headlines and see how they trend each day
#dataframe should have column names of: date, 4 news sources, type of headline, positive/neutral/negative trend
#further applications:
#	create categories for types of news: sports, politics, environment, technology, finance, entertainment, international, pop culture
#   and then label them as positive, neutral, or negative using machine learning



#get the date
today = dt.today()

#create lists of categories to compare to
politics = ["trump", "dems", "dem", "democrats", "democrat", "democracy", "rep", "republican", 
"republicans", "politics", "election", "elections", "candidate", "candidates", "ballots",
"ballot", "campaign", "government", "govt", "gov't", "senate", "judiciary", "president",
"paul ryan", "vote", "voting", "votes", "gop", "dnc", "rnc", "trump's", "bernie", "bernie sanders",
"senator", "presidential", "affordable care act", "biden", "aoc"]

sports = ["soccer", "football", "tennis", "hockey", "baseball", "world series", 
"world-series", "sport", "sports", "champion", "tournament", "lacrosse", "softball",
"olympics", "world cup"]

environment = ["storm", "typhoon", "earthquake", "tsunami", "hurricane", "tornado", 
"earthquakes", "rain", "global warming", "climate", "environment"]

technology = ["amazon", "iphone", "android", "google", "microsoft", "macbook", "technology",
"netflix", "tech"]

international = ["france", "london", "england", "uk", "brexit", "british", "china",
"japan", "chinese", "tariff", "tariffs", "south africa", "asia", "south america", 
"africa", "african", "countries", "abroad", "saudi", "iran", "israel"]


##########################Get the soup ready##################################################
headlines = []

###########################FOX#################################################
urlFOX = requests.get("https://www.foxnews.com/")
if urlFOX.status_code != 200:
    print(urlFOX.status_code + "\n")
    print("Something is wrong with Fox...")
    sys.exit("Check website status code")

soupFOX = BeautifulSoup(urlFOX.content, 'html.parser')

FOXcontainer = soupFOX.find(class_="collection collection-spotlight has-hero")
FOXcontainer2 = FOXcontainer.find('header', class_='info-header')

FOXheadline = FOXcontainer2.find('a').get_text()
foxBlob = TextBlob(FOXheadline)
foxPolarity = foxBlob.sentiment.polarity
foxSubj = foxBlob.sentiment.subjectivity
print(FOXheadline)
print(foxPolarity)
print(foxSubj)
print("Done with FOX")
headlines.append(FOXheadline)


##########################NBC#################################################
urlNBC = requests.get("https://www.nbcnews.com/")

if urlNBC.status_code != 200:
    print(urlNBC.status_code + "\n")
    print("Something is wrong with NBC...")
    sys.exit("Check website status code")

soupNBC = BeautifulSoup(urlNBC.content, 'html.parser')

NBCcontainer = soupNBC.find('article', class_="teaseCard content___3FGvZ")
#NBCcontainer = soupNBC.find('div', class_="massiveHeadline massiveHeadline___3rr60")
#NBCcontainer = soupNBC.find('article', class_="teaseCard content___3FGvZ content___FIXYj")

NBCcontainer2 = NBCcontainer.find_all('h2')
#NBCcontainerAlt2 = NBCcontainerAlt.find_all('h2')

NBCheadline = NBCcontainer2[1].find('a').get_text()
#NBCheadline = NBCcontainerAlt2[1].find('a').get_text()

nbcBlob = TextBlob(NBCheadline)
nbcPolarity = nbcBlob.sentiment.polarity
nbcSubj = nbcBlob.sentiment.subjectivity

print(NBCheadline)
print(nbcPolarity)
print(nbcSubj)
print("Done with NBC")

headlines.append(NBCheadline)

############################WP#################################################
urlWP = requests.get("https://www.washingtonpost.com/?noredirect=on")
if urlWP.status_code != 200:
    print(urlWP.status_code + "\n")
    print("Something is wrong with Washington Post...")
    sys.exit("Check website status code")

soupWP = BeautifulSoup(urlWP.content, 'html.parser')

#WPcontainer = soupWP.find(class_="no-skin flex-item flex-stack normal-air text-align-center equalize-height-target")
try:
    WPcontainer = soupWP.find(class_="headline normal normal-style text-align-inherit ") #class changes between small, normal, and large, x-large and xx-large, and huge
    WPheadline = WPcontainer.find('a').get_text()
    print("first try")
except:
    try:
        WPcontainer = soupWP.find(class_="headline small normal-style text-align-inherit ") #class changes between small, normal, and large, x-large and xx-large, and huge
        WPheadline = WPcontainer.find('a').get_text()
    except:
        try:
            WPcontainer = soupWP.find(class_="headline large normal-style text-align-inherit ") #class changes between small, normal, and large, x-large and xx-large, and huge
            WPheadline = WPcontainer.find('a').get_text()
        except:
            try:
                WPcontainer = soupWP.find(class_="headline huge normal-style text-align-inherit ") #class changes between small, normal, and large, x-large and xx-large, and huge
                WPheadline = WPcontainer.find('a').get_text()
            except:
                try:
                    WPcontainer = soupWP.find(class_="headline x-large normal-style text-align-inherit ") #class changes between small, normal, and large, x-large and xx-large, and huge
                    WPheadline = WPcontainer.find('a').get_text()
                except:
                    try:
                        WPcontainer = soupWP.find(class_="headline xx-large normal-style text-align-inherit ") #class changes between small, normal, and large, x-large and xx-large, and huge
                        WPheadline = WPcontainer.find('a').get_text()
                    except:
                        sys.exit("Can't find headline tag in Wash Post")

#WPheadline = WPcontainer.find('a').get_text()
wpBlob = TextBlob(WPheadline)
wpPolarity = wpBlob.sentiment.polarity
wpSubj = wpBlob.sentiment.subjectivity
print(WPheadline)
print(wpPolarity)
print(wpSubj)
print("Done with WP")

headlines.append(WPheadline)
# ##########################WP#################################################
urlABC = requests.get("https://abcnews.go.com/")
if urlABC.status_code != 200:
    print(urlABC.status_code + "\n")
    print("Something is wrong with ABC...")
    sys.exit("Check website status code")

soupABC = BeautifulSoup(urlABC.content, 'html.parser')

ABCcontainer = soupABC.find(id="row-1", class_="rows")

ABCheadline = ABCcontainer.find('h1').get_text().strip()

abcBlob = TextBlob(ABCheadline)
abcPolarity = abcBlob.sentiment.polarity
abcSubj = abcBlob.sentiment.subjectivity

print(ABCheadline)
print(abcPolarity)
print(abcSubj)
print("Done with ABC")

headlines.append(ABCheadline)
###########################Breitbart###################################################

urlBB = requests.get("https://www.breitbart.com/")
if urlBB.status_code != 200:
    print(urlBB.status_code + "\n")
    print("Something is wrong with Breitbart...")
    sys.exit("Check website status code")

soupBB = BeautifulSoup(urlBB.content, 'html.parser')

BBcontainer = soupBB.find(class_="top_article_main")

BBheadline = BBcontainer.find('h2').get_text().strip()

bbBlob = TextBlob(BBheadline)
bbPolarity = bbBlob.sentiment.polarity
bbSubj = bbBlob.sentiment.subjectivity

print(BBheadline)
print(bbPolarity)
print(bbSubj)
print("Done with BB")

headlines.append(BBheadline)
###########################BuzzFeed################################################


urlBF = requests.get("https://www.buzzfeed.com/")
if urlBF.status_code != 200:
    print(urlBF.status_code + "\n")
    print("Something is wrong with BuzzFeed...")
    sys.exit("Check website status code")

soupBF = BeautifulSoup(urlBF.content, 'html.parser')

BFcontainer = soupBF.find(class_="featured-card__body")

BFheadline = BFcontainer.find('h2').get_text().strip()

bfBlob = TextBlob(BFheadline)
bfPolarity = bfBlob.sentiment.polarity
bfSubj = bfBlob.sentiment.subjectivity

print(BFheadline)
print(bfPolarity)
print(bfSubj)
print("Done with BF")

headlines.append(BFheadline)



###########################China Daily################################################


urlCD = requests.get("http://www.chinadaily.com.cn/china/")
if urlCD.status_code != 200:
    print(urlCD.status_code + "\n")
    print("Something is wrong with China Daily...")
    sys.exit("Check website status code")

soupCD = BeautifulSoup(urlCD.content, 'html.parser')

CDcontainer = soupCD.find(class_="l490")
CDcontainer2 = CDcontainer.find(class_="tBox")

CDheadline = CDcontainer2.find('a').get_text().strip()

cdBlob = TextBlob(CDheadline)
cdPolarity = cdBlob.sentiment.polarity
cdSubj = cdBlob.sentiment.subjectivity

print(CDheadline)
print(cdPolarity)
print(cdSubj)
print("Done with CD")

headlines.append(CDheadline)

###########################Sixth Tone################################################


urlST = requests.get("http://www.sixthtone.com/")
if urlST.status_code != 200:
    print(urlST.status_code + "\n")
    print("Something is wrong with Sixth Tone...")
    sys.exit("Check website status code")

soupST = BeautifulSoup(urlST.content, 'html.parser')

STcontainer = soupST.find('main', id="main-content")
STheadline = STcontainer.find('h3', class_="heading-1").get_text().strip()


stBlob = TextBlob(STheadline)
stPolarity = stBlob.sentiment.polarity
stSubj = stBlob.sentiment.subjectivity

print(STheadline)
print(stPolarity)
print(stSubj)
print("Done with ST")

headlines.append(STheadline)


####################################The Onion########################################

urlO = requests.get("http://www.theonion.com/")
if urlO.status_code != 200:
    print(urlO.status_code + "\n")
    print("Something is wrong with The Onion...")
    sys.exit("Check website status code")

soupO = BeautifulSoup(urlO.content, 'html.parser')

Oheadline = soupO.find('h3')
Oheadline2 = Oheadline.get_text().strip()

oBlob = TextBlob(Oheadline2)
oPolarity = oBlob.sentiment.polarity
oSubj = oBlob.sentiment.subjectivity
print(Oheadline2)
print(oPolarity)
print(oSubj)
print("Done with The Onion")
headlines.append(Oheadline2)

####################################################################################




categories = []
for headline in headlines:
    #create array of words in headline
    word = ""
    words = []
    categoryTag = ""
    for char in headline:
        char = char.lower()
        if char != ' ' or char != ',':
            word += char
        else:
            words.append(word)
            word = ""
    for word in words:

        if word in politics:
            categoryTag = "politics"
            break
        elif word in sports:
            categoryTag = "sports"
            break
        elif word in international:
            categoryTag = "international"
            break
        elif word in environment:
            categoryTag = "environment"
            break
        elif word in technology:
            categoryTag = "technology"
            break
        else:
            continue

    if categoryTag == "":
        categoryTag = "miscellaneous"
    
    categories.append(categoryTag)

foxCategory = categories[0]
nbcCategory = categories[1]
wpCategory = categories[2]
abcCategory = categories[3]
bbCategory = categories [4]
bfCategory = categories[5]
cdCategory = categories[6]
stCategory = categories[7]
oCategory = categories[8]


#rounding polarities and subjectivities to 2 decimal places

foxPolarity = round(foxPolarity,2)
nbcPolarity = round(nbcPolarity,2)
abcPolarity = round(abcPolarity,2)
wpPolarity = round(wpPolarity,2)
bbPolarity = round(bbPolarity,2)
bfPolarity = round(bfPolarity,2)
cdPolarity = round(cdPolarity,2)
stPolarity = round(stPolarity,2)
oPolarity = round(oPolarity, 2)

foxSubj = round(foxSubj,2)
nbcSubj = round(nbcSubj,2)
abcSubj = round(abcSubj,2)
wpSubj = round(wpSubj,2)
bbSubj = round(bbSubj,2)
bfSubj = round(bfSubj,2)
cdSubj = round(cdSubj,2)
stSubj = round(stSubj,2)
oSubj = round(oSubj, 2)

#write webscraped data to csv file for viz
#order should be: date, source, headline, polarity, subj, cat

#in the future, only write data if data for that source exists
with open('flat_file.csv', mode='a', newline='') as destFile:
    writer = csv.writer(destFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['\n'])
    #Fox
    writer.writerow([today, 'Fox', FOXheadline, foxPolarity, foxSubj, foxCategory])
    #NBC
    writer.writerow([today, 'NBC', NBCheadline, nbcPolarity, nbcSubj, nbcCategory])
    #WP
    writer.writerow([today, 'Washington Post', WPheadline, wpPolarity, wpSubj, wpCategory])
    #ABC
    writer.writerow([today, 'ABC', ABCheadline, abcPolarity, abcSubj, abcCategory])
    #BB
    writer.writerow([today, 'Breitbart', BBheadline, bbPolarity, bbSubj, bbCategory])
    #BF
    writer.writerow([today, 'Buzzfeed', BFheadline, bfPolarity, bfSubj, bfCategory])
    #CD
    writer.writerow([today, 'China Daily', CDheadline, cdPolarity, cdSubj, cdCategory])
    #ST
    writer.writerow([today, 'Sixth Tone', STheadline, stPolarity, stSubj, stCategory])
    #O
    writer.writerow([today, 'The Onion', Oheadline2, oPolarity, oSubj, oCategory])











