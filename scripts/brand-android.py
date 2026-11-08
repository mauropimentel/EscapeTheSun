"""Create consistent Android launcher icons from simple original vector-like artwork."""
from pathlib import Path
from PIL import Image, ImageDraw

root=Path('android/app/src/main/res')
for name,size in [('mdpi',48),('hdpi',72),('xhdpi',96),('xxhdpi',144),('xxxhdpi',192)]:
    n=size*4
    im=Image.new('RGBA',(n,n),(22,56,67,255))
    d=ImageDraw.Draw(im)
    # Original playful icon: Burj Al Arab's sail with a tiny tourist hiding in its shade.
    d.ellipse((n*.57,n*.07,n*.94,n*.44),fill=(255,209,93,255))
    d.ellipse((n*.11,n*.68,n*.89,n*.97),fill=(235,180,105,255))
    d.polygon([(n*.21,n*.78),(n*.44,n*.20),(n*.49,n*.10),(n*.52,n*.77)],fill=(246,241,217,255))
    d.polygon([(n*.48,n*.22),(n*.75,n*.73),(n*.53,n*.73)],fill=(147,214,226,255))
    d.line([(n*.49,n*.13),(n*.49,n*.81)],fill=(26,61,80,255),width=max(2,int(n*.024)))
    for y in (.36,.48,.60):
        d.line([(n*.47,n*y),(n*(.54+(y-.30)*.29),n*y)],fill=(30,85,111,255),width=max(2,int(n*.012)))
    d.ellipse((n*.21,n*.71,n*.33,n*.83),fill=(255,221,172,255))
    d.arc((n*.22,n*.74,n*.31,n*.81),0,180,fill=(26,57,69,255),width=max(2,int(n*.015)))
    d.pieslice((n*.19,n*.68,n*.35,n*.75),180,360,fill=(247,190,72,255))
    d.rectangle((n*.19,n*.75,n*.35,n*.78),fill=(245,194,68,255))
    d.ellipse((n*.20,n*.78,n*.35,n*.90),fill=(42,79,91,255))
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

# Apply splash to the actual Capacitor launch theme, not to the regular app theme.
# Android 12+ uses a centered launcher icon and a brand-colored background.
import re
values=root/'values'
styles=values/'styles.xml'
if styles.exists():
    data=styles.read_text()
    pattern=r'(<style[^>]*name="AppTheme.NoActionBarLaunch"[^>]*>)([\s\S]*?)(</style>)'
    def patch(match):
        body=match.group(2)
        body=re.sub(r'<item name="android:windowBackground">.*?</item>','',body)
        body=re.sub(r'<item name="android:windowSplashScreenBackground">.*?</item>','',body)
        body=re.sub(r'<item name="android:windowSplashScreenAnimatedIcon">.*?</item>','',body)
        body+='\n<item name="android:windowBackground">@drawable/splash</item>\n'
        body+='<item name="android:windowSplashScreenBackground">#163843</item>\n'
        body+='<item name="android:windowSplashScreenAnimatedIcon">@mipmap/ic_launcher</item>\n'
        return match.group(1)+body+match.group(3)
    updated,count=re.subn(pattern,patch,data)
    if count!=1:
        raise RuntimeError('Expected Capacitor Android launch theme not found')
    styles.write_text(updated)
print('Configured Android launch theme')
