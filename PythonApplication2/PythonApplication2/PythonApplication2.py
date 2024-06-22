import pandas as pd


# 경도,위도 추가하는 코드
# #파일 불러오기
# file_path = 'C:/Users/user/source/repos/PythonApplication3/PythonApplication3/a.csv'

# df = pd.read_csv(file_path, encoding='UTF-8')
# CSV 파일을 읽어옵니다.
df = pd.read_csv('C:/Users/user/source/repos/PythonApplication2/PythonApplication2/b.csv')

# # 합치고자 하는 세 개의 열 이름을 지정합니다.
# col1 = 'CTPRVN_NM'
# col2 = 'SIGUNGU_NM'
# col3 = 'EMD_NM'

# # 세 개의 열을 합칩니다. 각 값을 문자열로 변환한 후 합칩니다.
# df['Combined'] = df[col1].astype(str) + df[col2].astype(str) + df[col3].astype(str)

# # 결과를 새로운 CSV 파일로 저장합니다.
# df.to_csv('bto.csv', index=False)