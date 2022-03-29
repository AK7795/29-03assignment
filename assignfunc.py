def arm(a):
    s = 0
    t = a
    while t > 0:
        d = t % 10
        s += d ** 3
        t //= 10
    if a == s:
        return "yes"
    else:
        return "no"


def palin(a):
    t = a
    r = 0
    while a > 0:
        d = a % 10
        r = r * 10 + d
        a = a // 10
    if t == r:
        return "yes"
    else:
        return "no"


def divby8(a):
    if a % 8 == 0:
        return "yes"
    else:
        return "no"


def evod(a):
    if a % 2 == 0:
        return "even"
    else:
        return "odd"


def smallest(a, b, c):
    if a < b:
        if a < c:
            return a
    if b < a:
        if b < c:
            return b
    if c < a:
        if c < b:
            return c

if __name__ =="__main__":
    n1 = int(input("1 : "))
    n2 = int(input("2 : "))
    n3 = int(input("3 :"))