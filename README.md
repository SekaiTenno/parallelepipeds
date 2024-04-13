# parallelepipeds

'''



Parallelepiped task

В данном проекте вы напишите программу для вычисления некоторых величин, которые характеризуют такую геометрическую фигуру как параллелепипед. Это хороший кейс для обучения написанию скриптов.

Параллелепипед - это объемная фигура, каждой гранью которой является прямоугольником.

Если задан параллелепипед 
, то:

, 
 ... - грани параллелепипеда
 .. - ребра параллелепипеда.
 - главная диагональ параллелепипеда.
From JSON

Вам предоставлен json файл parallelepipeds.json, который можете скачать ТУТ

Его структура:

{
    "figure_1": {
        "a": "2",
        "b": "1",
        "c": "6"
    },
    "figure_2": {
        "a": "16",
        "b": "10",
        "c": "14"
    },
    "figure_3": {
        "a": "19",
        "b": "9",
        "c": "19"
    },
    ....,
}
Тут хранятся данные по 100 разным параллелепипедам, грани (длина, ширина и высота) , ,  каждого из которых находятся в словарях по ключам figure_ ... глобального словаря.

Техническое задание для написания скрипта.

Напишите скрипт my_first_script.py, который можно запускать локально, который:

Прочитает исходный parallelepipeds.json
Сохранит в директорию два новых JSON файла
"ЗАПРИНТИТ" сообщение о количестве фигур в файле в виде сообщения "Total number of figures <...count...>."
В конце запринтит красиво полученные усредненные значения о которых пойдет речь далее.
Также в начале скрипта для пущей красоты можно запринтить строчку которая написана ниже:


pict = """
MY FIRST SKRIPT

    /------/
   /      /|
  /      / |
 /------/  |
 |      |  /
 |      | /
 |______|/

I LOVE PYTHON
"""
print(pict)
     
MY FIRST SKRIPT

    /------/ 
   /      /|
  /      / |
 /------/  |
 |      |  /
 |      | / 
 |______|/

I LOVE PYTHON

characteristics.json

Так должен называться первый файл, который сохранит в директорию ваш скрипт. Он имеет примерно ту же структуру, что и входной JSON файл и имеет вид:

{
    "figure_1": {
        "diag": <your value, type=str>,
        "volume": <your value, type=str>,
        "surface_area": <your value, type=str>,
        "alpha": <your value, type=str>,
        "beta": <your value, type=str>,
        "gamma": <your value, type=str>
        "radius_described_sphere": <your value, type=str>,
        "volume_described_sphere": <your value, type=str>
    },
    "figure_2": {
        "diag": <your value, type=str>,
        "volume": <your value, type=str>,
        "surface_area": <your value, type=str>,
        "alpha": <your value, type=str>,
        "beta": <your value, type=str>,
        "gamma": <your value, type=str>
        "radius_described_sphere": <your value, type=str>,
        "volume_described_sphere": <your value, type=str>
    },
    "figure_3": {
        "diag": <your value, type=str>,
        "volume": <your value, type=str>,
        "surface_area": <your value, type=str>,
        "alpha": <your value, type=str>,
        "beta": <your value, type=str>,
        "gamma": <your value, type=str>
        "radius_described_sphere": <your value, type=str>,
        "volume_described_sphere": <your value, type=str>
    },
    .....
}
В этом словаре для каждого параллелограма расчитываются:

diag - Главная диагональ
volume - объем параллелограмма
surface_area - площадь поверхности параллелограма
alpha - угол между диагональю и стороной  в градусах!!!
beta - угол между диагональю и стороной  в градусах!!!
gamma - угол между диагональю и стороной  в градусах!!!
radius_described_sphere - радиус описаной сферы (равен половине гл. диагонали)
volume_described_sphere - объем описаной сферы.
В этом же порядке привожу формулы для вычисления:




 
 Где  - диагональ

 

 

 
 Где  - диагональ

 

Обратите внимание, что в полученном словаре расчитанные значения должны иметь СТРОКОВЫЙ формат!!! В противном случае у вас возникнут проблемы с созданием JSON из данного словаря.

statistics.json
Так должен называться второй файл, который сохранит в директорию ваш скрипт. В нем должны храниться по каждой расчитанной величине СРЕДНИЕ значения для всех параллелограмов. Вот его структура:

{
        "avg_diag": <your value, type=str>,
        "avg_volume": <your value, type=str>,
        "avg_surface_area": <your value, type=str>,
        "avg_alpha": <your value, type=str>,
        "avg_beta": <your value, type=str>,
        "avg_gamma": <your value, type=str>
        "avg_radius_described_sphere": <your value, type=str>,
        "avg_volume_described_sphere": <your value, type=str>
}
avg_diag - Среднее всех главных диагоналей
avg_volume - Средний объем параллелограммов
avg_surface_area - Средняя площадь поверхностей параллелограмов
........
Также БУДЕТ ПОЛЕЗНЫМ каждое это усредненное значени ЗАПРИНТИТЬ чтобы это красиво было отображено в терминале при запуске скрипта!)

Директория
Если вы разворачивайте проект на ПК локально, то в папке пользователя  C:\Users\USER> создайте папку проекта PAR_proj.

Это можно сделать через проводник или через терминал выполнив 2 команды:

mkdir PAR_proj   # создание папки
cd PAR_proj      # переход к этой папке
Папка должна в себе содержать два файла - скрипта и исходного JSON.

PAR_proj
--- parallelepipeds.json
--- my_first_script.py

Запустите скрипт через терминал:

python my_first_script.py
иногда нужно написать так:

python3 my_first_script.py
После запуска скрипта в этой папке буду сохранены сгенеренные JSON файлы.

Colab
Если вы хотите запустить скрипт в Colab, то поместите файлы в директорию колаба:

image.png

Запустите скрипт написав в ячейке колаба:

!python my_first_script.py

'''
