from pathlib import Path
import os



BASE_PATH = Path(__file__).resolve().parent

# game width and heigh
WIDTH = 1000
HEIGHT = 600


# background color
bg_color = (255,255,255)

#back ground image
bg_image =os.path.join(BASE_PATH /"img/backgroundstart001.png")