#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

isFihished = False
bookDoc = None

def checkBookDoc():
    if None == bookDoc:
        print('no book document loaded')
        return False
    else:
        return True

def printBookList():
    global bookDoc

    if False == checkBookDoc():
        return

    print('\nBOOK LIST')
    catalogNode = bookDoc.childNodes
    bookNodeList = catalogNode[0].childNodes
    for subNode in bookNodeList:
        if 'book' == subNode.nodeName:
            items = subNode.childNodes
            title = author = None
            for item in items:
                if 'title' == item.nodeName:
                    title = item.firstChild.nodeValue
                if 'author' == item.nodeName:
                    author = item.firstChild.nodeValue
            print('title:', title, ', ', 'author:', author)
        

def searchTitle(title):
    global bookDoc

    if False == checkBookDoc():
        return None

    bookInfo = None
    found = False
    catalogNode = bookDoc.childNodes
    bookNodeList = catalogNode[0].childNodes
    for subNode in bookNodeList:
        if 'book' == subNode.nodeName:
            items = subNode.childNodes
            for item in items:
                if 'title' == item.nodeName:
                    if title == item.firstChild.nodeValue:
                        found = True
                        break
            if True == found:
                bookInfo = {item.nodeName: item.firstChild.nodeValue for item in items if 1 == item.nodeType}
                break
    return bookInfo

                
def searchBook():
    title = input('please enter a book title: ')
    bookInfo = searchTitle(title)
    if None != bookInfo:
        print(bookInfo)
    else:
        print('there is no book with title', title)
    
            
                
def loadBookXml():
    global bookDoc
    file = input('please input file name: ')
    try:
        with open(file) as xmlFile:
            bookDoc = parse(xmlFile)

    except IOError:
        print('invalid file name')
    except Exception:
        print('invalid book document')
    else:
        print('succeeded to load book document')        
        

def freeBookXml():
    global bookDoc
    if checkBookDoc():
        bookDoc.unlink()
        print('unload book document')


def printToXml ():
    """
    """
    if checkBookDoc():
        print(bookDoc.toxml())


#def addBook(book):
#    global bookDoc
#    if not checkBookDoc():
#        return None
#
#    newBook = bookDoc.createElement('book')
#    newBook.setAttribute('id', 'bk130')
#    titleEle = bookDoc.createElement('title')
#    titleNode = bookDoc.createTextNode()
#    
        
        
def prompt():
    print('==========Menu=========')
    print('Load xml: l')
    print('Print dom to xml: p')
    print('Quit program: q')
    print('print Book list: b')
    print('Add new book: a')
    print('Search book title: s')
    print('Make html: m')
    print('=======================')
    menu = input('select menu: ')
    return menu

def quitBookManager():
    global isFihished
    isFihished = True
    
def execute(menu):
    if 'q' == menu:
        quitBookManager()
    elif 'l' == menu:
        loadBookXml()
    elif 'p' == menu:
        printToXml()
    elif 'b' == menu:
        printBookList()
    elif 's' == menu:
        searchBook()
#    elif 'a' == menu:
#            addBook()
    else:
        print('Wrong menu: ', menu)

    
if __name__ == '__main__':
        
    try:
        while isFihished == False:
            print("Welcome! Book Manager Program (xml version)")
            menu = prompt()
            execute(menu)
    finally:
        freeBookXml()
        print('bye')


        
        