import bpy
from .ui import MaterialUDIMPanel
from .material_operations import CountMaterialsOperator, GenerateUDIMOperator
from .texel_density_operations import AdjustTexelDensityOperator, ApplyTexelDensityOperator

bl_info = {
    "name": "Material UDIM",
    "blender": (4, 2, 0),
    "category": "UV",
    "author": "Rodrigo Camacho",
    "description": "A tool to move faces based on materials to different UDIMs.",
}

def update_texel_density(self, context):
    td = context.scene.td
    texel_density_value = context.scene.texel_density_value

    bpy.ops.uv.select_all(action='DESELECT')
    td.density_set = str(texel_density_value)
    bpy.ops.object.texel_density_set()

def register():
    bpy.utils.register_class(MaterialUDIMPanel)
    bpy.utils.register_class(CountMaterialsOperator)
    bpy.utils.register_class(GenerateUDIMOperator)
    bpy.utils.register_class(AdjustTexelDensityOperator)
    bpy.utils.register_class(ApplyTexelDensityOperator)

    bpy.types.Scene.material_count = bpy.props.IntProperty(name="Material Count", default=0)
    bpy.types.Scene.texel_density_value = bpy.props.FloatProperty(
        name="Texel Density Value",
        default=1.0,
        update=update_texel_density
    )
    bpy.types.Scene.texel_density_status = bpy.props.StringProperty(
        name="Texel Density Status",
        default="Ready"
    )

def unregister():
    bpy.utils.unregister_class(MaterialUDIMPanel)
    bpy.utils.unregister_class(CountMaterialsOperator)
    bpy.utils.unregister_class(GenerateUDIMOperator)
    bpy.utils.unregister_class(AdjustTexelDensityOperator)
    bpy.utils.unregister_class(ApplyTexelDensityOperator)

    del bpy.types.Scene.material_count
    del bpy.types.Scene.texel_density_value
    del bpy.types.Scene.texel_density_status

if __name__ == "__main__":
    register()
