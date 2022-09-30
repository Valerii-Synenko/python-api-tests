from src.models.user_model import UserModelFactory


class Models:
    def user_model(self, **kwargs):
        return UserModelFactory.build(**kwargs)
