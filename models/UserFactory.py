from models.constants import Shape
from models.User import User
from models.Pyada import Pyada


class UserFactory:
    def getUser(self, name: str, shape: Shape) -> User:
        p = Pyada(shape)
        return User(name, p)
