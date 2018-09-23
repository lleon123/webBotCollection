class UrlCreation:
    urlubersuggest = ""
    urlonekeyword = ""
    urlkeywordlist = ""

    def __init__(self, language, type, keyword, country):
        setlanguage(language)
        settype(type)
        setkeyword(keyword)
        setcountry(country)
        seturlonekeyword(language, keyword)
        seturlkeywordlist(language, keyword)


def setlanguage(language):
    UrlCreation.urlubersuggest = "https://app.neilpatel.com/" + language


def settype(type):
    UrlCreation.urlubersuggestl = UrlCreation.urlubersuggest + "/ubersuggest/" + type


def setkeyword(keyword):
    UrlCreation.urlubersuggest = UrlCreation.urlubersuggest + "?keyword=" + keyword


def setcountry(country):
    UrlCreation.urlubersuggest = UrlCreation.urlubersuggest + "&country=" + country


def seturlkeywordlist(language, keyword):
    UrlCreation.urlkeywordlist = "https://qdjnvxwje1.execute-api.us-east-1.amazonaws.com/blue/keyword_ideas?query=" + keyword + "&language=" + language + "&country=" + "de" + "&google=http:%2F%2Fwww.google.com&service=0"


def seturlonekeyword(language, keyword):
    UrlCreation.urlonekeyword = "https://qdjnvxwje1.execute-api.us-east-1.amazonaws.com/blue/keyword_info?keyword=" + keyword + "&language=" + language + "&country=de"


def geturlubersuggest():
    return UrlCreation.urlubersuggest


def geturlonekeyword():
    return UrlCreation.urlonekeyword


def geturlkeywordlist():
    return UrlCreation.urlkeywordlist
# UrlCreation("de", "overview", "stuhl test", "de")
# print(UrlCreation.urlonekeyword)
