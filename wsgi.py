'''
아파치 서버가 이파일을 구동하여 flask 가동시킴
여기서는 Flask 객체를 가져와서 참조
'''

import sys
import os

#경로 성정
CUR_DIR = os.getcwd()
#에러의 출력방향을 출력으로 동일하게 구성
sys.stdout = sys.stderr
#path추가
sys.path.insert(0, CUR_DIR)

#서버 가져오기
from run import app as application
