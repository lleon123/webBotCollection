import selenium.webdriver as sl
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
import time
import urlCreation


class CsvDownload:
    driver = ""
    error = 0

    def __init__(self, urltofirefoxprofile, urltocsvfolder, keyword):
        self.urltofirefoxprofile = urltofirefoxprofile
        self.urltocsvfolder = urltocsvfolder
        self.keyword = keyword
        errorchecker(urltofirefoxprofile, urltocsvfolder, keyword)
        download()


def startbrowser(urltofrefoxprofile, urltocsvfolder, keyword):
    options = Options()
    options.set_headless(headless=False)
    fp = sl.FirefoxProfile(urltofrefoxprofile)
    fp.set_preference("browser.download.dir", urltocsvfolder)
    CsvDownload.driver = sl.Firefox(firefox_profile=fp, firefox_options=options)
    urlCreation.UrlCreation("com", "keyword_ideas", keyword, "de")
    print(urlCreation.UrlCreation.url)
    CsvDownload.driver.get(urlCreation.UrlCreation.url)


def download():
    timer = 0
    while timer < 20:
        try:
            elLanguage = CsvDownload.driver.find_element_by_xpath(
                "/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[4]/button[1]")
            elLanguage.send_keys(Keys.ENTER)
            text = elLanguage.text
            print(text)
            time.sleep(1)
            timer = 1000
        except WebDriverException:
            time.sleep(1)
            timer = timer + 1

    if timer < 1000:
        CsvDownload.driver.quit()


def errorchecker(urltofrefoxprofile, urltocsvfolder, keyword):
    try:
        startbrowser(urltofrefoxprofile, urltocsvfolder, keyword)
    except WebDriverException:
        CsvDownload.driver.quit()
        CsvDownload.error = 1


CsvDownload("/run/media/leonl/Data/KW_Crawler/Profiles/US/", "/run/media/leonl/Data/KW_Crawler/CSV_Files/", "elegoo")
