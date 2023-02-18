from bank_account import bank_balance, average_check
from file_tools import list_to_sep_str


def test_bank_balance():
    assert bank_balance(0) == '💰 Остаток на счету: 0'
    assert bank_balance(125) == '💰 Остаток на счету: 125'


def test_average_check():
    assert average_check({}) == 'Еще не было покупок!', 'Нет истории еще'
    assert average_check({'tools': 50.0, 'tv': 30.0}) == '🛒Средний чек = 40.0'
    assert average_check({'books': 150.0}) == '🛒Средний чек = 150.0'


def test_list_to_sep_str():
    assert list_to_sep_str([]) == ''
    assert list_to_sep_str(['file1', 'file2', 'file3']) == 'file1, file2, file3'
    assert list_to_sep_str(['.dir1', '.dir2']) == '.dir1, .dir2'