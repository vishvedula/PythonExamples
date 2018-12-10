def random_parallelogram(self, x1, y1, x2, y2, x3, y3, grains):

    pix = self.pix
    rectangle = self.ctx.rectangle
    fill = self.ctx.fill

    v1 = array((x2-x1, y2-y1))
    v2 = array((x3-x1, y3-y1))

    a1 = random((grains, 1))
    a2 = random((grains, 1))

    dd = v1*a1 + v2*a2

    dd[:, 0] += x1
    dd[:, 1] += y1

    for x, y in dd:
      rectangle(x, y, pix, pix)
      fill() 
