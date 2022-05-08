numero_alunos_presentes = 4 # alterar valor conforme o desejado
tempo_chegada_alunos = [-3, -2, -1, 0, 1, 2, 2, 4, 5, 6] # alterar valor conforme o desejado
contador_alunos_pontuais = 0

for tempo in tempo_chegada_alunos:
    if tempo <= 0:
        contador_alunos_pontuais += 1
    
if contador_alunos_pontuais >= numero_alunos_presentes:
    print('Aula normal')
else:
    print('Aula cancelada')
