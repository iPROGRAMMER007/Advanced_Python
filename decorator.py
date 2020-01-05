def chees_and_buns():
    def wrap():
        print("This is upper bread")
        chicken()
        print("This is lower bread")

    return wrap()

def chicken():
    print("I am roasted chicken")

chees_and_buns()

#chicken()