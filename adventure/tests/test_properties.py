from program.classes.properties import *

def test_wear():
    ring = Wearable()

    assert ring.worn == False

    ring.wear()

    assert ring.worn == True

    ring.remove()

    assert ring.worn == False