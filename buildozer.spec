[app]
title = FortuneoDaki
package.name = fortuneodaki
package.domain = org.issam
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,otf,json,txt
version = 0.1

requirements = python3,kivy,kivymd,requests

# (optional) if you use icons:
# icon.filename = assets/icon.png

[buildozer]
log_level = 2

[android]
# common stable defaults:
android.permissions = INTERNET
android.api = 33
android.minapi = 21
