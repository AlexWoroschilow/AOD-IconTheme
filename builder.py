import os
import sys
import glob
import optparse
from lxml import etree
import copy
from PyQt5 import QtSvg
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore


def render_color(source=None, ignores=[]):
    try:

        for pattern in ignores:
            if source.find(pattern) == -1:
                continue
            return False

        with open(source, 'r+') as stream:

            tree = etree.parse(stream)
            stream.close()
            root = tree.getroot()
            for child in root:
                style = child.get('style')
                if style is not None and len(style):
                    continue

                child.set('color', '#53b7ec')
                child.set('fill', '#53b7ec')

            with open(source, 'wb') as stream:
                stream.write(etree.tostring(root))
                stream.close()

    except Exception as ex:
        print(ex)
    return True


def render_png(source=None, destination=None, size=None):
    if source is None: return False
    if destination is None: return False
    if size is None: return False

    icon = QtGui.QIcon(source)

    destination = destination.replace('-symbolic', '')
    destination = destination.replace('.svg', '.png')

    width, height = size
    image = icon.pixmap(QtCore.QSize(width, height)).toImage()
    image.save(destination)

    return True


if __name__ == "__main__":

    parser = optparse.OptionParser()
    parser.add_option("--file", default=None, dest="file", help="file to parse")
    (options, args) = parser.parse_args()

    application = QtWidgets.QApplication(sys.argv)

    pattern = '**/*symbolic.svg' if options.file is None else '**/{}'.format(options.file)
    for scalable in glob.glob(pattern, recursive=True):

        if render_color(scalable, ['/apps/']):
            print('.', end='')

        destination = scalable.replace('-symbolic', '')
        with open(destination, 'w') as stream:
            stream.write(open(scalable, 'r').read())
            stream.close()

        path_8 = scalable.replace('scalable', '8x8')
        path_8_folder = os.path.dirname(path_8)
        if not os.path.exists(path_8_folder):
            os.makedirs(path_8_folder, exist_ok=True)

        path_12 = scalable.replace('scalable', '12x12')
        path_12_folder = os.path.dirname(path_12)
        if not os.path.exists(path_12_folder):
            os.makedirs(path_12_folder, exist_ok=True)

        path_16 = scalable.replace('scalable', '16x16')
        path_16_folder = os.path.dirname(path_16)
        if not os.path.exists(path_16_folder):
            os.makedirs(path_16_folder, exist_ok=True)

        path_20 = scalable.replace('scalable', '20x20')
        path_20_folder = os.path.dirname(path_20)
        if not os.path.exists(path_20_folder):
            os.makedirs(path_20_folder, exist_ok=True)

        path_22 = scalable.replace('scalable', '22x22')
        path_22_folder = os.path.dirname(path_22)
        if not os.path.exists(path_22_folder):
            os.makedirs(path_22_folder, exist_ok=True)

        path_24 = scalable.replace('scalable', '24x24')
        path_24_folder = os.path.dirname(path_24)
        if not os.path.exists(path_24_folder):
            os.makedirs(path_24_folder, exist_ok=True)

        path_32 = scalable.replace('scalable', '32x32')
        path_32_folder = os.path.dirname(path_32)
        if not os.path.exists(path_32_folder):
            os.makedirs(path_32_folder, exist_ok=True)

        path_48 = scalable.replace('scalable', '48x48')
        path_48_folder = os.path.dirname(path_48)
        if not os.path.exists(path_48_folder):
            os.makedirs(path_48_folder, exist_ok=True)

        path_64 = scalable.replace('scalable', '64x64')
        path_64_folder = os.path.dirname(path_64)
        if not os.path.exists(path_64_folder):
            os.makedirs(path_64_folder, exist_ok=True)

        path_96 = scalable.replace('scalable', '96x96')
        path_96_folder = os.path.dirname(path_96)
        if not os.path.exists(path_96_folder):
            os.makedirs(path_96_folder, exist_ok=True)

        path_128 = scalable.replace('scalable', '128x128')
        path_128_folder = os.path.dirname(path_128)
        if not os.path.exists(path_128_folder):
            os.makedirs(path_128_folder, exist_ok=True)

        path_256 = scalable.replace('scalable', '256x256')
        path_256_folder = os.path.dirname(path_256)
        if not os.path.exists(path_256_folder):
            os.makedirs(path_256_folder, exist_ok=True)

        path_512 = scalable.replace('scalable', '512x512')
        path_512_folder = os.path.dirname(path_512)
        if not os.path.exists(path_512_folder):
            os.makedirs(path_512_folder, exist_ok=True)

        if render_png(scalable, path_8.replace('.svg', '.png'), (8, 8)):
            print('.', end='')

        if render_png(scalable, path_12.replace('.svg', '.png'), (12, 12)):
            print('.', end='')

        if render_png(scalable, path_16.replace('.svg', '.png'), (16, 16)):
            print('.', end='')

        if render_png(scalable, path_20.replace('.svg', '.png'), (20, 20)):
            print('.', end='')

        if render_png(scalable, path_22.replace('.svg', '.png'), (22, 22)):
            print('.', end='')

        if render_png(scalable, path_24.replace('.svg', '.png'), (24, 24)):
            print('.', end='')

        if render_png(scalable, path_32.replace('.svg', '.png'), (32, 32)):
            print('.', end='')

        if render_png(scalable, path_48.replace('.svg', '.png'), (48, 48)):
            print('.', end='')

        if render_png(scalable, path_64.replace('.svg', '.png'), (64, 64)):
            print('.', end='')

        if render_png(scalable, path_96.replace('.svg', '.png'), (96, 96)):
            print('.', end='')

        if render_png(scalable, path_128.replace('.svg', '.png'), (128, 128)):
            print('.', end='')

        if render_png(scalable, path_256.replace('.svg', '.png'), (256, 256)):
            print('.', end='')

        if render_png(scalable, path_512.replace('.svg', '.png'), (512, 512)):
            print('.', end='')

    print('done')
