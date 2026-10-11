class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for i in range(len(tokens)):
            element = tokens[i]
            if element in {"*", "+", "-", "/"}:

                #we have found an element that isn't an integer
                top = stack.pop()
                secondTop = stack.pop()
                if element == "*":
                    number = int(secondTop) * int(top)
                elif element == "+":
                    number = int(secondTop) + int(top)
                elif element == "-":
                    number = int(secondTop) - int(top)
                else:
                    assert(element == "/")
                    assert(int(top) != 0)
                    number = int(int(secondTop) / int(top))

                stack.append(number)
            else:
                stack.append(int(element))
        return int(stack.pop())

        