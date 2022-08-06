# 프로젝트 02 - 파이썬 기반 데이터 활용

## :computer: 코드

##### 00.py

```python
# 요청을 보냄 (requests를 사용함)
import requests
# 비트코인 KRW 정의
def get_btc_krw(): 
    order_currency = "BTC" # order_currency에 BTC 대입
    payment_currency = "KRW"  # pyament_currency에 KRW 대입
    # URL 만듬
    url = f"http://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"
    # URL에 get해서 가지고 오고 JSON을 파이썬 객체로 변함
    # 그러면 response 객체를 줌
    # 이것을 res 변수에 저장
    res = requests.get(url=url).json()
    # res["data"] 결과를 data로 저장
    data = res["data"]
    # data["전일종가"] 결과를 전일종가에 저장
    prev_closing_price = data["prev_closing_price"]
    # 전일종가 출력
    return prev_closing_price
# 이름이 메인이면
if __name__ == "__main__":
    # get_btc_krw 출력
    print(get_btc_krw())
```



##### 01.py

```python
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

```



##### 02.py

```python
import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('api_key')



def vote_average_movies():
    pass 
    BASE_URL = 'https://api.themoviedb.org/3' 
    path = '/movie/popular'
    params = {
        'api_key': 'api_key',
        'language' : 'ko-KR'
    }

    response = requests.get(BASE_URL+path, params=params).json()
    
    movie_list = response.get('results') # movie_list에 response.get('results')을 저장
    
    vote_average_movies = []

    for movie in movie_list:
        if movie.get('vote_average') >= 8: # 평점 8점 이상 영화 get
          vote_average_movies.append(movie)
    
    return vote_average_movies
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(vote_average_movies())
    """
    [{'adult': False,
      'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
      'genre_ids': [28, 12, 878],
      'id': 634649,
      'original_language': 'en',
      'original_title': 'Spider-Man: No Way Home',
      'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                  '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                  '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                  '사상 최악의 위기를 맞게 되는데…',
      'popularity': 1842.592,
      'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
      'release_date': '2021-12-15',
      'title': '스파이더맨: 노 웨이 홈',
      'video': False,
      'vote_average': 8.1,
      'vote_count': 13954},
    ..생략..,
    }]
    """

```



##### 03.py

```python
import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('api_key')


def ranking():
    pass

    BASE_URL = 'https://api.themoviedb.org/3' 
    path = '/movie/popular'
    params = {
        'api_key': 'api_key',
        'language': 'ko-KR',
    }

    response = requests.get(BASE_URL+path, params=params).json()
    movie_list = response.get('results')
    movie_list.sort(key=lambda x: x['vote_average'], reverse= True)

ranking = [] # 빈 리스트 생성

for i in range(5):
    ranking.append(movie_list[i])

return ranking


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
```



##### 04.py

```python
import requests
from pprint import pprint

# 추천 영화 (제목) 정의
def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
    URL = 'https://api.themoviedb.org/3/search/movie' 
    
    params = {
        'api_key': '6113132e8f47d25f160c7567d23869a3',
        'language': 'ko-KR',
        'query': title
    }
    response = requests.get(URL, params=params).json()
    a = response.get('results')
    if len(a) == 0: # a의 길이가 0이면
        return None # None 반환
    b = a[0]['id']


    URL2 = f'https://api.themoviedb.org/3/movie/{b}/recommendations'
    params2 = {
        'api_key': '6113132e8f47d25f160c7567d23869a3',
        'language': 'ko-KR',
    }
    c = requests.get(URL2, params = params2).json()
    d = c.get('results') # results get
    result = [] # 빈 리스트 생성
    for i in d: # d를 순회
        result.append(i['title'])
    return result
           

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None


```



##### 05.py

```python
import requests
from pprint import pprint


def credits(title):
    pass 
    URL = 'https://api.themoviedb.org/3/search/movie'
    
    params = {
        'api_key': '6113132e8f47d25f160c7567d23869a3',
        'language': 'ko-KR',
        'query': title
    }
    
    response = requests.get(URL, params=params).json()
    a = response.get('results')
    if len(a) == 0:
        return None
    b = a[0]['id']


    URL1 = f'http://api.themoviedb.org/3/movie/{b}/credits'
    params2 = {
        'api_key': '6113132e8f47d25f160c7567d23869a3',
        'language': 'ko-KR',

    }
    c = requests.get(URL2, params = params2).json()
    d = c.get('cast') # 출연진 get
    t1 = []
    for i in d:
        if i['cast_id'] < 10: # 10 미만인 출연진이면
            t1.append(i['name']) # t1에 추가
    
    e = c.get('crew') # 스태프 get
    t2 = []
    for i in e:
        if i['department'] == 'Directing': # 부서가 Directing이면
            t2.append(i['name']) # t2에 추가

    result = {"cast" : t1, "crew" : t2}
    return result
       

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None

```





## :rocket: 후기

* Python 기본 문법과 JSON을 다시 문제에 응용하고 적용한 문법을 해설하는 시간을 통해 파이썬과 더욱 친해지게 되었습니다.
* `external library`를 활용해서 자유자재로 데이터를 수집할 수 있는 능력을 얻게 되었습니다.
* Request와 Response의 본질을 이해하게 되었고 어떻게 사용하는지 알게 되었습니다. 개발자의 문서도 읽을 수 있는 역량이 생겼습니다.