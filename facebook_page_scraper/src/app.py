from flask import Flask, render_template, request
import os
import kristiania_project

app = Flask(__name__)

@app.route('/api/search')
def index():
    query = request.args.get('q')
    if not query:
        return f"There is no query. q=name"
    
    start_date = request.args.get('start_date')
    if not start_date:
        start_date = "2023-07-01"
    
    path = f"csv_folder/{query}.csv"
    if os.path.exists(path):
        with open(path, "r") as file:
            return file.read()

    # scrape
    kristiania_project.scrape(query, start_date)

    if os.path.exists(path):
        with open(path, "r") as file:
            return file.read()
    
    return "Scrape done"


if __name__ == '__main__':
    app.run(debug=True)