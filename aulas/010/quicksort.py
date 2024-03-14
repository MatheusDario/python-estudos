def soma(lista):
  if lista == []: 
    return 0
  return lista[0] + soma(lista[1:])

def count(itens):
  if itens == []:
    return 0
  return 1 + count(itens[1:])

def maior(lista):
  if len(lista) == 2:
    return lista[0] if lista[0] > lista[1] else lista[1]
  sub_max = maior(lista[1:])
  return lista[0] if lista[0] > sub_max else sub_max

def max(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    else:
        max_num = max(lst[1:])
        return lst[0] if lst[0] > max_num else max_num
    
print(max([10, 20, 11, 9]))