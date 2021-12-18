# 3
```
class Person(models.Model):
    name = models.CharField('Item', max_length=100) birthday =
    models.DateField(...)
```

```
- i. 

birthday = models.DateField(null=True, blank=True)
```
Разрешенны пустые значения + разрешенны None

```
- ii.

birthday = models.DateField(null=False, blank=True)
```
Разрешенны пустые значения + запрещенны None

```
- iii.

birthday = models.DateField(null=True, blank=False)
```
Запрещенны пустые значения + разрешенны None

 ```
- iv.

birthday = models.DateField(null=False, blank=False)
```
Запрещенны пустые значения + запрещенны None

------

Правильный вариант
```
- iii.

birthday = models.DateField(null=True, blank=False)
```