# open api csv로 다운받는 코드
import requests
import pandas as pd
import xml.etree.ElementTree as ET
import os

# 현재 작업 디렉터리 출력
print("Current working directory:", os.getcwd())

# API 기본 URL
base_url = "http://211.237.50.150:7080/openapi/0dd7514aa1565f93bcc5bf364dc67ea1646777d3499e83dab1a089c835fd5044/xml/Grid_20220823000000000636_1/"

# 데이터 저장을 위한 리스트 초기화
data_list = []

# 데이터 요청 시작 위치 설정
start = 1
batch_size = 1000

# 데이터를 요청하고 수집하는 함수
def fetch_data(start, end):
    url = f"{base_url}{start}/{end}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Fetched data from {start} to {end}")
        return response.content
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# XML 데이터를 파싱하여 딕셔너리로 변환하는 함수
def parse_xml(xml_data):
    root = ET.fromstring(xml_data)
    rows = root.findall(".//row")
    print(f"Found {len(rows)} rows")  # 찾은 아이템 수 출력
    data = []
    for row in rows:
        row_data = {}
        for child in row:
            row_data[child.tag] = child.text
        data.append(row_data)
    return data

# 데이터를 수집하여 리스트에 저장
while True:
    end = start + batch_size - 1
    print(f"Fetching data from {start} to {end}")
    xml_data = fetch_data(start, end)
    if xml_data:
        data = parse_xml(xml_data)
        if not data:  # 더 이상 데이터가 없으면 종료
            print("No more data available.")
            break
        data_list.extend(data)
    else:
        break
    start += batch_size

# 수집된 데이터를 DataFrame으로 변환
df = pd.DataFrame(data_list)

# CSV 파일로 저장
output_path = os.path.join(os.getcwd(), "d.csv")  # 다른 파일 이름 사용
df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"Data has been saved to {output_path}")

# CSV 파일 내용을 확인
print(df.head())