print('BOLETIM ESCOLAR')
print('='*30)
boletim=dict()
boletim['nome']=str(input('Nome: '))
boletim['media']=float(input(f'Média de {boletim["nome"]}: '))
if boletim["media"]>=7:
    boletim['situacao']='APROVADO'
elif boletim["media"]<7 and boletim["media"]>=5:
    boletim['situacao']='RECUPERAÇÃO'
else:
    boletim['situacao']='REPROVADO'
print('-'*35)    
print(f'O aluno {boletim["nome"]} teve média {boletim["media"]} e a situação é {boletim["situacao"]}.')
print('='*35)
