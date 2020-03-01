# -*- coding: utf-8 -*-

import os
import zipfile

def zip(source, dest):
    with zipfile.ZipFile(dest, 'w') as zf:
        for folder, subfolders, files in os.walk(source):
            for file in files:
                abspath = os.path.join(folder, file)
                relpath = os.path.relpath(abspath, source)
                zf.write(abspath, relpath, compress_type = zipfile.ZIP_DEFLATED)

        zf.close()

    print('ZIP\t|', os.path.split(dest)[-1])

def unzip(source, dest):
    with zipfile.ZipFile(source, 'r') as zf:
        zf.extractall(dest)
        zf.close()

    print('Unzip\t|', os.path.split(dest)[-1])

if __name__ == '__main__':
    print('<MENU>'.center(20, '-') + \
          '\n' + \
          '1) Zip\n' + \
          '2) Unzip\n')
    menu     = input('MENU : ')
    basepath = input('PATH : ')

    try:
        for file in os.listdir(basepath):
            source = os.path.join(basepath, file)

            if menu == '1' and os.path.isdir(source):
                destfile = source + '.zip'

                if not os.path.exists(destfile):
                    zip(source, destfile)
                else:
                    print('EXISTS\t|', file + '.zip')
            elif menu == '2' and os.path.splitext(source)[-1] == '.zip':
                folder = source[:source.rfind('.')]

                if not os.path.exists(folder):
                    unzip(source, folder)
                else:
                    print('EXISTS\t|', file[:file.rfind('.')])
    except os.error:
        print('Failed! Input right PATH.')
