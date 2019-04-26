import random


def gen_rect():
    a=random.random()*10
    b=random.random()*10+5.0
    return [a, b]

def gen_pts_poly(a, b, hor=True):
    if(hor==True):
        pt=[(a, 0.0, 0.0), (b, 0.0, 0.0)]
        poly=[(a, 0.0, 0.0), (b, 0.0, 0.0), (b, 0.2, 0.0), (a, 0.2, 0.0), (a, 0.0, 0.0)]
    else:
        pt = [(a, 0.0, 0.0), (a, b, 0.0)]
        poly = [(a, 0.0, 0.0), (a+0.2, 0.0, 0.0), (a+0.2, b, 0.0), (a, b, 0.0), (a, 0.0, 0.0)]
    return [pt, poly]