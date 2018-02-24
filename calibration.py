#  560, 150:   0,   0
#  556, 365:   0, 200
#  254, 148: 300,   0

class Calibration:
  def transform(self, x, y):
    x1 = 218.
    y1 = 365.
    x2 = 346.
    y2 = 194.

    mx = (y2 - y1) / (x2 - x1)
    bx = y1 - mx * x1

    xn = int(mx*x + bx)

    x1 = 156.
    y1 = -26.
    x2 = 292.
    y2 = 147.

    my = (y2 - y1) / (x2 - x1)
    by = y1 - my * x1

    yn = int(my*y + by)

    return [xn, yn]

