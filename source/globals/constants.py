# -*- coding: utf-8 -*-

############################################################################
#
#   Copyright (C) 2010-2015
#    Christian Kohlöffel
#    Jean-Paul Schouwstra
#
#   This file is part of DXF2GCODE.
#
#   DXF2GCODE is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   DXF2GCODE is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with DXF2GCODE.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################

"""
All global constants are initialized in this module.
They are used in the other modules.

see http://code.activestate.com/recipes/65207/ for module const

@purpose:  initialization of the global constants used within the other modules.
"""

import logging

'''
By default we (should) want to run the PyQt5 version
'''
PYQT5notPYQT4 = True
try:
    import PyQt5
except ImportError:
    PYQT5notPYQT4 = False

# Our 3D mode is only possible with PyQt5 v5.4
VIEW3D = True

# Global Variables
APPNAME = "DXF2GCODE"
VERSION = "PyQt4 Beta"

DATE     =  "$Date$"
REVISION =  "$Revision$"
AUTHOR   = u"$Author$"

CONFIG_EXTENSION = '.cfg'
PY_EXTENSION = '.py'

# Rename unreadable config/varspace files to .bad
BAD_CONFIG_EXTENSION = '.bad'
DEFAULT_CONFIG_DIR = 'config'
DEFAULT_POSTPRO_DIR = 'postpro_config'

# log related
DEFAULT_LOGFILE = 'dxf2gcode.log'
STARTUP_LOGLEVEL = logging.DEBUG
# PRT = logging.INFO
