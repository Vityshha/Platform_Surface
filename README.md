# Platform_Surface
Приложение для управления гусеничной платформы. 
Реализовано: 
1) Движение с помощью геймпада Xbox360
2) Движение с помощью джойстика
3) Движение по заданной траектории 
4) Движение за человеком
5) Движение за меткой
6) Движение по сценарием (квадрат, часы)

Приложение написано с помощью PyQt5 и python3.8. Сервер
находится в репозитории [Platform](https://github.com/Vityshha/Platform).
Связь с платформой реализована через UDP (движение по джойстику), а связь с сервером через TCP. Распознавание происходит на сервере с помощью yolo8x, обработка сценариев также на сервере. 


В файле Network\sockets\NetworkConstants.py находится флаг для запуска либо локально,
либо с подключением к серверу. Все сетевые константы находятся там (ip, port, rtsp link).


<hr>

## Запуск проекта:

1) `python -m venv venv `
2) `.\venv\Scripts\activate`
3) `pip install -r .\requirements.txt`

<hr>

## Как собрать exe:

1) `pip install auto-py-to-exe`
2) `auto-py-to-exe`

<hr>

## GUI

![ris1.png](image%2Fris1.png)
![ris2.png](image%2Fris2.png)
![ris3.png](image%2Fris3.png)
