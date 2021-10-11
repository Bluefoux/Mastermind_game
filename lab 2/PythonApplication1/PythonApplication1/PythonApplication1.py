
import time, os, sys
import tkinter as tk

self.master.title(title)
self.pack()
master.resizable(0,0)
self.foreground = "black"
self.items = []
self.mouseX = None
self.mouseY = None
self.bind("<Button-1>", self._onClick)
self.bind_all("<Key>", self._onKey)
self.height = int(height)
self.width = int(width)
self.autoflush = autoflush
self._mouseCallback = None
self.trans = None
self.closed = False
master.lift()
self.lastKey = ""
if autoflush: _root.update()

def __init__(self, title="Graphics Window", width=200, height=200, autoflush=True):
    assert type(title) == type("Hello!")
    master = tk.Toplevel
    master.protocol("DELETE WINDOW", self.close)












