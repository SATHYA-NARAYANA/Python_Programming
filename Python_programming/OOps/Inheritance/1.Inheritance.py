class parent():

    def parent_method(self):
        print("I am belonging to Parent Class")

class child_class(parent):
    def child_method(self):
        print("I am belonging to Child method")

obj_child_class = child_class()

obj_child_class.child_method()
obj_child_class.parent_method()
