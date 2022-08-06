# 6113132e8f47d25f160c7567d23869a3
# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
# 요청을 보냄 (request를 사용함)
import requests
import os
from detenv import load_dotenv # 환경변수 사용

load_dotenv()
api_key = os.getenv('api_key')


def popular_count():
    pass 
    #URL 저장
    BASE_URL = 'https://api.themoviedb.org/3' 
    # 상세경로에 popular movie 볼 수 있음
    path = '/movie/popular'
    # params에 api_key라고 하는 곳에 값을 넣음
    params = {
        'api_key' : 'api_key',
        'language' : 'ko-KR'
    }
    # 응답결과는 requests.get(BASE_URL에 더하기 path)
    # 이것을 파이썬 객체로 변환
    response = requests.get(BASE_URL+path, params=params).json()
    # print(response, type(response))

    movie_list = response.get('results')

    popular_count = 0
    for movie in movie_list:
        popular_count += 1

    return popular_count

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
