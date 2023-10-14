def mydecarator(f1):
    def inside_function():
        print("good bye")
        f1()
    return inside_function()
@mydecarator
def sayhello():
    print("hi.................!")


