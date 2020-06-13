import eel
print("hello")


@eel.expose
def hellopy(name):
    print("hello from python",name)


eel.init('web')
eel.start('index.html',size=(900,600))
