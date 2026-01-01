from threading import Lock, Thread

class SingletonMeta(type):
    """
    A metaclass for Singleton pattern implementation.
    Ensures that only one instance of a class is created.
    """
    _instances = {}

    _lock: Lock = Lock()


    def __call__(cls, *args, **kwargs):
        with cls._lock:        
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
        
class Singleton(metaclass=SingletonMeta):
    """
    A Singleton class example.
    Any class that wants to be a singleton can inherit from this class.
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        """
        Example business logic method.
        """
        pass


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(f"Singleton value: {singleton.value}")


if __name__ == "__main__":
    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")
    thread1 = Thread(target=test_singleton, args=("FOO",))
    thread2 = Thread(target=test_singleton, args=("BAR",))

    thread1.start()
    thread2.start()

