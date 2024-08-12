import bpy

class MaterialUDIMPanel(bpy.types.Panel):
    """Creates a Panel in the UV/Image Editor properties window"""
    bl_label = "Material UDIM"
    bl_idname = "UV_PT_material_udim"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Material UDIM'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.operator("uv.count_materials", text="Count Materials")
        layout.label(text="Materials Found: " + str(scene.material_count))
        layout.operator("uv.generate_udim", text="Generate UDIM")

        # Texel Density value input field
        layout.prop(scene, "texel_density_value", text="Texel Density")

        # Button to apply texel density
        layout.operator("uv.apply_texel_density", text="Apply Texel Density")

        # Status message (now this can be removed if only using console output)
        layout.label(text="Status: " + scene.texel_density_status)
