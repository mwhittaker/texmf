"""
This file contains classes, decorators, and functions that help write latex
code from within python.
"""

import numpy as np

################################################################################
# begin-ends
################################################################################
class begend(object):
    """
    A decorator to wrap text in an environment.

    \\begin{tag}
        f(*args, **kwargs)
    \\end{tag}

    """
    def __init__(self, tag, opts=""):
        self.tag_  = tag
        self.opts_ = opts

    def __call__(self, f):
        def f_(*args, **kwargs):
            print "\\begin{%s}%s" % (self.tag_, self.opts_)
            f(*args, **kwargs)
            print "\\end{%s}" % self.tag_
        return f_

################################################################################
# before and after
################################################################################
class before(object):
    """
    A decorator to insert text before.

    \\command{args}
    code
    """
    def __init__(self, tag, args="", opts=""):
        self.tag_  = tag
        self.args_ = args
        self.opts_ = opts

    def __call__(self, f):
        def f_(*args, **kwargs):
            print "\\%s{%s}%s" % (self.tag_, self.args_, self.opts_)
            f(*args, **kwargs)
        return f_

class after(object):
    """
    A decorator to insert text before.

    \\command{args}
    code
    """
    def __init__(self, tag, args="", opts=""):
        self.tag_  = tag
        self.args_ = args
        self.opts_ = opts

    def __call__(self, f):
        def f_(*args, **kwargs):
            f(*args, **kwargs)
            print "\\%s{%s}%s" % (self.tag_, self.args_, self.opts_)
        return f_

################################################################################
# backslash commands
################################################################################
def backslash(tag, opts=""):
    def f(s):
        print "\\%s%s{%s}" % (tag, opts, s)
    return f

section       = backslash("section")
subsection    = backslash("subsection")
subsubsection = backslash("subsubsection")
paragraph     = backslash("paragraph")
subparagraph  = backslash("subparagraph")
textbf        = backslash("textbf")
textit        = backslash("textit")

################################################################################
# matrices
################################################################################
def matrix(a, m="p"):
    """
    Returns a LaTeX bmatrix [http://stackoverflow.com/a/17131750/3187068]

    :a: numpy array
    :m: type of matrix
    :returns: LaTeX matrix as a string
    """
    np.set_printoptions(precision=2, suppress=True)
    if len(a.shape) > 2:
        raise ValueError('matrix can at most display two dimensions')
    mstring = m + "matrix"
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{%s}' % mstring]
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{%s}' % mstring]
    print '\n'.join(rv)

def svd(a, m="p"):
    U, s, V = np.linalg.svd(a)
    S = np.zeros(a.shape)
    S[:s.size, :s.size] = np.diag(s)
    matrix(a, m)
    print "="
    matrix(U, m)
    matrix(S, m)
    matrix(np.transpose(V), m)
    print "^{T}"
