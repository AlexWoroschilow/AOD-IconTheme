import os
import glob
import optparse
from lxml import etree
from cairosvg import svg2png
from multiprocessing import Pool


def render_color(source=None, ignores=[]):
    try:

        for pattern in ignores:
            if source.find(pattern) == -1:
                continue
            print(source)
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

    destination = destination.replace('-symbolic', '')
    destination = destination.replace('.svg', '.png')

    try:

        width, height = size

        with open(source, 'rb') as stream:
            svg2png(bytestring=stream.read(), unsafe=True,
                    write_to=destination,
                    output_width=width,
                    output_height=height)
            stream.close()

    except Exception as ex:
        print(source, destination, ex)

    return True


def iconify(arguments=None):
    scalable, size = arguments
    width, height = size

    # if render_color(scalable, ['/vendors/']):
    #     print('.', end='')

    destination = scalable.replace('-symbolic', '')
    with open(destination, 'w') as stream:
        stream.write(open(scalable, 'r').read())
        stream.close()

    path = scalable.replace('scalable', '{}x{}'.format(width, height))
    path_folder = os.path.dirname(path)
    if len(path_folder) and not os.path.exists(path_folder):
        os.makedirs(path_folder, exist_ok=True)

    if render_png(scalable, path.replace('.svg', '.png'), size):
        print('.', end='')


if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("--file", default=None, dest="file", help="file to parse")
    (options, args) = parser.parse_args()

    pool = Pool(processes=4)

    elements = []

    pattern = '**/*symbolic.svg' if options.file is None else '**/{}'.format(options.file)
    for scalable in glob.glob(pattern, recursive=True):
        if os.path.isdir(scalable):
            continue

        #elements.append((scalable, (8, 8)))
        #elements.append((scalable, (12, 12)))
        #elements.append((scalable, (16, 16)))
        #elements.append((scalable, (20, 20)))
        #elements.append((scalable, (24, 24)))
        elements.append((scalable, (32, 32)))
        elements.append((scalable, (48, 48)))
        elements.append((scalable, (64, 64)))
        elements.append((scalable, (96, 96)))
        elements.append((scalable, (128, 128)))
        elements.append((scalable, (256, 256)))
        elements.append((scalable, (512, 512)))

    pool.map(iconify, elements)
    pool.close()
