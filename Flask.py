from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'BankNote_Authentication'

pickle_in = open('picklefile.pkl','rb')
classifier = pickle.load(pickle_in)


@app.route('/')
def land():
    return render_template('land.html')

@app.route('/Authentication',methods=['POST','GET'])
def bank_note_authentication():
    if request.method == 'POST':
        variance = float(request.form['variance'])
        skewness = float(request.form['skewness'])
        curtosis = float(request.form['curtosis'])
        entropy = float(request.form['entropy'])
        pred = classifier.predict([[variance,skewness,curtosis,entropy]])   
        if (pred == 1):
            return render_template('approved.html')
        else:
            return render_template('unapproved.html')    

    else:
        return render_template('value.html')

@app.route('/File_Authentication',methods=["POST",'GET'])
def bank_note_authentication2():
    if request.method == 'POST':
        test = pd.read_csv(request.files["file"])
        pred = classifier.predict(test).tolist()
        outcomes = len(pred)
        return render_template('fileoutcome.html',pred=pred, outcomes=outcomes)
    else:
        return render_template('file.html')


if __name__ == '__main__':
    app.run(debug=True)
