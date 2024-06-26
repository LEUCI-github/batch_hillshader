﻿# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Batch_Hillshader
                                 A QGIS plugin  to generate a three light 
                                 exposure hillshade (shaded relief by 
                                 combining three light exposures)
  
    For more information, see the program documentation.
                                 
    If you uses as input LiDAR data, note that plugin uses LASTools library.
        See LASTools License at  <https://rapidlasso.com/lastools/>
        
    Plugin also use in LiDAR data mode FUSION LDV. 
        See FUSION LDV License at <http://forsys.cfr.washington.edu/fusion.html>
                              -------------------
        begin                : 2016-07-13
        git sha              : $Format:%H$
        copyright            : (C) 2017 by PANOimagen S.L.
        email                : info@panoimagen.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software: you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation, either version 3 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       * 
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program.  If not, see <https://www.gnu.org/licenses/> *
 ***************************************************************************/
"""
from __future__ import unicode_literals


def fix(iface):
    """Fix bug with some QGis versions fail due to use of print with unicode.

    On some QGis versions, calls to print with unicode characters fail when the
    python console has not been launched yet.
    This fix sends a unicode character to print and,
    if unicodeencodeerror shows, opens the python console to keep from showing
    again.
    """
    try:
        if iface.UNICODEENCODEERROR_FIXED:
            # This interface has already been tested successfully
            return
    except AttributeError:
        iface.UNICODEENCODEERROR_FIXED = False

    test_message = "áéíóúñâäÓÙ¿¡"
    try:
        print('Unicode test: {}'.format(test_message))
        iface.UNICODEENCODEERROR_FIXED = True
        return
    except UnicodeEncodeError:
        iface.actionShowPythonDialog().trigger()

    #Now test that everythin works fine:
    try:
        print('Now unicode should work: {}'.format(test_message))
        iface.UNICODEENCODEERROR_FIXED = True
    except UnicodeEncodeError:
        print("UnicodeEncodeError fix does not seem to work"
              +" with this version of QGis!!!")
