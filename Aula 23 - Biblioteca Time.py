import time

print()
relogio = time.localtime()
print(relogio)

print()

ano = relogio.tm_year
print(ano)

print()

ano = relogio.tm_year
mes = relogio.tm_mon
dia = relogio.tm_mday
hora = relogio.tm_hour
minuto = relogio.tm_min
segundo = relogio.tm_sec
diadoano = relogio.tm_yday
diadasemana = relogio.tm_wday

print(dia, mes, ano)
print(hora, minuto, segundo)
print(diadoano, diadasemana)

print()

relogio_ini = time.localtime()
relogio_em_segundos = time.mktime(relogio_ini)
relogio_em_segundos += 5
relogio_fim = time.localtime(relogio_em_segundos)

print()

while True:
    localTime = time.localtime()
    result = time.strftime("%d/%m/%Y %H:%M:%S", localTime)
    print(result)
    time.sleep(1)

    if localTime == relogio_fim:
        exit()

