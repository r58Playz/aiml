from src.mergesort import merge_sort, merge_sort_return


def test_merge_sort():
    input_array = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(input_array)
    assert input_array == [3, 9, 10, 27, 38, 43, 82]


def test_merge_sort_return():
    input_array = [38, 27, 43, 3, 9, 82, 10]
    assert merge_sort_return(input_array) == [3, 9, 10, 27, 38, 43, 82]