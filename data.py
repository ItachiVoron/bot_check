import pandas as pd
df=pd.read_csv('phishing_site_urls.csv')
df['Label']=df['Label'].replace('bad','0')
df['Label']=df['Label'].replace('good','1')

id=[]
url=[]
label=[]
for i in range(549346):
  id.append(i)
  url.append(df['URL'][i])
  label.append(df['Label'][i])
data=list(zip(id,url,label))
print(data)