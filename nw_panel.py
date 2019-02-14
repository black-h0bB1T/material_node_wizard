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
from bpy.types import Panel, WindowManager
from bpy.props import EnumProperty, StringProperty

from . nw_base_panel       import NW_BasePanel
from . nw_preview_helper   import NW_PreviewHelper
from . nw_generate_op      import NW_GenerateOperator
from . nw_tools_op         import *
from . nw_node_importer_op import NW_NodeImporter

class NW_Panel(NW_BasePanel):
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_label = "Node Wizard"
    bl_category = "Node Wizard"

    def draw(self, context):
        properties = context.window_manager.nw_properties

        self.add_label("Material from Textures")

        op = self.add_split_row().operator(NW_GenerateOperator.bl_idname, text="PBR Setup", icon="UV")
        op.mode = "PBR"
        op.add_hslbc = properties.add_hslbc
        op.add_uv = properties.add_uv
        op.decal = properties.decal

        op = self.add_split_row().operator(NW_GenerateOperator.bl_idname, text="From Diffuse Image", icon="UV")
        op.mode = "Image"
        op.add_hslbc = properties.add_hslbc
        op.add_uv = properties.add_uv
        op.decal = properties.decal
    
        self.add_center_row().prop(properties, "add_hslbc")
        self.add_center_row().prop(properties, "add_uv")
        self.add_center_row().prop(properties, "decal")
        self.add_separator()

        #########################################

        self.add_label("Material Layers")
        self.add_split_row().operator(
            NW_GenerateTwoLayerShaderBasedSetupOperator.bl_idname,
            text=NW_GenerateTwoLayerShaderBasedSetupOperator.bl_label,
            icon="RENDERLAYERS"
        )
        self.add_split_row().operator(
            NW_GenerateTwoLayerTextureBasedSetupOperator.bl_idname,
            text=NW_GenerateTwoLayerTextureBasedSetupOperator.bl_label,
            icon="RENDERLAYERS"
        )
        self.add_separator()

        #########################################

        self.add_label("Node Support Tools")
        self.add_split_row().operator(
            NW_NormalScalerOperator.bl_idname, 
            text=NW_NormalScalerOperator.bl_label, 
            icon="EMPTY_SINGLE_ARROW"
            )
        self.add_split_row().operator(
            NW_DX2OGLConverterOperator.bl_idname,
            text=NW_DX2OGLConverterOperator.bl_label,
            icon="ARROW_LEFTRIGHT"
        )
        self.add_split_row().operator(
            NW_GenerateDistortionOperator.bl_idname,
            text=NW_GenerateDistortionOperator.bl_label,
            icon="EMPTY_ARROWS"
        )
        self.add_split_row().operator(
            NW_GenerateBlurOperator.bl_idname,
            text=NW_GenerateBlurOperator.bl_label,
            icon="EMPTY_ARROWS"
        )
        self.add_separator()

        #########################################

        self.add_label("Masks")
        self.add_split_row().template_icon_view(properties, "nodes_previews", show_labels=True)
        self.add_split_row().operator(
            NW_NodeImporter.bl_idname, 
            text="Add Mask", 
            icon="ADD"
        ).group = properties.nodes_previews
        self.add_separator()

        #########################################

        self.add_label("Materials")
        self.add_split_row().template_icon_view(properties, "materials_previews", show_labels=True)
        self.add_split_row().operator(
            NW_NodeImporter.bl_idname, 
            text="Add Material", 
            icon="ADD"
        ).group = properties.materials_previews
