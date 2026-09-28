from init import *

class Game:
    def __init__(self):
        self.running = True

    def run_main(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

        screen.fill(black)
        pg.display.flip()
        pg.quit()