#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import os.path as path
import shutil
import glob

variousArtistDir = 'Various Artists'


def moveFiles(src, dest):
    """
    src디렉토리에 있는 파일을 dest 디렉토리로 옮긴다
    """    
    for f in glob.glob(path.join(src, '*')):
        shutil.move(f, dest)

        
        
def tryRemoveEmptyDir(path):
    """
    비어있는 디렉토리는 삭제한다.
    """   
    if 0 == len(os.listdir(path)):
        os.rmdir(path)

        
        
def buildAlbumArtistDic(musicdir):
    albumArtistDic = {}
    for item  in glob.glob(path.join(musicdir, '*')):
        if item.endswith(variousArtistDir):
            continue

        if True == path.isdir(item):
            artistDir = item
            albums = os.listdir(artistDir)
            for album in albums:
                albumPath = path.join(artistDir, album)
                if False == path.isdir(albumPath):
                    continue

                if album in albumArtistDic:
                    albumArtistDic[album].append(artistDir)
                else:
                    albumArtistDic[album] = [artistDir]
            

    return albumArtistDic


def createVariousArtistAlbum(musicdir, album, artistDirs):
    albumDir = path.join(musicdir, variousArtistDir, album)
    if path.exists(albumDir) == False:
        os.makedirs(albumDir)

    for artistDir in artistDirs:
        artistAlbumDir = path.join(artistDir, album)
        moveFiles(artistAlbumDir, albumDir)
        tryRemoveEmptyDir(artistAlbumDir)
        tryRemoveEmptyDir(artistDir)



def organizeGoogleMusicDir(musicdir):

    albumArtistDic = buildAlbumArtistDic(musicdir)
    
    for album, artistDirs in albumArtistDic.items():
        if len(artistDirs) > 1:
            createVariousArtistAlbum(musicdir, album, artistDirs)
            
    
    

if __name__ == '__main__':

    musicDir = path.abspath(input('enter music directory: '))

    if path.exists(musicDir) == False:
        print(musicDir, 'does not exist.')
        exit(-1)

    organizeGoogleMusicDir(musicDir)
