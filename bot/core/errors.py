class EnvironmentVariableIsRequired(Exception):
    """
    Вызывается, если в переменная окружения не найдена
    """

    def __init__(self, name: str):
        self.name = name
        super().__init__(f"Обязательная переменная окружения {name} не найдена")


__all__ = ("EnvironmentVariableIsRequired",)
