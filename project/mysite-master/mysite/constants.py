class _CONS(int):
    def __new__(cls, value, display_name):
        obj = int.__new__(cls, value)
        obj.display_name = display_name
        return obj

    def get_display_name(self):
        return self.display_name

TEST_PROJECT_TESTLINK = 1

TEST_STATUS_WAIT = _CONS(1, 'Wait')
