from math import sqrt

def rss(x, y) -> float:
    """Root of Sum of Squares

    Args:
        x (list or tuple): vector 1
        y (list or tuple): vector 2

    Returns:
        float: Root of Sum of Squares
    """
    ss : float = 0
    if (x.type == list and y.type == list) or (x.type == tuple and y.type == tuple):
        if len(x) == len(y):
            for p,q in zip(x,y):
                ss += (p-q)**2
            rss = sqrt(ss)
            return rss
        else: 
            print("Length or Type of two operands are not same")
            return -1
    else: return abs(x-y)
    
def rss(x) -> float:
    """Root of Sum of Squares

    Args:
        x (list or tuple or const)

    Returns:
        float: Root of Sum of Squares
    """
    if x.type == list or x.type == tuple:
        for i in x:
            ss += i**2
        rss = sqrt(ss)
        return rss
    else: return x

