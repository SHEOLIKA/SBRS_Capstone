from flask import Flask, jsonify,  request, render_template

import numpy as np
from model import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if (request.method == 'POST'):
        user_name = [x for x in request.form.values()]
        if validate_user(user_name[0]):
            final_recomm = recommendation(user_name[0])
            final_file = final_recomm.to_json(orient = 'records')
        else:
            final_file = 'User_name is not valid'
        return render_template('index.html', prediction_text='Product Recommendation {}'.format(final_file))

    else :
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)