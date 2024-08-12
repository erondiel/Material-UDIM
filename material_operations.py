import bpy
import os

class CountMaterialsOperator(bpy.types.Operator):
    """Count the number of materials on the active object"""
    bl_idname = "uv.count_materials"
    bl_label = "Count Materials"

    def execute(self, context):
        obj = bpy.context.active_object
        if obj and obj.type == 'MESH':
            materials = obj.data.materials
            material_count = len(materials)
            context.scene.material_count = material_count
            self.report({'INFO'}, f"Materials found: {material_count}")
        else:
            self.report({'WARNING'}, "No active mesh object selected")
        return {'FINISHED'}

class GenerateUDIMOperator(bpy.types.Operator):
    """Generate UDIM based on materials"""
    bl_idname = "uv.generate_udim"
    bl_label = "Generate UDIM"

    def execute(self, context):
        obj = bpy.context.active_object
        if not obj or obj.type != 'MESH':
            self.report({'WARNING'}, "No active mesh object selected")
            return {'CANCELLED'}

        materials = [mat.name for mat in obj.data.materials]

        if bpy.context.mode != 'EDIT_MESH':
            bpy.ops.object.mode_set(mode='EDIT')

        current_selection_mode = bpy.context.tool_settings.mesh_select_mode[:]
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
        bpy.ops.mesh.select_all(action='DESELECT')

        material_count = len(materials)
        if material_count <= 1:
            self.report({'WARNING'}, "Not enough materials found on the active object")
            return {'CANCELLED'}

        uv_layer = obj.data.uv_layers.active
        if uv_layer is None:
            self.report({'WARNING'}, "No UV map found on the active object")
            return {'CANCELLED'}

        for area in bpy.context.screen.areas:
            if area.type == 'IMAGE_EDITOR':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        override = bpy.context.copy()
                        override['area'] = area
                        override['region'] = region
                        override['space_data'] = area.spaces.active

                        for index in range(1, material_count):
                            obj.active_material_index = index
                            bpy.ops.object.material_slot_select()

                            udim_x_offset = index % 10
                            udim_y_offset = index // 10

                            with bpy.context.temp_override(**override):
                                bpy.ops.transform.translate(
                                    value=(udim_x_offset, udim_y_offset, 0),
                                    constraint_axis=(True, True, False),
                                    orient_type='LOCAL'
                                )

                            bpy.ops.mesh.select_all(action='DESELECT')
                        break

        bpy.context.tool_settings.mesh_select_mode = current_selection_mode

        self.report({'INFO'}, f"UVs moved to UDIM tiles for {material_count - 1} materials, excluding the first one.")
        return {'FINISHED'}
