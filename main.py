import os

def top_py_fayllar(papka_yoli):
    py_fayllar = []
    for papka, kataloglar, fayllar in os.walk(papka_yoli):
        for fayl in fayllar:
            if fayl.endswith('.py'):
                py_fayllar.append(os.path.join(papka, fayl))
    return py_fayllar

papka_yoli = '/path/to/papka'  # papka_yoli o'rniga sizning papkangizni yozib qoying
print(top_py_fayllar(papka_yoli))
```

Kodni ishlatish uchun, `/path/to/papka` o'rniga sizning papkangizni yozib qoying.
