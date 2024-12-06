from flask import Flask, request, jsonify
from ytube_api import Auto

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Please provide a name parameter"}), 400

    try:
        # Initialize Auto with the query and format
        Auto(query=name, format="mp3")
        
        # Return the download link
        return jsonify({"downloadlink": "/download?now"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
