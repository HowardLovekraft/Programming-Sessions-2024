import math
def percentile_of_seq(seq: list[int], percentile: int) -> list:
    """
    Функция возвращает значения из N-ого процентиля последовательности, т.е. первые N% значений из отсортированной последовательности. Подробнее про процентиль - на википедии.
        :param seq: Последовательность, для которой вычисляется квантиль
        :param percentile: Номер процентиля (от 1 до 99)
        :return result: Список - числа, входящие в N-ый процентиль
    """
    sorted_seq = sorted(seq)
    seq_len = len(sorted_seq)
    percentile_len = math.ceil(seq_len * 0.01 * percentile)
    result = sorted_seq[:percentile_len]

print(percentile_of_seq([1, 2, 3, 4, 5], 40)) # В консоли должно появиться "[1,2]"
