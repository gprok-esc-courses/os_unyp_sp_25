
def test(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)



test(5, brand="VW", model="Polo", cc=1200)