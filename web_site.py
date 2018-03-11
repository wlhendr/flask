from flask import Flask, render_template, url_for, request

app = Flask(__name__)

image = [['#FFFFFF', '#000000'],
        ['#000000', '#FFFFFF']]

def get_rgb(row, col):
    #temp = ''
    #temp = temp + str(row) + ' ' + str(col)
    return image[row,col]

@app.route("/", methods = ['POST', 'GET'])
def hello(color = None):
    if request.method == 'POST':
        row = request.form['row']
        col = request.form['col']
        #return row
        #print row
        #print col
        #print image[0][0]
        color = image[0][0]
        return render_template('full_screen.html', color = color)
        #return get_rgb(row, col)
        #return 'potato'
    else:
        return render_template('web_site.html')

if __name__ == "__main__":
    app.run();
