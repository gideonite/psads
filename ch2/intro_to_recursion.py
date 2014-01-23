#!/usr/bin/python

def reverse(string):
    def helper(string, acc):
        if '' == string:
            return "".join(acc)
        acc.insert(0, string[0])
        return helper(string[1:], acc)

    return helper(string, [])

assert "gnirts" ==  reverse("string")

def is_palindrome(string):
    '''
    string -> bool.
    '''
    if len(string) <= 1:
        return True

    ignores = " ,;.!?'’"

    # skip spaces coming from left
    if string[0] in ignores:
        return is_palindrome(string[1:])

    # skip spaces coming from right
    if string[-1] in ignores:
        return is_palindrome(string[:-1])

    if string[0].lower() == string[-1].lower():
        return is_palindrome(string[1:-1])

    return False

assert is_palindrome("k")
assert not is_palindrome("ka")
assert is_palindrome("kk")
assert is_palindrome("kayak")
assert is_palindrome("aibohphobia")
assert is_palindrome("Live not on evil")
assert is_palindrome("Reviled did I live, said I, as evil I did deliver")
assert is_palindrome("Go hang a salami; I’m a lasagna hog.")
assert is_palindrome("Able was I ere I saw Elba")
assert is_palindrome("Kanakanak")
assert is_palindrome("Wassamassaw")
