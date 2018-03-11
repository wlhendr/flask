from flask import Flask, render_template, url_for, request
from flask import jsonify



app = Flask(__name__)

image = [['#522D80', '#F66733'],
        ['#F66733', '#522D80']]

@app.route('/refresh')
def refresh():
    update = make_summary()
    return jsonify()

def get_rgb(row, col):
    #temp = ''
    #temp = temp + str(row) + ' ' + str(col)
    return image[row,col]

@app.route("/", methods = ['POST', 'GET'])
def hello(color = None):
    if request.method == 'POST':
        row = request.form['row']
        col = request.form['col']
        color = image[int(row)][int(col)]
        print row
        print col
        return render_template('full_screen.html', color = color)
        #return get_rgb(row, col)
        #return 'potato'
    else:
        return render_template('web_site.html')


if __name__ == "__main__":
    app.run();
