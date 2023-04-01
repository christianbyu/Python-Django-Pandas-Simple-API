from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/csv')
def get_csv_data():
    df = pd.read_csv('sample_data.csv') # Replace 'data.csv' with the path to your CSV file
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
