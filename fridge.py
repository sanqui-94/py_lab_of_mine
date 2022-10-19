"""Demonstrate raiding a refrigerator,"""

from contextlib import closing

class RefrigeratorRaider:
    """Raid a refrigerator"""

    def open(self):
        print("Open the fridge door.")

    def take(self, food):
        print("Finding {}".format(food))
        if food == 'apples':
            raise RuntimeError("Health warning!")
        print("Taking {}".format(food))

    def close(self):
        print("Close fridge door.")


def raid(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)

