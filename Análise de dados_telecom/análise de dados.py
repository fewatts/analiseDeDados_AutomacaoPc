#Este código faz a análise de uma base de dados da 
# empresa telecom com o intuito de verificar as diferenças 
# visuais de porque certos clientes cancelaram o serviço da empresa
from numpy import histogram
import pandas as pd
df = pd.read_csv(r'C:\Users\Administrador\Downloads\telecom_users.csv')
df = df.drop(['Unnamed: 0'], axis=1)
df = df.dropna(how='all', axis=1)
df['TotalGasto'] = pd.to_numeric(df['TotalGasto'], errors='coerce')
df = df.dropna()
print(df['Churn'].value_counts())
print(df['Churn'].value_counts(normalize=True).map('{:.1%}'.format))
print(df.info())
import plotly.express as px
for Column in df:
	if Column != 'IDCliente':
		fig = px.histogram(df, x=Column, color='Churn')
		fig.show()
		print(df.pivot_table(index='Churn', columns=Column, aggfunc='count')['IDCliente'])
