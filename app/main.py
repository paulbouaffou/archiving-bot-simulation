from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

data_store = []  # Stocke les données temporairement

# Fonction pour archiver une URL via Wikiwix
def archive_url(url):
    archive_service = "http://archive.wikiwix.com/cache/?url="
    return archive_service + url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        value = request.form['value']
        ref_url = request.form['ref_url']
        archived_url = archive_url(ref_url)
        
        data_entry = {
            "value": value,
            "reference": {
                "original": ref_url,
                "archived": archived_url
            }
        }
        data_store.append(data_entry)
        return redirect(url_for('index'))
    
    return render_template('index.html', data_store=data_store)

if __name__ == '__main__':
    app.run(debug=True)