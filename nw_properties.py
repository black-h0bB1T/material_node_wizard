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

from bpy.props import EnumProperty, BoolProperty, IntProperty, PointerProperty
from bpy.types import PropertyGroup, WindowManager

from . nw_preview_helper import NW_PreviewHelper

class NW_Properties(PropertyGroup):

    add_hslbc: BoolProperty(name="Add HSL/BC Setup")
    add_uv: BoolProperty(name="Add UV Input")
    decal: BoolProperty(name="Clip Texture/Decal")
    nodes_previews: EnumProperty(items = lambda _, __: NW_PreviewHelper.getCollection("nodes").items)
    materials_previews: EnumProperty(items = lambda _, __: NW_PreviewHelper.getCollection("materials").items)        

    @staticmethod
    def initialize():
        WindowManager.nw_properties = PointerProperty(type=NW_Properties)

    @staticmethod
    def cleanup():
        del(WindowManager.nw_properties)
