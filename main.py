from flask import Flask, send_file, render_template
import subprocess
import os
import shutil


app = Flask(__name__, static_folder='dist', static_url_path='')


@app.route('/')
def index():
    return send_file('dist/index.html')


@app.route('/api/v1.0/scan')
def main():

    # Create out dir
    directory = '.scan/'
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.mkdir(directory)

    # compile scan command
    command = ['scanimage',
               '--format', 'tiff',
               '--resolution', '300',
               '--source', 'ADF Duplex',
               '--page-width', '210',
               '--page-height', '297',
               '--ald=yes',
               '--device-name', 'fujitsu:ScanSnap iX500:1201996',
               f'--batch={directory}%02d.tiff']

    # scan
    subprocess.check_output(command,
                            stderr=subprocess.STDOUT)

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

