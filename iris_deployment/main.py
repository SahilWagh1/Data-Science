from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        values = [request.form[f'field{i}'] for i in range(1, 5)]
        input_data = np.array(values, dtype=float).reshape(1, -1)
        result = model.predict(input_data)
        result = result[0]
    return render_template('index.html', result=result)
if __name__ == '__main__':
    app.run(debug=True)
