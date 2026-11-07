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

# Branded launch background, generated from original shapes (no third-party assets).
splash=Image.new('RGB',(1080,1920),(22,56,67))
d=ImageDraw.Draw(splash)
d.ellipse((190,440,890,1140),fill=(249,199,72))
d.polygon([(0,1370),(220,1170),(350,1260),(550,1010),(730,1280),(890,1150),(1080,1370),(1080,1920),(0,1920)],fill=(48,111,111))
d.rectangle((0,1550,1080,1590),fill=(247,227,170))
d.ellipse((450,1490,630,1670),fill=(252,241,210))
drawable=root/'drawable'
drawable.mkdir(parents=True,exist_ok=True)
splash.save(drawable/'escape_splash.png')
# Capacitor Android's generated splash screen references drawable/splash.
splash.save(drawable/'splash.png')
print('Generated original splash artwork')
