import re

coins_: dict[int] = {
    '5c': 5,
    '10c': 10,
    '20c': 20,
    '50c': 50,
    '1e': 100,
    '2e': 200
}

num_val: dict[str, int] = {
    r'^00\d+$': 150,
    r'^8(?!08)\d{8}$': 0,
    r'112': 0,
    r'^808\d{6}$': 10,
    r'^9(1|2|3|6)\d{7}$': 25,
    r'^2\d{8}$': 25
}

def number_checker(num: str) -> int:
    for k, v in num_val.items():
        if re.match(k, num):
            if k == '112':
                print('Chamada de emergência!')
            return v
    return -1


def coin_checker(coins: list[str]) -> int:
    charge: int = 0
    for coin in coins.split(','):
        if coin not in coins_:
            print(f'Invalid coin: {coin}')
        else:
            charge += coins_[coin]
    return charge

def change_maker(cur_bal: int):
    change: dict[int, int] = {5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0}
    for coin in sorted(change, reverse=True):
        while cur_bal >= coin:
            change[coin] += 1
            cur_bal -= coin
    coins: list[str] = [f"{k}x{change[v]}" for k, v in sorted(coins_.items()) if change[v]]
    print(f"Moedas devolvidas: {', '.join(coins)}")

if __name__ == '__main__':
    levantado = False
    cur_bal: int = 0
    while True:
        read = input('maq in touch > ')
        if re.match(r'^\s*LEVANTAR\s*$', read) and not levantado:
            print('Telefone levantado. Insira moedas ou efetue uma chamada grátis.')
            levantado = True
        elif levantado:
            if m := re.fullmatch(r'^\s*MOEDA\s+(?P<coins>(.*,?)+)\s*$', read):
                cur_bal += coin_checker(re.sub(r'\s+', r'', m.groupdict()['coins']))
                print(f"Saldo atual: {(cur_bal/100):.2f}€")
            
            elif m := re.fullmatch(r'^\s*T\s*=\s*(?P<num>00\d+|\d{9}|112)\s*$', read):
                cost: int = number_checker(m.groupdict()['num'])
                if cost == -1:
                    print('Insira um número válido!')
                elif cur_bal - cost < 0:
                    print(f'Não tem saldo suficiente para efetuar esta operação!')
                else:
                    cur_bal -= cost
                print(f'Custo total da operação: {(cost/100):.2f}€; Saldo atual: {(cur_bal/100):.2f}€')
            
            elif re.fullmatch(r'\s*POUSAR\s*', read):
                if cur_bal != 0:
                    print(f'Troco total: {(cur_bal/100):.2f}€; ', end='')
                    change_maker(cur_bal)
                print('Obrigado e volte sempre!')
                break
            
            else:
                print('Input inválido, por favor inserir um input correto')
        else:
            print('Para iniciar a operação, escreva \'LEVANTAR\'')
