from flask import Flask, request, jsonify
import os
from matcher import compare_voices
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/compare', methods=['POST'])
def compare():
    if 'voice1' not in request.files or 'voice2' not in request.files:
        return jsonify({'error': 'Missing audio files'}), 400

    voice1 = request.files['voice1']
    voice2 = request.files['voice2']

    filename1 = secure_filename("original.3gp")
    filename2 = secure_filename("new_voice.3gp")

    path1 = os.path.join(UPLOAD_FOLDER, filename1)
    path2 = os.path.join(UPLOAD_FOLDER, filename2)

    voice1.save(path1)
    voice2.save(path2)

    is_match = compare_voices(path1, path2)

    return jsonify({'match': is_match}), 200

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
