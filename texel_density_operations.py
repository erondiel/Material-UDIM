import bpy
import time

class AdjustTexelDensityOperator(bpy.types.Operator):
    """Adjust Texel Density using the Texel Density Checker add-on"""
    bl_idname = "uv.adjust_texel_density"
    bl_label = "Adjust Texel Density"

    def execute(self, context):
        addon_name = "Texel_Density_2023_2_Bl400"

        if addon_name in bpy.context.preferences.addons:
            texel_density_value = context.scene.texel_density_value
            context.scene.td.density_set = str(texel_density_value)

            # Call the Texel Density Set operator
            bpy.ops.object.texel_density_set()
            self.report({'INFO'}, "Texel Density has been adjusted.")
        else:
            self.report({'ERROR'}, f"The '{addon_name}' add-on is not installed or enabled.")
            return {'CANCELLED'}

        return {'FINISHED'}


class ApplyTexelDensityOperator(bpy.types.Operator):
    """Apply Texel Density to each material in the list"""
    bl_idname = "uv.apply_texel_density"
    bl_label = "Apply Texel Density"

    def execute(self, context):
        addon_name = "Texel_Density_2023_2_Bl400"

        if addon_name in bpy.context.preferences.addons:
            bpy.context.scene.td.set_method = '1'
            bpy.context.scene.td.rescale_anchor = 'SELECTION'

            texel_density_value = context.scene.texel_density_value
            context.scene.td.density_set = str(texel_density_value)

            obj = context.active_object
            if obj and obj.type == 'MESH':
                materials = obj.data.materials
                for index, material in enumerate(materials):
                    # Report the status to the Info window
                    status_message = f"Scaling material {index + 1}/{len(materials)}: {material.name}"
                    self.report({'INFO'}, status_message)

                    time.sleep(0.1)  # Small pause to simulate processing time

                    obj.active_material_index = index
                    bpy.ops.object.material_slot_select()
                    bpy.ops.object.texel_density_set()

                    bpy.ops.mesh.select_all(action='DESELECT')

                # Final status message
                self.report({'INFO'}, "Texel Density application complete.")
            else:
                self.report({'WARNING'}, "No active mesh object selected")
                return {'CANCELLED'}
        else:
            self.report({'ERROR'}, f"The '{addon_name}' add-on is not installed or enabled.")
            return {'CANCELLED'}

        return {'FINISHED'}
