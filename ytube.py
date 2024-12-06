from flask import Flask, request, jsonify
from ytube_api import Ytube

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_video():
    # Get the 'url' query parameter from the request
    video_name = request.args.get('url', type=str)

    if not video_name:
        return jsonify({"error": "No video name provided"}), 400

    try:
        # Initialize Ytube API
        yt = Ytube()
        
        # Search for the video using the provided name
        search_results = yt.search_videos(video_name)
        
        # Check if there are search results
        if not search_results.items:
            return jsonify({"error": "No videos found for the search query"}), 404
        
        # Get the first video result
        target_video = search_results.items[0]
        
        # Get the download link for the video in mp3 format and 320 quality
        download_link = yt.get_download_link(target_video, format="mp3", quality="320")
        
        # Return the download link in the response
        return jsonify({"video_name": target_video.title, "download_link": download_link})

    except Exception as e:
        # Return any error message as a response
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
