import os, shutil, glob
import ctypes
import globals
from jaraco.windows import filesystem
# NEED TO INSTAL jaraco.windows !!!

constants = globals.Constants()
def copySourceToTargetDestination(source, destination):
    if(not os.path.exists(destination)):
        #shutil.copytree(source, destination)
        os.makedirs(destination)
        files = os.listdir(source)
        for file in files:
            path = os.path.dirname(os.path.abspath(__file__))
            file = os.path.join(path, source, file)
            if(not os.path.isdir(file)):
                #if files.endswith(".txt"):
                if not is_hidden(file):
                    shutil.copy(file, destination)
            else:
                if not is_hidden(file):
                    doRecurisve(file, destination, source)

def doRecurisve(path, destination, source):
    #mkdirDestination = '../Target/Django.Core/' + path.split(source)[1]
    mkdirDestination = constants.goBack + constants.targetDestination + path.split(source)[1]
    os.makedirs(mkdirDestination)
    fileList = os.listdir(path)
    for file in fileList:
        file = path + '/' + file
        if(not os.path.isdir(file)):
            destination = mkdirDestination
            if not is_hidden(file):
                shutil.copy(file, destination)
        else:
            if not is_hidden(file):
                doRecurisve(file, destination, source)


def is_hidden(filepath):
    name = os.path.basename(os.path.abspath(filepath))
    return name.startswith('.') or has_hidden_attribute(filepath)

def has_hidden_attribute(filepath):
    return filesystem.GetFileAttributes(filepath).hidden