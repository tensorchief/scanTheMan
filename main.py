import subprocess
import os
import shutil

def main(directory='.scan/'):

    # Create out dir
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
