'''
Сериализация (Pickling): Преобразование объекта в поток байтов, который можно сохранить в файл, отправить по сети или в бд
Десериализация (Unpickling): Наоборот, восстановление объекта из потока байтов

Pickle
Модуль pickle в Python предоставляет удобные функции для выполнения этих операций, 
однако его не рекомендуется использовать для данных из ненадежных источников из-за уязвимостей безопасности при десериализации, 
которая может выполнить произвольный код. 

Функции модуля Pickle для сохранения/загрузки объектов:

pickle.dump(obj, file, protocol=None, *, fix_imports=True) - записывает сериализованный объект в файл. Дополнительный аргумент protocol указывает используемый протокол

pickle.dumps(obj, protocol=None, *, fix_imports=True) - возвращает сериализованный объект

pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict") - загружает объект из файла

pickle.loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict") - загружает объект из потока байт

Модуль pickle также определяет несколько исключений:

pickle.PickleError
    pickle.PicklingError - проблема с сериализацией объекта.
    pickle.UnpicklingError - проблема с десериализацией объекта.
    
Пример:
import pickle

# Сериализация словаря в байтовую строку
my_dict = {'a': 1, 'b': [1, 2, 3]}
pickled_data = pickle.dumps(my_dict)
print(f"Сериализованные данные (байты): {pickled_data}")

# Десериализация байтовой строки обратно в объект
unpickled_dict = pickle.loads(pickled_data)
print(f"Десериализованный объект: {unpickled_dict}")

'''