#!/usr/bin/env python
#coding:utf8

from distutils.core import setup
import matplotlib as mpl
import py2exe
mpl.use('qt4agg')
import sys
import pylab
import openpyxl

includes = ['sip', 'PyQt4', 'PyQt4.QtGui', 'PyQt4.QtCore', "matplotlib.backends",
    "matplotlib.backends.backend_qt4agg", "matplotlib.figure","pylab",
    "encodings", "encodings.*", "email"
    ]

excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'pywin.debugger', 'pywin.debugger.dbgcon', 'pywin.dialogs', 'wx', 'tcl', 'tk']
packages = ['matplotlib', 'pytz', "encodings", "email"]
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'libgdk_pixbuf-2.0-0.dll', "mswsock.dll", "powrprof.dll" ]
data_files = mpl.get_py2exe_datafiles()

setup(
    options = {
        "py2exe": {
                    "compressed": 1,
                      "optimize": 2,
                      "includes": includes,
                      "excludes": excludes,
                      "packages": packages,
                      "dll_excludes": dll_excludes,
                      "bundle_files": 1,
                      "dist_dir": 'gprs',
                      "xref": False,
                      "skip_archive": False,
                      "ascii": False
        },
    },
    data_files=data_files,
    name = 'gprs',
    windows=[{"script": "gprs.py", "icon_resources":[(0, "logo.ico"),(1, "logo.ico")]}]
)
