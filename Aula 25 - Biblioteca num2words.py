# Biblioteca num2works

from num2words import num2words as rw

# Extenso de números
print()
print(rw(1020))
print(rw(1199.66))
print(rw(12, 'ordinal'))
print(rw(1020, lang ='pt_BR'))
print(rw(1231.88, lang ='pt_BR'))

# Extenso de valores monetarios
print(rw(1300.37, lang ='pt_BR'))
print(rw(1300.37, lang ='pt_BR'),'reais')
print(rw(1300.37, lang ='pt_BR'),'reais e', rw(88, lang ='pt_BR'),'centavos')
print(rw(1300.37, lang ='pt_BR', to='currency'))
print(rw(125.66, lang ='pt_BR', to='currency'))
print()

print(rw(125.66, lang ='es-ES', to='currency'))
print(rw(125.66, lang ='ko'))
print(rw(125.66, lang ='ja'))
print(rw(125.66, lang ='ru'))
print()

print(rw(2025, lang='pt_BR', to='year'))
print(rw(2025, lang='pt_BR', to='year'))