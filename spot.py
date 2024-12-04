from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/downloadSong', methods=['GET'])
def download_song():
    songId = request.args.get('songId')
    url = "https://spotify-downloader9.p.rapidapi.com/downloadSong"
    headers = {
        "X-Rapidapi-Key": os.getenv("X_RAPIDAPI_KEY"),
        "X-Rapidapi-Host": os.getenv("X_RAPIDAPI_HOST"),
        "Host": os.getenv("X_RAPIDAPI_HOST")
    }
    params = {"songId": songId}
    response = requests.get(url, headers=headers, params=params)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
