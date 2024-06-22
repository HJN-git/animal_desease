# 경도,위도 추가하는 코드
# #파일 불러오기
# file_path = 'C:/Users/user/source/repos/PythonApplication3/PythonApplication3/a.csv'

# df = pd.read_csv(file_path, encoding='UTF-8')

# KAKAO_REST_API_KEY = "KakaoAk bf61fb3c509dd0c0a0e02d68a7c9e99b1f"

# api_key = KAKAO_REST_API_KEY

import pandas as pd
import requests

# 아래 겹따옴표 안에 데이터 파일명 입력
# df = pd.read_excel("./여성가족부_가족친화인증기관.xlsx") ##### 예시 #####
df = pd.read_csv("C:/Users/user/source/repos/PythonApplication3/PythonApplication3/bto.csv")

# 아래 겹따옴표 안에 복사한 키값 입력
# KAKAO_REST_API_KEY = "as91231kasd21u2813e9o21e" ##### 예시 #####
KAKAO_REST_API_KEY = "61fb3c509dd0c0a0e02d68a7c9e99b1f"

# 카카오 API를 사용하여 주소를 위도와 경도로 변환하는 함수
def get_lat_lng(address, api_key):
    url = "https://dapi.kakao.com/v2/local/search/address.json"
    headers = {"Authorization": f"KakaoAK {api_key}"}
    params = {"query": address}
    
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        result = response.json()
        if result['documents']:
            address_info = result['documents'][0]['address']
            return address_info['y'], address_info['x']
        else:
            return None, None
    else:
        raise Exception(f"Error: {response.status_code}")


# 카카오 API 키
api_key = KAKAO_REST_API_KEY

# API 요청 결과를 저장할 좌표 컬럼 생성
# 아래 df['도로명주소'] = 실제 주소가 들어가있는 컬럼명 만약 '주소'컬럼에 데이터가 저장되어 있으면 df['주소']로 수정
df['k'] = df['FARM_LOCPLC'].apply(lambda x: get_lat_lng(x, api_key))

# '위도', '경도' 컬럼 분리
df['g'] = df['k'].apply(lambda x: x[0])
df['f'] = df['k'].apply(lambda x: x[1])

# 데이터 저장
# 아래 겹따옴표 안에 새로운 데이터 파일명 입력
# df.to_excel("./(new)여성가족부_가족친화인증기관.xlsx", index=False) ##### 예시 #####
df.to_csv("fullb.csv", index=False)