# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
def Boolean no_name(a : String, b : String)
if a.length != b.length
return false

    for(x : Integer = 0; x < b.length; x++)
        if a[0] == b[x]
            return no_name(utilityFunction(a, 0), utilityFunction(b, x))
        end
    end

return b.length == 0
end

def String utilityFunction(s : String, j : Integer)
ret = new char[s.length - 1]
int d = 0
    for (k : Integer = 0; k < s.length; k++)
        if (k == j)
            d = 1
        else
            ret[k - d] = s[k]
        end
    end
return new String(ret)
end"""

import unittest


def is__equal_chars(a: str, b: str) -> bool:
    """
    作用是为了判定两个字符串是否由相同的字符，字符个数组成
    使用递归方式
    复杂度O(n^2)
    :param a:
    :param b:
    :return:
    """
    if len(a) != len(b):
        return False
    for ind in range(len(b)):
        if a[0] == b[ind]:
            return is__equal_chars(a[1:], b[:ind] + b[ind + 1:])
    return len(b) == 0


def is_equal_chars(str1, str2):
    """
    使用字典方式实现
    复杂度O(2n)
    """
    cnt_dict = {}
    if len(str1) != len(str2):
        return False
    for c in str1:
        cnt_dict[c] = cnt_dict.get(c, 0) + 1
    for c in str2:
        if c not in cnt_dict:
            return False
        cnt_dict[c] -= 1
        if cnt_dict[c] < 0:
            return False
    return True


class NoNameTest(unittest.TestCase):
    def test_work(self):
        self.assertEqual(is__equal_chars("abcde", "figge"), False)
        self.assertEqual(is__equal_chars("abcdevf", "sdsfs"), False)
        self.assertEqual(is__equal_chars("abcdef", "abcdef"), True)
        self.assertEqual(is__equal_chars("abcdef", "fedcba"), True)
        self.assertEqual(is__equal_chars("abcdef", "cbafed"), True)


if __name__ == '__main__':
    unittest.main()
