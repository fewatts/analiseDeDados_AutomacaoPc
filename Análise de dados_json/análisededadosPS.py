import pandas as pd
df = pd.read_json(r'C:\Users\Administrador\Downloads\dados.json')
indexnames = df[(df['valor'] == 0)].index
df.drop(indexnames, inplace=True)
max = df['valor'].max()
min = df['valor'].min()
med = df['valor'].mean()
df[df['valor'].between(20865.37, 50000)]
print(f'''O menor valor de faturamento foi de {min:,.2f} R$,
o maior valor de faturamento foi de {max:,.2f} R$,
a média mensal foi de {med:,.2f} R$
e no total foram esses dias com faturamento acima da média:
{df[df['valor'].between(20865.37, 50000)]}''')
