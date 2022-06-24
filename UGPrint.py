import requests
from bs4 import BeautifulSoup as bs
import json
from flask import Flask,render_template, request

app = Flask(__name__)

def get_tab(tab_url):
    try:
        code = requests.get(tab_url)
        soup = bs(code.text, 'html.parser')

        js = soup.find('div', class_='js-store').attrs['data-content']
        content = json.loads(js)
        tab = content['store']['page']["data"]["tab_view"]['wiki_tab']['content']

        tab = tab.replace('[tab]', '').replace(
            '[/tab]', '').replace('[ch]', '').replace('[/ch]', '')
    except:
        return "Error Loading Tab"
    return tab

@app.route('/')
def index():
    return render_template('index.html', content=None)

@app.route('/getTab', methods=['POST'])
def get_tab_route():
    if request.method == 'POST':
        url = request.form['url']
        return get_tab(url.replace('"',''))

if __name__ == '__main__':
    app.run(debug=True)

