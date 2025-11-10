import os
import pickle
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Đảm bảo load model từ đúng thư mục
base_path = os.path.dirname(__file__)

models = {
    'Naive Bayes': pickle.load(open(os.path.join(base_path, 'naive_bayes_model.pkl'), 'rb')),
    'Decision Tree': pickle.load(open(os.path.join(base_path, 'decision_tree_model.pkl'), 'rb')),
    'Bagging': pickle.load(open(os.path.join(base_path, 'bagging_model.pkl'), 'rb')),
    'Logistic': pickle.load(open(os.path.join(base_path, 'logistic_model.pkl'), 'rb')),
    'Random Forest': pickle.load(open(os.path.join(base_path, 'Random_Forest_model.pkl'), 'rb')),
}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            perimeter = float(request.form['perimeter'])
            major_axis_length = float(request.form['major_axis_length'])
            minor_axis_length = float(request.form['minor_axis_length'])
            eccentricity = float(request.form['eccentricity'])
            convex_area = float(request.form['convex_area'])
            extent = float(request.form['extent'])
            algorithm = request.form['algorithm']

            input_data = [[perimeter, major_axis_length, minor_axis_length,
                           eccentricity, convex_area, extent]]
            prediction = models[algorithm].predict(input_data)[0]
        except Exception as e:
            flash(str(e))
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
