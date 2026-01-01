from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Any

class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers
    and a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    _next_handler: Optional[Handler] = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}.\n"
        else:
            return super().handle(request)
    
class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}.\n"
        else:
            return super().handle(request)
        
class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}.\n"
        else:
            return super().handle(request)
        
def client_code(handler: Handler) -> None:
    requests = ["Nut", "Banana", "Cup of coffee"]
    
    for request in requests:
        print(f"Client: Who wants a {request}?")
        result = handler.handle(request)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {request} was left untouched.")

if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    print("Chain: Monkey > Squirrel > Dog\n")
    client_code(monkey)

    print("Subchain: Squirrel > Dog\n")
    client_code(squirrel)