dct = {1: 11, 2: 22, 3: 33, 4: 5, 5: 33, 6: 1}

mn_keys = set(dct.keys())
mn_zn = set(dct.values())
ob_mn = mn_keys.union(mn_zn)
print("Мн. ключей:", mn_keys)
print("Мн. знач.: ", mn_zn)
print("Объединения мн.: ", ob_mn)

