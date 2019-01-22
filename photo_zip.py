from PIL import Image, ImageSequence
import sys, os

if len(sys.argv) < 3:
    print("input invalid!")
    print("you need input ingif and outgif.")
    exit(1)

inf = sys.argv[1]
outf = sys.argv[2]

gif = Image.open('C:/usr/fans_medal/test/99999_30.gif')
dura = gif.info['duration']
imgs = [f.copy() for f in ImageSequence.Iterator(gif)]

index = 0
imglist = []
os.mkdir("C:/usr/fans_medal/testone")
for frame in imgs:
    frame.save("./C:/usr/fans_medal/testone/%d.png" % index)
    im = Image.open("./C:/usr/fans_medal/testone/%d.png" % index)
    im.thumbnail((88,31), Image.ANTIALIAS)
    imglist.append(im)
    index += 1

os.system("rm -rf ./C:/usr/fans_medal/testone")

imglist[0].save(outf, 'gif', save_all=True, append_images=imglist[1:], loop=0, duration=dura)
