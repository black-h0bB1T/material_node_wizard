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

import bpy, os, bpy.utils.previews

class NW_CollectionList:
    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.mustScan = True
        self.collection = None
        self.items = []

    def blend(self):
        return os.path.join(self.path, self.name + ".blend")

    def previewFolder(self):
        return os.path.join(self.path, self.name)

class NW_PreviewHelper:
    collections = {}

    @staticmethod
    def addCollection(path, name):
        NW_PreviewHelper.collections[name] = NW_CollectionList(path, name)

    @staticmethod
    def scanCollection(list):
        list.mustScan = False

        if list.collection:
            bpy.utils.previews.remove(list.collection)
        list.collection = bpy.utils.previews.new()

        id = 0
        with bpy.data.libraries.load(list.blend(), link=False) as (data_src, data_dst):
            for group in data_src.node_groups:
                if group.startswith("NW_"):
                    preview = os.path.join(list.previewFolder(), group + ".jpg")
                    if os.path.exists(preview):
                        thumb = list.collection.load(group, preview, 'IMAGE')
                    else:
                        thumb = list.collection.load(group, os.path.join(os.path.dirname(__file__), "NW_No_Icon.jpg"), 'IMAGE')
                    list.items.append((
                        "%s::%s" % (list.blend(), group), 
                        group,
                        "", 
                        thumb.icon_id, 
                        id
                    ))
                    id += 1

    @staticmethod
    def getCollection(name):
        list = NW_PreviewHelper.collections[name]
        if list.mustScan:
            NW_PreviewHelper.scanCollection(list)
        return list

    @staticmethod
    def removeAllCollections():
        for list in NW_PreviewHelper.collections.values():
            list.items.clear()
            if list.collection:
                bpy.utils.previews.remove(list.collection)
        NW_PreviewHelper.collections.clear()
