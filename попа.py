dct1 = {
	'1': 12,
	'2': 24,
	'3': 36
}

dct2 = {
	'a': '3',
	'b': '6',
	'c': '9'
}
def popa_pisa(dct2):
    d = 0
    for i in dct2:
        d += int(dct2[i])
    return d
def popa(dct1):
    ad = 0
    for ib in dct1:
        ad += dct1[ib]        
    return ad
print(popa(dct1) - popa_pisa(dct2))