"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) —
2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

from time import sleep
from itertools import cycle


class TrafficLight:
    __color = {"Красный": 7, "Желтый": 2, "Зеленый": 7, "Конец": 2}

    def running(self):
        for light, time in cycle(self.__color.items()):
            print(f'Сейчас горит {light} сигнал')
            if light == "Конец":
                print(f"Сейчас горит Желтый сигнал")
            sleep(time)


trafficlight = TrafficLight()
trafficlight.running()
