# KrxApi

다음 4가지 class를 이용하여 데이터를 가져올 수 있습니다.

class | 설명
-|-|
SearchStock | searchText에 일치하는 주식을 찾습니다.
AllStockPrice | trdDd(날짜포맷: %Y%m%d)의 모든 주식 정보를 가져옵니다.
AllStockFluctuationRate | strtDd ~ endDd(날짜포맷: %Y%m%d)사이의 주식 변동율을 가져옵니다.
StockPriceInfo | isuCd(주식 id)에 해당하는 strtDd ~ endDd(날짜포맷: %Y%m%d)사이의 가격정보를 가져옵니다.
