class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        assert a + b == 14, "We wait 14 here"


    def test_check_math2(self):
        a = 5
        b = 10
        assert a + b == 11, "We wait 11 here"