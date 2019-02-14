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

bl_info = {
    "name": "Node Wizard",
    "description": "Create material and utility nodes",
    "author": "h0bB1T",
    "version": (0, 1, 0, 0),
    "blender": (2, 80, 0),
    "location": "NodeEditor",
    "category": "Material"
}

import bpy, os

from bpy.props import *

from . nw_generate_op       import NW_GenerateOperator
from . nw_tools_op          import *
from . nw_panel             import NW_Panel
from . nw_node_importer_op  import NW_NodeImporter
from . nw_preview_helper    import NW_PreviewHelper
from . nw_properties        import NW_Properties

ops = [
    NW_GenerateOperator,
    NW_NormalScalerOperator,
    NW_DX2OGLConverterOperator,
    NW_GenerateTwoLayerTextureBasedSetupOperator,
    NW_GenerateTwoLayerShaderBasedSetupOperator,
    NW_GenerateDistortionOperator,
    NW_GenerateBlurOperator,
    NW_Panel,
    NW_NodeImporter,
    NW_Properties
]

def register():
    for op in ops:
        bpy.utils.register_class(op)

    home = os.path.dirname(__file__)
    NW_PreviewHelper.addCollection(home, "nodes")
    NW_PreviewHelper.addCollection(home, "materials")

    NW_Properties.initialize()
    
def unregister():
    NW_Properties.cleanup()

    NW_PreviewHelper.removeAllCollections()

    for op in ops:
        bpy.utils.unregister_class(op)

if __name__ == "__main__":
    register()
