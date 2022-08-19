import pandas as pd
df = pd.read_csv('notas_alunos.csv', encoding="UTF-8", sep=";" )

df["Media"] = (df['nota_1'] + df['nota_2']) / 2 

testeSitacao = ''
df.loc[(df['Media'] >= 7) & (df["faltas"] < 5), "testeSitacao"] = "Aprovado"
df.loc[(df['Media'] < 7)  | (df["faltas"] > 5), "testeSitacao"] = "Reprovado"

df.to_csv('alunos_situação.csv')


maiorMedia = df['Media'].max()
maiorFalta = df['faltas'].max()
MediaTurma = df['Media'].median()
print('A maior nota foi: ' + str(maiorMedia))
print('O maior numero de faltas foi: ' + str(maiorFalta))
print('A media geral da turma foi: ' + str(MediaTurma))

df.head()