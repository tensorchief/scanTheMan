from flask import Flask, send_file, request
from flask_cors import CORS
import subprocess
import os
import shutil

app = Flask(__name__, static_folder='dist', static_url_path='')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

sources = [
    {'value': 'ADF Duplex', 'text': 'duplex'},
    {'value': 'ADF Front', 'text': 'front'},
    {'value': 'ADF Back', 'text': 'back'}
]


@app.route('/')
def index():
    return send_file('dist/index.html')


@app.route('/api/options')
def get_options():
    return {'sources': sources}


@app.route('/api/v1.0/scan')
def main():
    if request.args.get('source') and request.args.get('source') not in [item['value'] for item in sources]:
        return 'Invalid source', 400

    # Create out dir
    directory = '.scan/'
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.mkdir(directory)

    # compile scan command
    command = ['scanimage',
               '--format', 'tiff',
               '--resolution', '300',
               '--source', request.args.get('source', sources[0]['value']),
               '--page-width', '210',
               '--page-height', '297',
               '--ald=yes',
               '--device-name', 'fujitsu:ScanSnap iX500:1201996',
               f'--batch={directory}%02d.tiff']

    # scan
    result = subprocess.run(command,
                            stderr=subprocess.STDOUT)
    if result.returncode:
        if result.returncode == 7:
            return 'Document feeder out of documents.', 502
        if result.returncode == 1:
            return 'Device not found.', 503
        return '', 500

    # convert to PDF
    command = ['convert',
               f'{directory}*.tiff',
               f'{directory}outfile.pdf']
    subprocess.check_output(command,
                            stderr=subprocess.STDOUT)

    return send_file(f'{directory}outfile.pdf', attachment_filename='outfile.pdf')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()
