import os

directory = r"d:\Книги"

def getsubs(dir):
    # get all
    dirs = []
    files = []
    for dirname, dirnames, filenames in os.walk(dir):
        dirs.append(dirname)
        print("Директорий %s" % dirname)
        for subdirname in dirnames:
            dirs.append(os.path.join(dirname, subdirname))
            print("ПодДиректорий %s" % subdirname)
        for filename in filenames:
            if str(filename).endswith('.pdf'):
                files.append(os.path.join(dirname, filename))
                print("Файл %s" % filename)
    return dirs, files

dirs, files = getsubs(directory)

print(files)