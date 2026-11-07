"""Create consistent Android launcher icons from simple original vector-like artwork."""
from pathlib import Path
from PIL import Image, ImageDraw

root=Path('android/app/src/main/res')
for name,size in [('mdpi',48),('hdpi',72),('xhdpi',96),('xxhdpi',144),('xxxhdpi',192)]:
    n=size*4
    im=Image.new('RGBA',(n,n),(22,56,67,255))
    d=ImageDraw.Draw(im)
    d.ellipse((n*.19,n*.10,n*.81,n*.72),fill=(249,199,72,255))
    d.polygon([(0,n*.74),(n*.22,n*.60),(n*.31,n*.68),(n*.50,n*.46),(n*.65,n*.68),(n*.82,n*.55),(n,n*.75),(n,n),(0,n)],fill=(48,111,111,255))
    d.rectangle((n*.14,n*.73,n*.86,n*.79),fill=(247,227,170,255))
    d.ellipse((n*.41,n*.70,n*.59,n*.88),fill=(252,241,210,255))
    im=im.resize((size,size),Image.Resampling.LANCZOS)
    folder=root/f'mipmap-{name}'
    folder.mkdir(parents=True,exist_ok=True)
    for filename in ('ic_launcher.png','ic_launcher_round.png','ic_launcher_foreground.png'):
        im.save(folder/filename)
print('Generated original Escape the Sun Android launcher icons')
