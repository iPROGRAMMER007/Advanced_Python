def chees_and_buns(orignal_func):
    def wrap():
        print("This is upper bread")
        orignal_func()
        print("This is lower bread")

    return wrap

@chees_and_buns
def chicken():
    print("I am roasted chicken")

chicken()