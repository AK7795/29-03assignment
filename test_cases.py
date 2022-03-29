import pytest
import assignfunc


#@pytest.mark.skip(reason = "something")
@pytest.mark.parametrize("a,b", [(370, "yes"), (400, "no"), (153, "yes")])
def test_arm(a, b):
    r1 = assignfunc.arm(a)
    assert r1 == b


#@pytest.mark.xfail
@pytest.mark.parametrize("a,b", [(343, "yes"), (1220, "no"), (5005, "yes")])
def test_palin(a, b):
    r2 = assignfunc.palin(a)
    assert r2 == b


@pytest.mark.parametrize("a,b", [(64, "yes"), (60, "no"), (56, "yes")])
def test_divby8(a, b):
    r2 = assignfunc.divby8(a)
    assert r2 == b


@pytest.mark.parametrize("a,b", [(64, "even"), (69, "odd"), (56, "even")])
def test_evod(a, b):
    r2 = assignfunc.evod(a)
    assert r2 == b


@pytest.mark.parametrize("a,b,c,d", [(64, 60, 65, 60), (1, 2, 3, 1), (10, 50, 60, 10)])
def test_small(a, b, c, d):
    r2 = assignfunc.smallest(a, b, c)
    assert r2 == d
