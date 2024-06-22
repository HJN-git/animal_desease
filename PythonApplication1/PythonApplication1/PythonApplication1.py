# open api csv�� �ٿ�޴� �ڵ�
import requests
import pandas as pd
import xml.etree.ElementTree as ET
import os

# ���� �۾� ���͸� ���
print("Current working directory:", os.getcwd())

# API �⺻ URL
base_url = "http://211.237.50.150:7080/openapi/0dd7514aa1565f93bcc5bf364dc67ea1646777d3499e83dab1a089c835fd5044/xml/Grid_20220823000000000636_1/"

# ������ ������ ���� ����Ʈ �ʱ�ȭ
data_list = []

# ������ ��û ���� ��ġ ����
start = 1
batch_size = 1000

# �����͸� ��û�ϰ� �����ϴ� �Լ�
def fetch_data(start, end):
    url = f"{base_url}{start}/{end}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Fetched data from {start} to {end}")
        return response.content
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# XML �����͸� �Ľ��Ͽ� ��ųʸ��� ��ȯ�ϴ� �Լ�
def parse_xml(xml_data):
    root = ET.fromstring(xml_data)
    rows = root.findall(".//row")
    print(f"Found {len(rows)} rows")  # ã�� ������ �� ���
    data = []
    for row in rows:
        row_data = {}
        for child in row:
            row_data[child.tag] = child.text
        data.append(row_data)
    return data

# �����͸� �����Ͽ� ����Ʈ�� ����
while True:
    end = start + batch_size - 1
    print(f"Fetching data from {start} to {end}")
    xml_data = fetch_data(start, end)
    if xml_data:
        data = parse_xml(xml_data)
        if not data:  # �� �̻� �����Ͱ� ������ ����
            print("No more data available.")
            break
        data_list.extend(data)
    else:
        break
    start += batch_size

# ������ �����͸� DataFrame���� ��ȯ
df = pd.DataFrame(data_list)

# CSV ���Ϸ� ����
output_path = os.path.join(os.getcwd(), "d.csv")  # �ٸ� ���� �̸� ���
df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"Data has been saved to {output_path}")

# CSV ���� ������ Ȯ��
print(df.head())