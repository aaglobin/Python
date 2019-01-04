def words_filter(words, startswith='', min_length =-1, endswith='', contains=''):
    if (startswith != ''): ## Обработка некорректного вызова функции
        return ((0, 'Не умею работать с startswith', [])) 
    if (endswith != ''): ## Обработка некорректного вызова функции
        return ((0, 'Не умею работать с endswith', []))
    if(type(words) is str): ## Если слова передали как строку то преобразовываем в лист
        words = list(words.split())
    ans = [] ## Лист с подходящими словами
    for i in range(len(words)):
        if (words[i].count(contains) != 0 and len(words[i]) >= min_length): ## Если слово подходит то добавляем его в наш новый лист
            ans.append(words[i])
    return((1, '', ans)) ## Возвращаем итог корректно отработавшей программы