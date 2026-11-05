[app]
title = TwinPing NOC
package.name = twinpingnoc
package.domain = org.twinping
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db,wav,mp3
version = 1.0.0
requirements = python3==3.10,kivy
orientation = landscape
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,WAKE_LOCK,VIBRATE,FOREGROUND_SERVICE,POST_NOTIFICATIONS
android.api = 33
android.minapi = 24
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
