"""
FizzBuzz on Python
"""
class FizzBuzz:
    """
    FizzBuzzのlogic部分
    @param num_eval: parameter "num_eval" description
    @type num_eval: int

    @return: None
    """
    def logic(self, num_eval):
        out = "";
        for i in range(1, num_eval+1):
            if i % 3 == 0:
                out = "Fizz"
            if i % 5 == 0:
                out += "Buzz"
            if out == "":
                out = i
            print(out)
            out = ""

# 出力用
fizz_buzz = FizzBuzz()
fizz_buzz.logic(num_eval = 100)
