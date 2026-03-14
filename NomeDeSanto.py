from nomes import santos

print('Bem-vindo ao programa "Nome de Santo"!')

nome = input('Digite seu nome: ').strip().lower()
primeiro_nome = nome.split()[0]

print('Analisando seu nome...')

if primeiro_nome in santos:
    print(f'Parabéns! O nome {primeiro_nome.title()} é nome de santo!')
else:
    print(f'Infelizmente o nome {primeiro_nome.title()} não é nome de santo.')
