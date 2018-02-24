#  560, 150:   0,   0
#  556, 365:   0, 200
#  254, 148: 300,   0

class Calibration:
  def transform(self, x, y):
    x1 = 558.
    y1 = 0.
    x2 = 254.
    y2 = 300.

    mx = (y2 - y1) / (x2 - x1)
    bx = y1 - mx * x1

    xn = int(mx*x + bx)

    x1 = 149.
    y1 = 0.
    x2 = 365.
    y2 = 200.

    my = (y2 - y1) / (x2 - x1)
    by = y1 - my * x1

    yn = int(my*y + by)

    return [xn, yn]

