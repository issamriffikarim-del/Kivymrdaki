[app]
title = FortuneoDaki
package.name = fortuneodaki
package.domain = org.issam
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,otf,json,txt
version = 0.1

requirements = python3,kivy,kivymd,requests

[buildozer]
log_level = 2

[android]
android.permissions = INTERNET
android.api = 34
android.minapi = 21
