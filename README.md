#  Модуль фитнес-трекер.

Обрабатывает данные для трёх видов тренировок: бега, спортивной ходьбы и плавания.
- принимать от блока датчиков информацию о прошедшей тренировке,
- определять вид тренировки,
рассчитывать результаты тренировки,
выводить информационное сообщение о результатах тренировки.

Информационное сообщение должно включать такие данные:
тип тренировки (бег, ходьба или плавание);
длительность тренировки;
дистанция, которую преодолел пользователь, в километрах;
среднюю скорость на дистанции, в км/ч;
расход энергии, в килокалориях.

## Технологии:
- Python 3.7

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/pozdnysheva/Fitness-tracker-module.git
```

```
cd hw_python_oop
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить проект:

```
python homework.py
```
