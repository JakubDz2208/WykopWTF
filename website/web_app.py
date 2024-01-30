from flask import Flask, render_template, request, jsonify
import sys
import os
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_path)

from model.model_api import GPTModel
from scraper.scraper import CommentScraper

app = Flask(__name__, static_folder='static')

# Set your OpenAI API key
OPENAI_API_KEY = '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'
gpt_instance = GPTModel(api_key=OPENAI_API_KEY)

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

        # Generate prompts for each comment
        generated_prompts = []
        for comment in scraped_comments['Comment']:
            prompt = gpt_instance.generate_response(f"Odpowiedz Tak lub Nie, czy ten tekst jest nacechowany negatywnie? {comment}")
            generated_prompts.append(prompt)

        # Assign generated prompts to the DataFrame
        scraped_comments['Generated_Prompts'] = generated_prompts

        # Return the DataFrame as JSON
        return jsonify({'comments': scraped_comments.to_dict(orient='records')})
    else:
        return jsonify({'error': 'Invalid parameters'})

if __name__ == '__main__':
    app.run(debug=True)