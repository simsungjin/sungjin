# sungjin
최초 flask app 소스 관리


배포 관련 사항
deloy.json : 도메인, 아이피 등 정보
            형식이 json이라서 주석 불가
fabfile.py : 페브릭 작업 내용 기술
fabfile_comment.py : 주석 버전
wsgi.py : entry파일, 서버구동시 시작점
requirement.txt : 서버 구동시 필요한 모듈을 기술(버전포함)


# 서버로그확인 
접속로그 (파이썬 로그)
> tail -f /var/log/apache2/access.log 로그파일명 => 
이 파일이 변화되는 것을 실시간적으로 읽어서 출력해라
> ctrl + c
에러로그 (500에러 발생시, internal server error)
> tail -f/log/apache2/error.log
> ctrl + c