# 2
```
- i.

class CustomQuerySet(QuerySet):
    def delete(self): 
        self.update(active=False)
    def delete_real(self): 
        super(CustomQuerySet, self).delete_real()
```
delete_real не существует у родителя

```
- ii.

class CustomQuerySet(QuerySet):
    def delete(self):
        self.update(active=False)
    def delete_real(self): 
        super(CustomQuerySet, self).delete()
```
Правильный вариант удаление лишь обновляет соответствующую колонку, либо удаляет физически если это необходимо через новый метод delete_real

```
- iii.

class CustomQuerySet(QuerySet):
    def delete(self):
        self.active = False
    def delete_real(self):
        super(CustomQuerySet, self).delete()
```
свойство active существует у модели а не у qs а значит не меняет значение в БД

```
- iv.

class CustomQuerySet(QuerySet):
    def delete(self): 
        self.active = False
    def delete_real(self): 
        super(CustomQuerySet, self).delete_real()
```
свойство active существует у модели а не у qs а значит не меняет значение в БД

------

Правильный вариант
```
- ii.

class CustomQuerySet(QuerySet):
    def delete(self):
        self.update(active=False)
    def delete_real(self): 
        super(CustomQuerySet, self).delete()
```
