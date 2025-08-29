import my_functions

class TestFunctions:
    def test_hi(self):
        assert "Hello!" == my_functions.say_hi()

    def test_bye(self):
        assert "Goodbye!" == my_functions.say_bye()