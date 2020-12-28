import subprocess

def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    command = ['scanimage',
               '--format', 'tiff',
               '--resolution', '300',
               '--source', 'ADF Duplex',
               '--page-width', '210',
               '--page-height', '297',
               '--ald=yes',
               '-d', 'fujitsu:ScanSnap iX500:1201996',
               '--batch=./%02d.tiff']
    subprocess.check_output(command,
                            stderr=subprocess.STDOUT)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
