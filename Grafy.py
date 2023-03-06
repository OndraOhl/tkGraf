#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import filedialog
import pylab as pl

#from tkinter import ttk

class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw, width=43)

        if not ""