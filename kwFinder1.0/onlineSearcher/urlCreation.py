class UrlCreation:
    url = ""

    def __init__(self, language, type, keyword, country):
        setlanguage(language)
        settype(type)
        setkeyword(keyword)
        setcountry(country)


def setlanguage(language):
    UrlCreation.url = "https://app.neilpatel.com/" + language


def settype(type):
    UrlCreation.url = UrlCreation.url + "/ubersuggest/" + type


def setkeyword(keyword):
    UrlCreation.url = UrlCreation.url + "?keyword=" + keyword


def setcountry(country):
    UrlCreation.url = UrlCreation.url + "&country=" + country


#UrlCreation("com", "overview", "tisch", "de")
#print(UrlCreation.url)
