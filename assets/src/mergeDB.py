import pandas as pd

df = pd.read_csv('../db/db.csv')
df['楷書編號'] = df['楷書編號'].str.replace('[', '').str.replace(']', '').str.replace("'", '')
df = df.drop(columns = ['鍵盤字型','鍵盤字型(binary)'])
dfimg = pd.read_csv('../db/dbimg.csv')
dfmerge = pd.merge(df, dfimg, on="字體編號")
dfdup = dfmerge[dfmerge.duplicated(subset=['小篆編號'],keep=False)]
dfmerge = dfmerge.drop_duplicates(subset=['小篆編號'], keep='first')
print(dfdup)

for d in dfmerge:
	print(d)
	s()
dfmerge.to_csv('../db/dball.csv',index = False)