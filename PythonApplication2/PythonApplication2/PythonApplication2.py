import pandas as pd


# �浵,���� �߰��ϴ� �ڵ�
# #���� �ҷ�����
# file_path = 'C:/Users/user/source/repos/PythonApplication3/PythonApplication3/a.csv'

# df = pd.read_csv(file_path, encoding='UTF-8')
# CSV ������ �о�ɴϴ�.
df = pd.read_csv('C:/Users/user/source/repos/PythonApplication2/PythonApplication2/b.csv')

# # ��ġ���� �ϴ� �� ���� �� �̸��� �����մϴ�.
# col1 = 'CTPRVN_NM'
# col2 = 'SIGUNGU_NM'
# col3 = 'EMD_NM'

# # �� ���� ���� ��Ĩ�ϴ�. �� ���� ���ڿ��� ��ȯ�� �� ��Ĩ�ϴ�.
# df['Combined'] = df[col1].astype(str) + df[col2].astype(str) + df[col3].astype(str)

# # ����� ���ο� CSV ���Ϸ� �����մϴ�.
# df.to_csv('bto.csv', index=False)