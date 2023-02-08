def monotonic_array(lst):
    """
    1 Kata

    This function returns True/False if the given list is monotonically increased or decreased

    :param lst: list of numbers (int, floats)
    :return: bool: indicating for monotonicity
    """
    lst1, lst2 = [], []
    lst1.extend(lst)
    lst2.extend(lst)

    lst1.sort() 
    lst2.sort(reverse=True)

    if (lst1 == lst or lst2 == lst):
        return True
    else:
        return False
        