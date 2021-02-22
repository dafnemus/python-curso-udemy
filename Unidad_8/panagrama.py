# pylint: disable=missing-docstring

ABC = 'abcdefghijklmnopqrstuvwxyz'


def pangram(text: str) -> bool:
    text = text.lower().replace(', ', '')
    panagrama = []
    for letra in text:
        if ABC.count(letra):
            panagrama.append(letra)
    if len(set(panagrama)) == len(list(ABC)):
        return True
    return False


pangram('abcdefg hijklmnopqrs tuvwxyz')
