# 괄호 테스트
def bracket_test(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0

print('()())()(', bracket_test((')())()(')))
print('((()))()', bracket_test(('((()))()')))
print('(()((test)))', bracket_test(('(()((test)))')))

