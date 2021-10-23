import numpy as np
from utils import AList


class TestAList:
    def test_files_io(self) -> None:
        # uses a code from Mackay with known params
        original_file = "tests/test_data/Mackay_96.3.963.alist"
        a = AList.from_file(original_file)
        assert a.n == 96
        assert a.m == 48
        assert a.largest_column_weight == 3
        assert a.largest_row_weight == 6
        assert a.column_weights == [3]*96
        assert a.row_weights == [6]*48

        test_file = "tests/test_data/test.alist"
        a.to_file(test_file)
        with open(original_file, "r") as o_file:
            with open(test_file, "r") as n_file:
                assert o_file.read() == n_file.read()

    def test_array_io(self) -> None:
        """matrix:      [[1,1,1]
                        [1,1,0]
                        [0,0,1]
                        [0,1,1]]
        """
        arr = np.array([[1, 1, 1], [1, 1, 0], [0, 0, 1], [0, 1, 1]])
        a = AList.from_array(arr)
        assert arr.shape == (a.m, a.n)
        assert a.largest_row_weight == 3
        assert a.largest_column_weight == 3
        assert a.column_weights == [2, 3, 3]
        assert a.row_weights == [3, 2, 1, 2]
        assert a.non_zero_elements_in_row == [[1, 2, 3],
                                              [1, 2],
                                              [3],
                                              [2, 3]]
        assert a.non_zero_elements_in_column == [[1, 2],
                                                 [1, 2, 4],
                                                 [1, 3, 4]]
        b = a.to_array()
        np.testing.assert_array_equal(arr, b)  # type: ignore

    def test_verify_alist(self) -> None:
        original_file = "tests/test_data/Mackay_96.3.963.alist"
        a = AList.from_file(original_file)
        assert a.verify_elements() is True