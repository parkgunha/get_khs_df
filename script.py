# 필요 라이브러리 가져오기
import requests
import xml.etree.ElementTree as ET
import pandas as pd

# 함수 정의
def get_khs_df():
    # xml 데이터 생성: API URL과 Parameter를 requests.get(url, params) 함수에 넣기
    url = "https://www.khs.go.kr/cha/SearchKindOpenapiList.do"
    response = requests.get(url)

    # xml 파싱: element객체로 만들기
    root = ET.fromstring(response.text)

    # 열과 값(리스트)형태로 된 딕셔너리 생성
    row_dict = {'sn':[]
                ,'no':[]
                ,'ccmaName':[]
                ,'crltsnoNm':[]
                ,'ccbaMnm1':[]
                ,'ccbaMnm2':[]
                ,'ccbaCtcdNm':[]
                ,'ccsiName':[]
                ,'ccbaAdmin':[]
                ,'ccbaKdcd':[]
                ,'ccbaCtcd':[]
                ,'ccbaAsno':[]
                ,'ccbaCncl':[]
                ,'ccbaCpno':[]
                ,'longitude':[]
                ,'latitude':[]
                ,'regDt':[]}

    # element의 tag와 text를 딕셔너리에 넣기
    for item in root.findall('./item'):
        for i in item:
            row_dict[i.tag].append(i.text)

    khs_df = pd.DataFrame(row_dict)
    return khs_df

if __name__ == '__main__':
    get_khs_df()