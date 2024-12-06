from flask import Flask, request, jsonify
from ytube_api import Ytube
import time
import os
import sys
import logging

# Initialize the Flask app
app = Flask(__name__)

# Set up logging with an ASCII format
log_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
logger = logging.getLogger()

# Define the route for downloading videos
@app.route('/download', methods=['GET'])
def download_video():
    # Get the 'url' query parameter from the request
    video_name = request.args.get('url', type=str)

    # Log the incoming request
    logger.info("Received request for video: %s", video_name)
    
    if not video_name:
        logger.warning("No video name provided.")
        return jsonify({"error": "No video name provided"}), 400

    try:
        # Initialize Ytube API
        yt = Ytube()
        
        # Search for the video using the provided name
        logger.info("Searching for videos with name: %s", video_name)
        search_results = yt.search_videos(video_name)
        
        # Check if there are search results
        if not search_results.items:
            logger.warning("No videos found for the search query: %s", video_name)
            return jsonify({"error": "No videos found for the search query"}), 404
        
        # Get the first video result
        target_video = search_results.items[0]
        logger.info("Found video: %s", target_video.title)
        
        # Get the download link for the video in mp3 format and 320 quality
        download_link = yt.get_download_link(target_video, format="mp3", quality="320")
        
        # Log the download link
        logger.info("Download link for video '%s': %s", target_video.title, download_link)

        # Return the download link in the response
        response = jsonify({"video_name": target_video.title, "download_link": download_link})
        
        # Wait for 2 minutes before rebooting
        logger.info("Waiting for 2 minutes before rebooting the system...")
        time.sleep(120)  # Sleep for 120 seconds (2 minutes)
        
        # Reboot the system
        if sys.platform == 'win32':
            logger.info("Rebooting the system (Windows)...")
            os.system('shutdown /r /f /t 0')  # Windows reboot command
        else:
            logger.info("Rebooting the system (Linux/macOS)...")
            os.system('reboot')  # Linux/Mac reboot command
        
        return response

    except Exception as e:
        # Log any error that occurs during the process
        logger.error("Error occurred: %s", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0 and port 5000
    logger.info("Starting Flask application...")
    app.run(host='0.0.0.0', port=5000, debug=True)
