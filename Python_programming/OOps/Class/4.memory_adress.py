class nsr_class:
    a = "Welcome to NSR"
    print(a)

class msr_class:
    b = "Welcome to MSR"
    print(b)

obj_bng = nsr_class()
obj_che = msr_class

obj_class_msr = nsr_class()

print(id(obj_bng)," : is the Memory address of obj obj_bng ")

print(id(obj_che), " : is the Memory address of obj obj_che " )

print(id(obj_class_msr))
