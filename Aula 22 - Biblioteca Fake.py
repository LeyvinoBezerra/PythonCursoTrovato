from faker import Faker
import pandas as pd

fake = Faker(locale= 'pt-BR')
fakeVI = Faker(locale=['pt-br', 'es-ES', 'en-US'])

# como usar?
print(fake.text())             # Gerar Textos
print(fake.address())          # Gerar Endereços Completo
print(fake.ascii_email())      # Email Privado
print(fake.ascii_free_email()) # Email Gratuito
print(fake.mac_address())
print()

for _  in range(10):
    print(fake.name())
print()

for _ in range(10):
    print(fake.name_female())
print()

# diversos recursos
print(fake.random_letter())      # Letra Aleatoria
print(fake.random_letters())     # vetores de Letras aleatoria
print(fake.random_digit_not_null())
print(fake.year())
print(fake.date())
print(fake.date_time())
print(fake.time())
print(fake.url())
print(fake.image_url())
print(fake.cpf())
print(fake.rg())
print(fake.cellphone_number())
print(fake.bairro())
print(fake.city())
print()

# O uso na Pratica ?
# adicionar o resultado em listas
# juntar em um DataFrame

nome = []
empresa = []
cidade = []
pais = []
funcao = []
endereco = []
email = []
data_nascimento = []
cpf = []
idade = []

for i in range(0, 20):
    nome.append(fake.name())
    empresa.append(fake.company())
    cidade.append(fake.city())
    pais.append(fake.country())
    funcao.append(fake.job())
    endereco.append(fake.street_address())
    email.append(fake.email())
    data_nascimento.append(fake.date_of_birth())
    cpf.append(fake.cpf())
    idade.append(fake.random_number(digits=2))
print(empresa)    # Gerar Range

# Gerar um DataFrame

df = pd.DataFrame(
    {
        "NOME": nome,
        "EMPRESA": empresa,
        "CIDADE": cidade,
        "PAIS": pais,
        "CARGO": funcao,
        "ENDEREÇO": endereco,
        "EMAIL": email,
        "DATA DE NASCIMENTO": data_nascimento,
        "CPF": cpf,
        "IDADE": idade
    }
)

print(df)

# Gravar em um arquivo CSV

df.to_csv('DADOS_FAKES.csv', index=False)




