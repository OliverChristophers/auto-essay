import re
from flask import Flask, url_for, render_template, request
from markupsafe import escape
import requests
from bs4 import BeautifulSoup   



app = Flask(__name__)   


@app.route('/')
def football():
    return render_template('interface.html')



@app.route('/main/<topic>/<lang>/<plag>')
def soccer(topic, lang, plag):

    try:
        page = requests.get(f'https://{lang}.wikipedia.org/wiki/{topic}')
        soup = BeautifulSoup(page.content, 'html.parser')


        p = soup.find('div', class_='mw-parser-output')

        y = -1
        text = ''
        for i in p:
            y += 1
            x = soup.find_all('p')[y]
            text += (x.get_text() + ' ')
            if y == 7:
                break


        new = []
        delimiters = '[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[7]', '[8]', '[9]', '[10]', '[11]', '[12]', '[13]', '[14]', '[15]', '[16]', '[17]', '[18]', '[19]', '[20]', '[21]', '[22]', '[23]', '[24]', '[25]', '[26]', '[27]', '[28]', '[29]', '[30]', '[31]', '[32]', '[33]', '[34]', '[35]', '[36]', '[37]', '[38]', '[39]', '[40]', '[41]', '[42]', '[43]', '[44]', '[45]', '[46]', '[47]', '[48]', '[49]', '[50]', '[51]', '[52]', '[53]', '[54]', '[55]', '[56]', '[57]', '[58]', '[59]', '[60]', '[61]', '[62]', '[63]', '[64]', '[65]', '[66]', '[67]', '[68]', '[69]', '[70]', '[71]', '[72]', '[73]', '[74]', '[75]', '[76]', '[77]', '[78]', '[79]', '[80]', '[81]', '[82]', '[83]', '[84]', '[85]', '[86]', '[87]', '[88]', '[89]', '[90]', '[91]', '[92]', '[93]', '[94]', '[95]', '[96]', '[97]', '[98]', '[99]'
        regexPattern = '|'.join(map(re.escape, delimiters))
        new += re.split(regexPattern, text)

        new_text = ''
        for x in new:
            new_text += x
    
        text = str(new_text)

        y = 0
        tru = text.split()
        for u in tru:
            y += 1

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
                            page1 = requests.get(f'https://www.thesaurus.com/browse/{i}')
                            soup = BeautifulSoup(page1.content, 'html.parser')


                            pi = soup.find('div', id='meanings').get_text()


                            new_pi = pi.split('RELEVANT')

                            pie = ''
                            for c in new_pi:
                                pie += c

                            ULTRAnew_pi = c.split()

                            click = ULTRAnew_pi[0]
                            text1[win] = click

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



