# �浵,���� �߰��ϴ� �ڵ�
# #���� �ҷ�����
# file_path = 'C:/Users/user/source/repos/PythonApplication3/PythonApplication3/a.csv'

# df = pd.read_csv(file_path, encoding='UTF-8')

# KAKAO_REST_API_KEY = "KakaoAk bf61fb3c509dd0c0a0e02d68a7c9e99b1f"

# api_key = KAKAO_REST_API_KEY

import pandas as pd
import requests

# �Ʒ� �����ǥ �ȿ� ������ ���ϸ� �Է�
# df = pd.read_excel("./����������_����ģȭ�������.xlsx") ##### ���� #####
df = pd.read_csv("C:/Users/user/source/repos/PythonApplication3/PythonApplication3/bto.csv")

# �Ʒ� �����ǥ �ȿ� ������ Ű�� �Է�
# KAKAO_REST_API_KEY = "as91231kasd21u2813e9o21e" ##### ���� #####
KAKAO_REST_API_KEY = "61fb3c509dd0c0a0e02d68a7c9e99b1f"

# īī�� API�� ����Ͽ� �ּҸ� ������ �浵�� ��ȯ�ϴ� �Լ�
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


# īī�� API Ű
api_key = KAKAO_REST_API_KEY

# API ��û ����� ������ ��ǥ �÷� ����
# �Ʒ� df['���θ��ּ�'] = ���� �ּҰ� ���ִ� �÷��� ���� '�ּ�'�÷��� �����Ͱ� ����Ǿ� ������ df['�ּ�']�� ����
df['k'] = df['FARM_LOCPLC'].apply(lambda x: get_lat_lng(x, api_key))

# '����', '�浵' �÷� �и�
df['g'] = df['k'].apply(lambda x: x[0])
df['f'] = df['k'].apply(lambda x: x[1])

# ������ ����
# �Ʒ� �����ǥ �ȿ� ���ο� ������ ���ϸ� �Է�
# df.to_excel("./(new)����������_����ģȭ�������.xlsx", index=False) ##### ���� #####
df.to_csv("fullb.csv", index=False)