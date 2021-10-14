import pdb
import sys
import subprocess
from math import cos, sin, pi

ASPECT = 21./10. # A 45 degree line from (1,1) --> (23, 10)
ASPECT = 15./10. # A 45 degree line from (1,1) --> (23, 10)

def bresenham_line(start, end):
    """Brensenham line algorithm"""
    PLAIN, SLOPE = range(2)
    symbols = getsymbols(start, end)
    (x,y), (x2,y2) = start, end
    steep = 0
    coords = []
    dx = abs(x2 - x)
    if (x2 - x) > 0: sx = 1
    else: sx = -1
    dy = abs(y2 - y)
    if (y2 - y) > 0: sy = 1
    else: sy = -1
    if dy > dx:
        steep = 1
        x,y = y,x
        dx,dy = dy,dx
        sx,sy = sy,sx
    d = (2 * dy) - dx
    syms = []
    delta = 0
    for i in range(0,dx):
        syms.append(symbols[d>=0])
        delta = 0
        if syms[-1] in "/\\":
            delta = getdelta(start,end)
        if steep:
            assert delta==0
            coords.append((y,x + delta))
        else:
            coords.append((x,y + delta))
        while d >= 0:
            y = y + sy
            d = d - (2 * dx)
        x = x + sx
        d = d + (2 * dy)
    syms.append(symbols[d>=0])
    delta = 0
    if syms[-1] in "/\\":
        delta = getdelta(start,end)
    coords.append((x2,y2 + delta))
    if len(coords) > 1:
        if syms[0] == "|":
            if coords[0][1] < coords[1][1]:
                syms, coords = syms[1:], coords[1:]
        if syms[-1] == "|":
            print ("HAPPENED!")
            if coords[-1][1] < coords[-2][1]:
                syms, coords = syms[:-1], coords[:-1]
    return coords, syms

class Screen(object):
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.buf = [[" "]*self.w for x in range(self.h)]
    def __str__(self):
        ans=["-----START"]
        for x in self.buf:
            ans.append("".join(x))
        ans.append("-----END")
        return "\n".join(ans)
    def line(self, start, end):
        coords, syms = bresenham_line( start, end )
##        print coords, syms
        for (a, b), sym in zip(coords, syms):
            if 0<=b<self.h and 0<=a<self.w:
                self.buf[b][a] = sym
    def text(self, text, pos):
        start = pos[0]
        for i, x in enumerate(text):
            if 0 <= pos[1] < self.h and 0 <= start+i < self.w:
                self.buf[pos[1]][start + i] = x

def nearest(f):
    """Nearest integer
    >>> nearest(0.6)
    1
    >>> nearest(0.4)
    0
    >>> nearest(-0.45)
    0
    """
    return int(f+0.5)

def getsymbols(start ,end):
    """
    >>> getsymbols((9, 4), (19, 5))
    ['_', '\\\\']
    >>> getsymbols((9, 4), (0, 3))
    ['_', '\\\\']
    >>> getsymbols((9, 4), (15, 8))
    ['_', '\\\\']
    >>> getsymbols((9, 4), (7, 9))
    ['|', '/']
    >>> getsymbols((9, 4), (3, 0))
    ['_', '\\\\']
    >>> getsymbols((9, 4), (1, 7))
    ['_', '/']
    >>> getsymbols((9, 4), (12, 9))
    ['|', '\\\\']
    """
    if end[0] < start[0]:
        start, end = end, start
    if end[0] == start[0]:
        slope = 1e99
    else:
        slope = (end[1] - start[1]) / float((end[0] - start[0]))
    if slope > 0:
        if slope > 1.0:
            ans = ["|", '\\']
        else:
            ans = ["_", '\\']
    else:
        if slope > -1.0:
            ans = ["_", "/"]
        else:
            ans = ["|", "/"]
    return ans

def getdelta(start, end):
    """
    >>> getdelta((9, 4), (18, 7))
    1
    >>> getdelta((9, 4), (12, 9))
    0
    >>> getdelta((9, 4), (7, 9))
    0
    """
    ans = 0
    if end[1] > start[1]:
        ans = 1
        slope = (end[1] - start[1]) / float((end[0] - start[0]))
        if abs(slope) > 1.0:
            ans = 0
    return ans

##def correct(start, end):
##    """
##    >>> correct( (2,2), (3,5) )
##    ((2, 3), (3, 5))
##    """
##    syms = getsymbols(start, end)
##    ns, ne = start, end
##    if syms[0] == "|":
##        if start[1] < end[1]:
##            ns = (ns[0], ns[1]+1)
##            
##    return ns, ne
##        
   
def mytest():
##    screen = Screen(10,10)
##    screen.buf[0] = list("0123456789")
##    for i in range(10):
##        screen.buf[i][0] = str(i)
##    screen.line( (2,3), (3,5))
##    print screen

    print (getsymbols((25,14), (17,11)))


def test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
##    mytest()
####    mytest()
##    import sys
##    sys.exit(0)
    star = False
    square = False
    normal = True
    if star:
        w, h = 170 ,48
        w, h = 78, 48
        screen = Screen(w, h)
        start = 0
        x, y = nearest(w/2.)-1, nearest(h/2.)-1
        oldx, oldy = w-1, y
        for ang in range(start, 360 + start + 10, 10):
            
            x2, y2 = nearest(x+w/2.*cos(ang*pi/180.)),nearest(y+h/2.0*sin(ang*pi/180.))
            screen.line((x,y), (x2,y2))
            screen.line((oldx,oldy),(x2,y2))
            oldx,oldy=x2,y2
        print(screen)
                                                              
    if square:
        w = 30
        h = nearest(w/ASPECT)
        
        screen = Screen(w, h)
        screen.line( (0,0), (w-1,0))
        screen.line( (w-1,0),(w-1,h-1))
        screen.line((w-1,h-1),(0,h-1))
        screen.line((0,h-1),(0,0))
        start = 30
        x, y = nearest(w/2.)-1, nearest(h/2.)-1
        for i, size in enumerate([w/2., w/2. - 4]):
            x2, y2 = nearest(x+size*cos(start*pi/180.)),nearest(y+(size/ASPECT)*sin(start*pi/180.))
            oldx, oldy = x2, y2
            for ang in range(start, 360 + start + 60, 60):
                x2, y2 = nearest(x+size*cos(ang*pi/180.)),nearest(y+(size/ASPECT)*sin(ang*pi/180.))
                if i==0 or (i==1 and (ang/60)%2==0 ):
                    screen.line((oldx,oldy),(x2,y2))
                oldx,oldy=x2,y2
        print(screen)

    if normal:
        smiles = "CCC(C(=O)O)CCc1cc(C(=O)Cl)ccc1"
        smiles = "c1(c2c(nc(n1)C)ccc(c2)CN(c1ccc(C(=O)NCc2scnc2)cc1)CC#C)O"
##        smiles = "c1ccc2ccccc2c1"
##        smiles = "C"*25
        output, tmp = subprocess.Popen(["obabel", "-:%s" % smiles, "-opaint", "-xM"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

        w, h = 76, 30
    ##    scale = 0.3
        screen = Screen(w, h)
        for line in output.split("\n"):
            print(line)
            broken = line.split()
            if line.startswith("DrawLine"):
                tmp = [broken[i] for i in [1,2,4,5]]
                vals = [float(x)*scale for x in tmp]
                screen.line((nearest(vals[0]), nearest(vals[1]/ASPECT)),
                            (nearest(vals[2]), nearest(vals[3]/ASPECT)))
            elif line.startswith("DrawText"):
                vals = [float(x)*scale for x in broken[1:3]]
                screen.text(broken[3][1:-1],
                            (nearest(vals[0]), nearest(vals[1]/ASPECT)))
            elif line.startswith("NewCanvas"):
                vals = [float(x) for x in broken[1:3]]
                cw, ch = vals[0], vals[1]/ASPECT
                sx, sy = w/cw, h/ch
                scale = min(sx, sy)
            elif line.startswith("DrawPolygon"):
                tmp = [broken[i] for i in [1,2,4,5,7,8]]
                vals = [float(x)*scale for x in tmp]
                screen.line((nearest(vals[0]), nearest(vals[1]/ASPECT)),
                            (nearest(vals[2]), nearest(vals[3]/ASPECT)))
                screen.line((nearest(vals[2]), nearest(vals[3]/ASPECT)),
                            (nearest(vals[4]), nearest(vals[5]/ASPECT)))
                screen.line((nearest(vals[4]), nearest(vals[5]/ASPECT)),
                            (nearest(vals[0]), nearest(vals[1]/ASPECT)))

                
        print(screen)