[app]
title = TTS Maker
package.name = ttsmaker
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,pyjnius==1.6.1
orientation = portrait
icon = None
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.ndk = 25b
android.build_tools = 33.0.2
android.minapi = 21
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1