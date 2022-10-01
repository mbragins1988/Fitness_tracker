class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(
        self,
        training_type: str,
        duration: float,
        distance: float,
        speed: float,
        calories: float
    ) -> None:

        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (
            f'Тип тренировки: {self.training_type}; '
            f'Длительность: {self.duration:0.3f} ч.; '
            f'Дистанция: {self.distance:0.3f} км; '
            f'Ср. скорость: {self.speed:0.3f} км/ч; '
            f'Потрачено ккал: {self.calories:0.3f}.'
        )


class Training:
    """Базовый класс тренировки."""
    M_IN_KM: int = 1000  # Константа значенийм из метров в километры
    LEN_STEP: float = 0.65  # Расстояние за один шаг в метрах
    MIN_IN_HOUR: float = 60  # Количество минут в часе

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:

        self.action = action  # Количество совершённых действий
        self.duration = duration  # Длительность тренировки
        self.weight = weight  # Вес спортсмена

    def get_distance(self) -> float:  # Дистанция (в километрах)
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:  # Средняя скорость движения
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:  # Потраченные калории за тренировку
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(type(self).__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    coeff_calorie_1 = 18
    coeff_calorie_2 = 20

    def get_spent_calories(self) -> float:  # Метод расчета калорий для бега
        """Получить количество затраченных калорий."""
        return ((self.coeff_calorie_1 * self.get_mean_speed()
                 - self.coeff_calorie_2)
                * self.weight / self.M_IN_KM * self.duration
                * self.MIN_IN_HOUR)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    coeff_calorie_3 = 0.035
    coeff_calorie_4 = 0.029

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float,
        height: float
    ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.coeff_calorie_3 * self.weight
                + (self.get_mean_speed()**2 // self.height)
                * self.coeff_calorie_4 * self.weight)
                * self.duration * self.MIN_IN_HOUR)


class Swimming(Training):
    """Тренировка: плавание."""

    coeff_calorie_5 = 1.1
    coeff_calorie_6 = 2

    LEN_STEP: float = 1.38  # Расстояние за один гребок в метрах

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float,
        length_pool: float,  # Длина бассейна в метрах
        count_pool: int  # Сколько раз пользователь переплыл бассейн
    ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.get_mean_speed() + self.coeff_calorie_5)
                * self.coeff_calorie_6 * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    dict = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    return dict[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
