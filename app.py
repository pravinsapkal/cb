import os
from flask import Flask, render_template, request, jsonify

import chat

app = Flask(__name__)

@app.route("/predict", methods = ['POST'])
def predict():
    ans_pdc = sentence = ''
    if request.method == "POST":
        sentence = request.form["que"]
        if sentence != '':
            ans_pdc = chat.ans_prediction(sentence)

    data = {'que': sentence, 'prediction': ans_pdc}
    return jsonify(data)

@app.route("/", methods = ['GET', 'POST'])
def hello():
    ans_pdc = sentence = ''
    if request.method == "POST":
        sentence = request.form["que"]
        if sentence != '':
            ans_pdc = chat.ans_prediction(sentence)

    return render_template("index.html", que = sentence, pred = ans_pdc)

#if __name__ == "__main__":
#    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
