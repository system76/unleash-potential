#!/usr/bin/python3

from asciimatics.effects import Cycle, Stars, Print
from asciimatics.renderers import FigletText, ColourImageFile, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import webbrowser
import sys, os

def demo(screen):
    path = os.path.abspath(__file__)
    assetpath = os.path.dirname(path)
    scenes = []
    #Apt-get install...
    effects = [
        Cycle(screen,
            FigletText("apt-get install", font='big'),
            int(screen.height // 2 - 8)),
    ]
    scenes.append(Scene(effects, 60))

    #Docker
    effects = [
        Cycle(screen,
            ColourImageFile(screen, assetpath + "/assets/docker-logo.png", 16, 0, False),
            int(screen.height // 2 - 12)),
        Cycle(screen,
            FigletText("DOCKER", font='big'),
            int(screen.height // 2 + 3))
    ]
    scenes.append(Scene(effects, 60))

    effects = [
        Cycle(screen,
            ColourImageFile(screen, assetpath + "/assets/nodejs-logo.png", 16, 0, False),
            int(screen.height // 2 - 14)),
        Cycle(screen,
            FigletText("NODE.JS", font='big'),
            int(screen.height // 2 + 3))
    ]
    scenes.append(Scene(effects, 60))

    effects = [
        Cycle(screen,
            ColourImageFile(screen, assetpath + "/assets/git_logo.png", 16, 0, False),
            int(screen.height // 2 - 14)),
        Cycle(screen,
            FigletText("GIT", font='big'),
            int(screen.height // 2 + 3))
    ]
    scenes.append(Scene(effects, 60))

    # system76
    effects = [
        Cycle(screen,
            ColourImageFile(screen, assetpath + "/assets/system76_logo_white.png", 16, 0, False),
            int(screen.height // 2 - 14)),
        Cycle(screen,
            FigletText("Laptops for Developers", font='big'),
            int(screen.height // 2 + 3)),
        Stars(screen, (screen.width + screen.height) // 2),
        Print(screen,
            SpeechBubble("Press \"X\" to learn more!"),
            screen.height - 3,
            speed=1,
            transparent=False,
            start_frame=20)
    ]
    scenes.append(Scene(effects))
    screen.play(scenes, stop_on_resize=True)

if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo)
            webbrowser.open('https://system76.com/laptops')
            sys.exit(0)
        except ResizeScreenError:
            pass
