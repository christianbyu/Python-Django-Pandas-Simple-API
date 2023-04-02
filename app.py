from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/csv')
def get_csv_data():
    df = pd.read_csv('./data/sample_data.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/newsapi')
def get_news_data():
    df = pd.read_csv('./data/company_sales_data.csv')
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
