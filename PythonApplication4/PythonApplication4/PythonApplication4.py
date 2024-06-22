import pandas as pd

#���� �ҷ�����
file_path = 'C:/Users/user/source/repos/PythonApplication4/PythonApplication4/b.csv'

df = pd.read_csv(file_path,encoding='UTF-8')

print(df.head())


# CSV ������ �о�ɴϴ�.
df = pd.read_csv('C:/Users/user/source/repos/PythonApplication4/PythonApplication4/b.csv')

# ��ġ���� �ϴ� �� ���� �� �̸��� �����մϴ�.
col1 = 'CTPRVN_NM'
col2 = 'SIGUNGU_NM'
col3 = 'EMD_NM'

# �� ���� ���� ��Ĩ�ϴ�. �� ���� ���ڿ��� ��ȯ�� �� ��Ĩ�ϴ�.
df['FARM_LOCPLC'] = df[col1].astype(str) + ' ' + df[col2].astype(str) + ' ' + df[col3].astype(str)

# ����� ���ο� CSV ���Ϸ� �����մϴ�.
df.to_csv('bto.csv', index=False)