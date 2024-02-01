from integrate import riemann_sum

def test_integrand(x):
    """ function to integrate"""
    return 3.0 * (x ** 2)

riemann_sum(test_integrand, 0.0, 1.0, 10000)