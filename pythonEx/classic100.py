#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import os.path as path
import shutil


classic100 = 'Best Classics 100'
classic100dir = None
toBeRemoved = []


def moveFiles(src, dest):
"""
src디렉토리에 있는 파일을 dest 디렉토리로 옮긴다
"""    
    for f in os.listdir(src):
        fpath = path.join(src, f)
        dpath = path.join(dest, f)
        shutil.move(fpath, dpath)


def removeEmptyDir(path):
"""
비어있는 디렉토리는 삭제한다.
"""   
    if 0 == len(os.listdir(path)):
        os.rmdir(path)


def organizeClassic100(musicdir):
"""
Best Classics 100으로 분류할 디렉토리를 찾아서 Best Classics 100 
디렉토리로 옮긴다. 
"""
    global classic100
    global classic100dir

    for child in os.listdir(musicdir):
        childdir = path.join(musicdir, child)
        if True == path.isdir(childdir):
            if child == classic100:
                continue

            if True == child.startswith(classic100):
                movedChildDir = path.join(classic100dir, child)
                if False == path.exists(movedChildDir):
                    shutil.move(childdir, classic100dir)
                else:
                    moveFiles(childdir, movedChildDir)
                    os.rmdir(childdir)
            else:
                organizeClassic100(childdir)
                removeEmptyDir(childdir)

    

if __name__ == '__main__':

    musicdir = path.abspath(input('enter music directory: '))

    classic100dir = path.join(musicdir, classic100)


    if os.path.exists(classic100dir) == False :
        os.mkdir(classic100dir)

    organizeClassic100(musicdir)    
