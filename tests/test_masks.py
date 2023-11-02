from src.masks import do_mask_cart_number, do_mask_account_number, make_dict_content_folder


def test_do_mask_cart_number_for_str():
    assert do_mask_cart_number('1234567891234567') == '1234 56** **** 4567'


def test_do_mask_cart_number_for_int():
    assert do_mask_cart_number(1234567891234567) == '1234 56** **** 4567'


def test_do_mask_account_number_str():
    assert do_mask_account_number('01234567890123456789') == '**6789'


def test_do_mask_account_number_int():
    assert do_mask_account_number(12345678901234567890) == '**7890'


def test_make_dict_content_folder():
    assert make_dict_content_folder(r'C:\Users\user\YandexDisk\SkyPro\lesson_code'
                                    r'\pythonProject\tests\test_folder') == {'files': 1, 'folders': 1}


def test_make_dict_content_folder_req():
    assert make_dict_content_folder(r'C:\Users\user\YandexDisk\SkyPro\lesson_code'
                                    r'\pythonProject\tests\test_folder', True) == {'files': 2, 'folders': 1}
