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