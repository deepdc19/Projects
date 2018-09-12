from nose.tools import assert_equal

class testStack:
    #TODO : Testing the stack code using test code.

    def test_all():
        print('Test:Empty Stack')
        stack = Stack()
        assert_equal(stack.peek(),None)
        assert_equal(stack.pop(),None)

        print('Test:One element')
        top = Nope(10)
        stack = Stack(top)
        assert_equal(stack.peek(),10)
        assert_equal(stack.pop(),10)
        assert_equal(stack.peek(),None)

        print('Test:Multiple elements')

            



