import urllib.request
import time

contents = urllib.request.urlopen(
    "https://qdjnvxwje1.execute-api.us-east-1.amazonaws.com/blue/keyword_ideas?query=tisch123&language=de&country=de&google=http:%2F%2Fwww.google.com&service=0").read().decode(
    'utf-8')
competition = []
volume = []
keyword = []
stri = "Geeka:sjkdj:skjdkj"
array = list(contents.split(","))
length = len(array)
counter = 0
starttime = time.time()


def transformcode(arrayword, word, count, string):
    if word in arrayword[count]:
        newstr = arrayword[count].replace("{", "")
        newstr1 = newstr.replace('"', '')
        newstr2 = newstr1.replace("results: [", "")
        newstr3 = newstr2.replace(word + ":", "")
        newstr4 = newstr3.replace(" ", "")
        newstr5 = newstr4.replace("\\u00e4", "ä")
        newstr6 = newstr5.replace("\\u00f6", "ö")
        newstr7 = newstr6.replace("\\u00fc", "ü")
        newstr8 = newstr7.replace("\\u00df", "ß")
        string.append(newstr8)


while counter < length:
    transformcode(array, "competition", counter, competition)
    transformcode(array, "volume", counter, volume)
    transformcode(array, "keyword", counter, keyword)
    counter = counter + 1
endtime = time.time() - starttime
print(endtime)
print(keyword)
