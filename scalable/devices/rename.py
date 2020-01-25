import glob

if __name__ == "__main__":
    pass

    for scalable in glob.glob('**/*.svg', recursive=True):
        if scalable.find('symbolic') != -1: continue
        print(scalable)

        symbolic = scalable.replace('.svg', '-symbolic.svg')
        with open(symbolic, 'w') as stream:
            stream.write(open(scalable).read())
            stream.close()
