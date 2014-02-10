#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from os.path import *

# 현재 경로를 prefix로 해서 입력 받은 경로를 절대경로로 바꿔서 반환
abspath('tmp')

# 입력받은 경로의 기본 이름 반환. abspath와 반대 
basename(abspath('tmp'))

# 입력받은 경로 목록에서 공통 prefix를 추출
commonprefix([abspath('bin'), abspath('test'), abspath('lib')])

# 입력받은 경로에서 디렉토리 반환
dirname(abspath('tmp\\test.txt'))

# 파일 존재 유무
exists(abspath('tmp'))

# 입력받은 경로안의 '~'를 현재 사용자의 디렉터리의 절대경로로 대체, ~<사용자명>을 붙이면 원하는 사용자 경로로 대체됨.
expanduser('~\\temp\\test.txt')

# 입력받은 path안의 환경변수가 있으면 이를 확장함
expandvars('$HOME\\temp')

# 파일 최근 접근 시간
getatime(abspath('python.exe'))

import time
time.gmtime(getatime(abspath('python.exe')))


# 파일 사이즈
getsize(abspath('python.exe'))


# ls와 비슷하게 파일 목록을 가져옴. 와일드카드를 사용할 수 있음.
import glob

glob.glob(expanduser('~\\*'))

glob.glob(abspath('.') + '\\*.exe')

# 파일 목록을 이터레이터로 반환
for i in glob.iglob(expanduser('~\\*')):
    print(i)


