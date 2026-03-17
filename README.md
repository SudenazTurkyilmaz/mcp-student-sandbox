# mystery_module.py README

Bu modüldeki `fn_x(a, b, c)` fonksiyonu, ikinci dereceden bir denklemin

ax^2 + bx + c = 0

köklerini hesaplar.

## Fonksiyon Ne Yapar?

- Önce diskriminantı hesaplar: d = b^2 - 4ac
- Eğer d < 0 ise gerçek kök olmadığı için `None` döndürür
- Eğer d >= 0 ise iki gerçek kökü bir tuple olarak döndürür:
  - x1 = (-b + sqrt(d)) / (2a)
  - x2 = (-b - sqrt(d)) / (2a)

## Kullanım

```python
from mystery_module import fn_x

roots = fn_x(1, -3, 2)
print(roots)  # (2.0, 1.0)
```

## Not

- Bu fonksiyon gerçek sayılarda kök hesaplar.
- `a = 0` verilirse ifade ikinci dereceden denklem olmaz ve kod `2*a` bölümünde hataya gidebilir.
