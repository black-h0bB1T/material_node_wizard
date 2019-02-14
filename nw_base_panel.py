# Copyright (C) 2019 h0bB1T
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
#
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

import bpy
from bpy.types import Panel

class NW_BasePanel(Panel):
    def add_row(self):
        return self.layout.row()

    def add_center_row(self):
        row = self.layout.row()        
        row.alignment = "CENTER"
        return row

    def add_separator(self):
        self.layout.row().separator()

    def add_label(self, title):
        self.layout.row().label(text=title)

    def add_split_row(self, factor=1.0):
        row = self.layout.row()
        row.split(factor=factor)
        return row