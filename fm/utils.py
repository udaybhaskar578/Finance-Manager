# Standard
import os
import subprocess
import shutil
import ipaddress

from datetime import timedelta, date


def getLastNdaysStartAndEndDate(n):
    today = date.today()
    tdelta = timedelta(days=-n)
    startDate = today + tdelta
    endDate = today

    return startDate, endDate


class Ctx(object):
    '''
    This object can be used make an arbitrary context.
    '''


class Args(object):
    '''
    This object captures positional and keyword arguments
    '''

    def __init__(self, *pargs, **kwargs):
        self.pargs = pargs
        self.kwargs = kwargs


def silentRemove(filename):
    try:
        os.remove(filename)
    except OSError as e:
        pass


def copyFile(src, dest):
    if fileExists(src):
        shutil.copy(src, dest)


def createDir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def fileExists(fileName):
    if os.path.isfile(fileName):
        return True
    return False


def touchFile(filePath):
    with open(filePath, 'w'):
        os.utime(filePath, None)
