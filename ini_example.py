"""  работа с ini файлами
"""
import os
from configparser import ConfigParser

def test():
    """
    описание функции
    """
    config = ConfigParser()
    curdir = os.getcwd()
    filename = curdir + "\\config.ini"
    config.read(filename)
    items = config.items("Config")
    print(config.sections())
    db_driver, dbfile = items[1]
    print("Driver %s FileName %s" % (db_driver, dbfile))
    config.set("Config", "Version", "1.0")
    with open(filename, "w") as cf:
        config.write(cf)


test()
