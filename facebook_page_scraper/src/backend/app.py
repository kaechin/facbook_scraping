from flask import Flask, request, send_from_directory, jsonify
import os
import kristiania_project
import hashtag
from flask_cors import CORS
import time

app = Flask(__name__, static_folder='build/static', template_folder='build')
CORS(app)

@app.route('/api/search', methods=['POST', 'OPTIONS'])
def serve():
    return send_from_directory(app.template_folder, 'index.html')

@app.route('/api/search')
def search():
    query = request.args.get('q')
    start_date = request.args.get('start_date')
    if not query:
        return jsonify({"status": "error", "message": "Missing parameter: q"}), 400
    
    start_date = request.args.get('start_date', "2023-07-01")
    
    # Using an absolute path
    absolute_path = os.path.abspath(f"{query}.csv")
    print(f"Checking for file at: {absolute_path}")  # This will log the exact path it's looking at

    if os.path.exists(absolute_path):
        return jsonify({"status": "success", "message": "Data already exists"}), 200

    try:
        # scrape
        kristiania_project.scrape(query, start_date)
        
        # Wait for a couple of seconds to let the file system recognize the file
        time.sleep(2)

        if os.path.exists(absolute_path):
            print(f"Successfully scraped and found file for {query}")
            return jsonify({"status": "success", "message": "Scrape done"}), 200
        else:
            print(f"Current working directory: {os.getcwd()}")
            print(f"Expected file {query}.csv not found!")
            raise ValueError("Scraped file not found after scraping process")

    except Exception as e:
        # if str(e) == "Scraped file not found after scraping process":
        #     return jsonify({"status": "error", "message": "User is not valid. Please enter a valid user."}), 400
        # else:
        #     return jsonify({"status": "failed", "message": f"Scraping failed due to: {str(e)}"}), 500
        return jsonify({"status": "failed", "message": f"Scraping failed due to: {str(e)}"}), 500

@app.route('/api/download/<filename>', methods=['GET'])
def download(filename):
    return send_from_directory(os.getcwd(), filename, as_attachment=True)

@app.route('/api/hashtags')
def extract_hashtags():
    username = request.args.get('username')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    at_hashtags = request.args.get('at_hashtags')
    hash_hashtags = request.args.get('hash_hashtags')

    # Insert your log statement here if you want to print the username to the console
    print(f"Received username: {username}, {start_date}, {end_date}, {at_hashtags}, {hash_hashtags}")
    
    if not username or username == 'undefined':
        return jsonify({"status": "error", "message": "Invalid username parameter received"}), 400

    if not username or not start_date or not end_date:
        return jsonify({"status": "error", "message": "Missing parameters."}), 400
    
    try:
        result_message = hashtag.hashtag(username, start_date, end_date, at_hashtags, hash_hashtags)
        return jsonify({"status": "success", "message": result_message}), 200

    except Exception as e:
        return jsonify({"status": "failed", "message": f"Hashtag extraction failed due to: {str(e)}"}), 500


@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.template_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)