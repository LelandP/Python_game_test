from GenerationsGame.const_manager import Constants, constants

TEST_KEY_UPPER = "TEST"
TEST_KEY_LOWER = "test"
TEST_VAL = 0
TEST_CONST_DICT = {TEST_KEY_LOWER:TEST_VAL}

class TestConstManager:
    def test_init(self):
        Constants._consts = TEST_CONST_DICT
        const = Constants()
        assert TEST_KEY_UPPER in const._constants

    def test_get(self):
        Constants._consts = TEST_CONST_DICT
        const = Constants()
        assert const.get(TEST_KEY_UPPER) == TEST_VAL

    def test_get_lower(self):
        Constants._consts = TEST_CONST_DICT
        const = Constants()
        assert const.get(TEST_KEY_LOWER) == TEST_VAL
