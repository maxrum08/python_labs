import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''Нормализует текст'''
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
    if yo2e:
        text = text.replace('ё', 'е')
    
    text = ' '.join(text.split())
    return text

def tokenize(text: str) -> list[str]:
    """Разбивает текст на слова."""
    return re.findall(r"\w+(?:-\w+)*", text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитать частоту каждого слова."""
    freq = {}

    for word in tokens:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    '''Возвращает n самых частых слов.'''
    items = list(freq.items())
    items.sort(key = lambda item: (-item[1], item[0]))
    return items[:n]

if __name__ == '__main__':
    # normalize
    print('normalize:')
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    print("ПрИвЕт\nМИр\t"+ " => " + normalize("ПрИвЕт\nМИр\t"))
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    print()

    # tokenize
    print('tokenize:')
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    print("по-настоящему круто"+ " => " + f'{tokenize("по-настоящему круто")}')
    assert tokenize("2025 год") == ["2025", "год"]
    print()

    # count_freq + top_n
    print('count_freq:')
    freq = count_freq(["a","b","a","c","b","a"])
    assert freq == {"a":3, "b":2, "c":1}
    print(f'{["a","b","a","c","b","a"]} => {freq}')
    assert top_n(freq, 2) == [("a",3), ("b",2)]
    print()

    # тай-брейк по слову при равной частоте
    print('top_n:')
    freq2 = count_freq(["bb","aa","bb","aa","cc"])
    assert top_n(freq2, 2) == [("aa",2), ("bb",2)]
    print(f'{count_freq(["bb","aa","bb","aa","cc"])} => {top_n(freq2, 2)}')