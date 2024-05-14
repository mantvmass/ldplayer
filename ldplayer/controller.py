from ppadb.device import Device


class Controller:
    """
    The controller class for interacting with the LDPlayer emulator works using ppadb(https://github.com/Swind/pure-python-adb).
    """
    
    
    __device = None
    
    
    def __init__(self, device: Device) -> None:
        self.__device = device
    
    
    def tap(self, x: int, y: int):
        """
        Simulates a tap action at the specified coordinates.

        :param x: The x-coordinate of the tap action.
        :param y: The y-coordinate of the tap action.
        :return: None
        """
        return self.__device.shell("input tap {} {}".format(x, y))

    
    def swipe(self, sx: int, sy: int, ex: int, ey: int, duration: int):
        """
        Simulates a swipe action at the specified coordinates.

        :param sx: The starting x-coordinate of the swipe action.
        :param sy: The starting y-coordinate of the swipe action.
        :param ex: The ending x-coordinate of the swipe action.
        :param ey: The ending y-coordinate of the swipe action.
        :param duration: The duration (in milliseconds) of the swipe action.
        :return: None
        """
        return self.__device.shell("input swipe {} {} {} {} {}".format(sx, sy, ex, ey, duration))
