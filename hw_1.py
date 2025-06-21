from typing import Sequence, Tuple

def min_max(arr: Sequence[float]) -> Tuple[float, float]:
    """
    Divide‑and‑conquer пошук мінімального та максимального значень у послідовності.

    Параметри
    ----------
    arr : Sequence[float]
        Непорожня послідовність чисел.

    Повертає
    --------
    Tuple[float, float]
        Кортеж (min_value, max_value).

    Винятки
    -------
    ValueError
        Якщо вхідна послідовність порожня.

    Складність
    ----------
    Часова: O(n)
    Пам’яті (стек): O(log n) у середньому випадку.
    """
    if not arr:
        raise ValueError("Input sequence must not be empty.")

    def helper(lo: int, hi: int) -> Tuple[float, float]:
        if lo == hi:  # одна позиція
            return arr[lo], arr[lo]
        if hi == lo + 1:  # дві позиції
            if arr[lo] < arr[hi]:
                return arr[lo], arr[hi]
            return arr[hi], arr[lo]
        mid = (lo + hi) // 2
        min_left, max_left = helper(lo, mid)
        min_right, max_right = helper(mid + 1, hi)
        return min(min_left, min_right), max(max_left, max_right)

    return helper(0, len(arr) - 1)
