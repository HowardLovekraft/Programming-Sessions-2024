def foo(listy: list) -> list[int]:
    # return [elem for elem in listy if type(elem) == int] # с помощью list comprehensions

    for elem in listy:
        if type(elem) != int:
        listy.remove(elem)
    return elem
        