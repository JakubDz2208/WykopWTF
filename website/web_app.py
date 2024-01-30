from flask import Flask, render_template, request, jsonify
import os
import sys
import joblib

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_path)
from scraper.scraper import CommentScraper

app = Flask(__name__, static_folder='static')

model = joblib.load('model/model.joblib')
tfidf_vectorizer = joblib.load('model/tfidf_vectorizer.joblib')

@app.route('/')
def index():
    return render_template('template.html')

@app.route('/api/scrape_comments', methods=['POST'])
def api_scrape_comments():
    data = request.get_json()
    url = data.get('url', '')
    limit = data.get('limit', None)

    if url:
        scraper = CommentScraper(url, comments_selector=".wrapper")  # Adjust the selector accordingly
        scraped_comments = scraper.scrape_comments(limit=int(limit) if limit else None)
        
        comments_tfidf = tfidf_vectorizer.transform(scraped_comments['Comment'])

        predictions = model.predict(comments_tfidf)

        # Assign predictions to the DataFrame
        scraped_comments['Predictions'] = predictions
        print(scraped_comments)

        # Return the DataFrame as JSON
        return jsonify({'comments': scraped_comments.to_dict(orient='records')})
    else:
        return jsonify({'error': 'Invalid parameters'})

if __name__ == '__main__':
    app.run(debug=True)

