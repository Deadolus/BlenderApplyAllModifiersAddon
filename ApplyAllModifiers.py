bl_info = {
    "name": "Apply all modifiers of selected objects",
    "category": "Object",
    "author": "Deadolus",
    "version": (1,0,0),
    "blender": (2,80,0),
    "warning": "",
    "location": "Object > Apply > Apply all modifiers of selected objects",
}

import bpy


def main(context):
    #for ob in context.scene.objects:
        #print(ob)
    #bpy.ops.object.select_all(action='DESELECT')
    #bpy.ops.object.select_all(action='SELECT')
    act = context.active_object
    old_active = act
    sel = context.selected_objects

    for obj in sel:
        bpy.context.view_layer.objects.active = obj
        for mod in obj.modifiers:
            bpy.ops.object.modifier_apply(modifier=mod.name)
        
    context.view_layer.objects.active = old_active



class ApplyAllModifiersOperator(bpy.types.Operator):
    """Apply all modifiers of selected objects"""
    bl_idname = "object.apply_all_modifiers"
    bl_label = "Apply all modifiers of selected objects"
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator("object.apply_all_modifiers")
    # bl_idname should be in form of "something.something"
    # or YourClass.bl_idname
    
def register():
    bpy.utils.register_class(ApplyAllModifiersOperator)
    bpy.types.VIEW3D_MT_object_apply.append(menu_func)


def unregister():
    bpy.utils.unregister_class(ApplyAllModifiersOperator)
    bpy.types.VIEW3D_MT_object_apply.remove(menu_func)


if __name__ == "__main__":
    register()

