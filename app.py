from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    url = "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_156382517509.html"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Exemple : Trouver tous les titres h2 sur la page
        titles = soup.find_all('h2')
        titles_text = [title.text for title in titles]
        return jsonify(titles_text)
    else:
        return jsonify({"error": "Échec de la requête"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
