
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
