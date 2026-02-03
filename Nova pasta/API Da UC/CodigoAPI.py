import requests

# Definindo as credenciais
email = 'teuspw22@gmail.com'
senha = 'irTzMwGCe1e4'

login_url = 'http://137.184.108.252:5000/api/login'

# Fazendo a requisição para gerar o token
response = requests.post(login_url, json={'email': email, 'password': senha})

if response.status_code == 200:
    token = response.json().get('token')
    print(f'Token gerado: {token}')

    # Agora que temos o token, vamos buscar as cidades
    cidades_url = 'http://137.184.108.252:5000/api/cidades'
    headers = {'x-access-token': token}

    # Testando o método GET
    cidades_response = requests.get(cidades_url, headers=headers)  # ou requests.post, dependendo do que a API aceita

    if cidades_response.status_code == 200:
        cidades = cidades_response.json()
        print('Cinco cidades recebidas:')
        for cidade in cidades[:5]:
            print(cidade)
    else:
        print('Erro ao buscar cidades:', cidades_response.status_code, cidades_response.text)
else:
    print('Erro ao fazer login:', response.status_code, response.text)
