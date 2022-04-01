from flask import Flask, render_template, request
from util import utils
app = Flask(__name__)

'''
pip install virtualenv
python3 -m venv env
pip install flask
'''

@app.route('/', methods=['GET', 'POST'])
def main():
    if(request.method == 'POST'):
        text = request.form.get('para')
        word = utils.words(text)
        char = utils.characters(text)
        sentences = utils.sentences(text)
        f_c = utils.frequency_char(text)
        f_w = utils.frequency_word(text)

        return render_template('report.html', text=text, words=word, characters=char, 
                    sentences=sentences, frequency_char=f_c, frequency_word=f_w)

    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()