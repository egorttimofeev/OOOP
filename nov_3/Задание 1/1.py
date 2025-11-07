'''
Сериализация (Pickling): Преобразование объекта в поток байтов, который можно сохранить в файл, отправить по сети или в бд
Десериализация (Unpickling): Наоборот, восстановление объекта из потока байтов

Pickle
Модуль широко применятеся для сериализации и десериализации объектов в Python

функции модуля Pickle для сохранения/загрузки объектов:

pickle.dump(obj, file, protocol=None, *, fix_imports=True) - записывает сериализованный объект в файл. Дополнительный аргумент protocol указывает используемый протокол

pickle.dumps(obj, protocol=None, *, fix_imports=True) - возвращает сериализованный объект

pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict") - загружает объект из файла

pickle.loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict") - загружает объект из потока байт

Модуль pickle также определяет несколько исключений:

pickle.PickleError
    pickle.PicklingError - проблема с сериализацией объекта.
    pickle.UnpicklingError - проблема с десериализацией объекта.
'''