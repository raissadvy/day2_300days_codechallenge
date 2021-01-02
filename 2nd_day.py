# soal 1
import numpy as np
import operator as op

def jml_kata (b):
    return (f"Jumlah kata adalah sebanyak :{len(b)}")

def jml_kata_unik (b):
    unique, counts = np.unique(b, return_counts=True)
    c = dict(zip(unique, counts))
    return (f"Jumlah masing-masing kata :{c}")

def kata_muncul_sekali (b):
    try :
        unique, counts = np.unique(b, return_counts=True)
        c = dict(zip(unique, counts))
        d = [k for k, v in c.items() if v == 1]
        return (f"Kata yang muncul hanya sekali :{d}")
    except :
        return "tidak ada kata yang muncul cuma sekali"
    
def paling_banyak_muncul (b):
    e = create_dict(b)
    f = max(e.items(), key=op.itemgetter(1))[0]
    return (f"Kata yang paling banyak muncul : {f}x muncul -> {e[f]}")

def paling_sedikit_muncul (b):
    e = create_dict(b)         
    f = min(e.items(), key=op.itemgetter(1))[0]
    return (f"Kata yang paling sedikit muncul : {f}x muncul -> {e[f]}")

def create_dict (b):
        e = {}
        unique, counts = np.unique(b, return_counts=True)
        c = dict(zip(unique, counts))
        for i, v in c.items():
                e[v] = [i] if v not in e.keys() else e[v] + [i]
        return e

a = input("Masukkan teks :")
b = a.split()
print()
display(jml_kata(b))
print()
display(jml_kata_unik(b))
print()
display(kata_muncul_sekali(b))
print()
display(paling_banyak_muncul(b))
print()
display(paling_sedikit_muncul(b))

#soal 2

a = [12345,12344,12334]
aa = list(map(str, a))
b = [i[:3]+'**' for i in aa]
b 