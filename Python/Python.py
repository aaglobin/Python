def words_filter(words, startswith='', min_length =-1, endswith='', contains=''):
    if (startswith != ''):
        return ((0, 'Не умею работать с startswith', []))
    if (endswith != ''):
        return ((0, 'Не умею работать с endswith', []))
    if(type(words) is str):
        words = list(words.split())
    ans = []
    for i in range(len(words)):
        if (words[i].count(contains) != 0 and len(words[i]) >= min_length):
            ans.append(words[i])
    return((1, '', ans))