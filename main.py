from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.canvas = Canvas()
        self.canvas.pack()
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while (self.is_running):
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, color):
        line.draw(self.canvas, color)

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, color):
        canvas.create_line(
            self.point_1.x, 
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            fill=color,
            width=2
        )
        canvas.pack()

class Cell():
    def __init__(self, point_1, point_2, window):
        self.has_left_wall = False
        self.has_right_wall = False
        self.has_top_wall = False
        self.has_bottom_wall = False
        self._x1 = point_1.x
        self._y1 = point_1.y
        self._x2 = point_2.x
        self._y2 = point_2.y
        self._window = window

def main():
    window = Window(799, 600)
    
    point_1 = Point()
    point_2 = Point(100, 100)
    line = Line(point_1, point_2)
    window.draw_line(line, 'red')
    window.wait_for_close()

   
main()
