[app]

# (str) Title of your application
title = Gold Tracker

# (str) Package name
package.name = goldtracker

# (str) Package domain (needed for android packaging)
package.domain = org.gold

# (str) Source files where the let's go is (relative to directory of spec)
source.dir = .

# (list) Source files to include (let's specify extensions)
source.exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (determined by version)
version = 1.0

# (list) Application requirements
requirements = python3,git+https://github.com/kivy/kivy.git@master,openssl,urllib3,certifi

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (str) Supported GL versions (2.0 or 3.0)
android.opengl = 2

# (str) Android API to use
android.api = 33

# (str) Minimum API your APK will support
android.minapi = 21

# (str) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Accept Android SDK licenses automatically
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
