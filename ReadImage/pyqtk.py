import sys
from PyQt4.QtGui import QPixmap, QApplication, QCursor, QWidget
from PIL import Image
import time
from Xlib import display

app = QApplication(sys.argv)
disp = display.Display().screen()

for x in range(1, 10):
    screen = QApplication.desktop().screenGeometry()

    pixMap = QPixmap.grabWindow(QApplication.desktop().winId(), 0, 0, screen.width(), screen.height())

    print pixMap

    pixMap.save("test%d.bmp" % (x), 'bmp')

    data = disp.root.query_pointer()._data
    QCursor.setPos(x * 100, x * 100)

    im = Image.open('test1.bmp', 'r')
    pix_val = list(im.getdata())
