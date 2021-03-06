def todos_numeros_iguais(cpf):
    if len(cpf) < 0:
        return True
    return all(x == cpf[0] for x in cpf)

def recupera_soma(cpf, fator):
    return sum([int(n) * (fator -pos) for pos, n in enumerate(cpf[:9])])  

def recupera_digito(soma):
    resultado = (soma * 10) % 11
    if resultado == 10:
        return 0
    return resultado     
def recupera_primeiro_digito(cpf):
    soma = recupera_soma(cpf, 10)
    return recupera_digito(soma)   

def recupera_segundo_digito(cpf, primeiro_digito):
    soma = recupera_soma(cpf, 11) + (primeiro_digito * 2)    
    return recupera_digito(soma)    

def cpf_valido(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isnumeric() or todos_numeros_iguais(cpf):
        return False
    digito1 = recupera_primeiro_digito(cpf)
    digito2 = recupera_segundo_digito(cpf, digito1)
    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])      

if __name__ == '__main__':
    print('Informe o CPF')
    cpf = input()
    if cpf_valido(cpf):
        print('CPF é válido.')
    else:
        print('CPF inválido')
