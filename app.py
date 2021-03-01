import re
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from flask import Flask, url_for, render_template, request
from markupsafe import escape



options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe", options=options)


app = Flask(__name__)   


@app.route('/')
def football():
    return render_template('interface.html')


new_word = ''
def synonym(word):
    try:
        driver.get(f'https://www.thesaurus.com/browse/{word}?s=t')

        click = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/main/section/section/div[2]/div[2]/ul/li[1]/a')
        new_word = click.text
        return new_word
    except:
        pass
@app.route('/main/<topic>/<lang>/<plag>')
def soccer(topic, lang, plag):

    try:
        random_num = random.randrange(6, 10)

        driver.get(f'https://{lang}.wikipedia.org/wiki/{topic}')

        y = 0
        new = []
        for i in range(1, random_num):
            text = driver.find_element_by_xpath(
                '//*[@id="mw-content-text"]/div[1]/p[' + str(i) + ']').text

            delimiters = '[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[7]', '[8]', '[9]', '[10]', '[11]', '[12]', '[13]', '[14]', '[15]', '[16]', '[17]', '[18]', '[19]', '[20]', '[21]', '[22]', '[23]', '[24]', '[25]', '[26]', '[27]', '[28]', '[29]', '[30]', '[31]', '[32]', '[33]', '[34]', '[35]', '[36]', '[37]', '[38]', '[39]', '[40]', '[41]', '[42]', '[43]', '[44]', '[45]', '[46]', '[47]', '[48]', '[49]', '[50]', '[51]', '[52]', '[53]', '[54]', '[55]', '[56]', '[57]', '[58]', '[59]', '[60]', '[61]', '[62]', '[63]', '[64]', '[65]', '[66]', '[67]', '[68]', '[69]', '[70]', '[71]', '[72]', '[73]', '[74]', '[75]', '[76]', '[77]', '[78]', '[79]', '[80]', '[81]', '[82]', '[83]', '[84]', '[85]', '[86]', '[87]', '[88]', '[89]', '[90]', '[91]', '[92]', '[93]', '[94]', '[95]', '[96]', '[97]', '[98]', '[99]'
            regexPattern = '|'.join(map(re.escape, delimiters))
            new += re.split(regexPattern, text)

            new_text = ''
            for x in new:
                new_text += x

            new_new_text = new_text.split()
            for bob in new_new_text:
                if i == (random_num - 1):
                    y += 1



        text = str(new_text)

        if plag == 'yes':
            text1 = text.split()
            win = -1
            for i in text1:
                win += 1
                if win % 6 == 0:
                    try:
                        nums = 0
                        for x in i:
                            nums += 1
                            
                        if nums <= 3:
                            pass
                        else:
                            driver.get(f'https://www.thesaurus.com/browse/{i}?s=t')

                            click = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/main/section/section/div[2]/div[2]/ul/li[1]/a')
                            text1[win] = click.text

                    except:
                        pass


            string = ''
            for i in text1:
                string += (i + ' ')



            return render_template('interface2.html', content=string, topic=topic, cont=y)

        else:
            return render_template('interface2.html', content=text, topic=topic, cont=y)
    except:
        return render_template('interface3.html')


@app.route('/contact')
def contact():
    return render_template('interface4.html')
