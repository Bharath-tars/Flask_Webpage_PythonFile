from flask import Flask, render_template, request
from process import doit
from datetime import datetime
import os

app = Flask(__name__)

# Set the directory for storing uploaded files
app.config['UPLOAD_FOLDER'] = 'pics'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['name']
    email = request.form['email']
    phoneno = request.form['phno']
    file = request.files['file']
    filename = f"{name}_{email}_{phoneno}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    with open('data.txt', 'a') as np:
        np.writelines(f"{name} - {email} - {phoneno} | ")
    doit(name, email, phoneno)
    return render_template('pass.html', n=name, e=email, p=phoneno)

if __name__ == '__main__':
    app.run(debug=True)
