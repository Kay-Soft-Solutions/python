[app]

# (str) Title of your application
title = Assessment

# (str) Package name
package.name = app2

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (str) Source files to include (comma separated values)
source.include_exts = py,png,xlsx

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = kivy, openpyxl

# (str) Application main file (this is the launcher script)
main.py = main.py

# (list) Icon of the application (comma separated values)
icon.filename = %(source.dir)s/icon.png

# (list) Presplash of the application (comma separated values)
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
#android.permissions = INTERNET

# (list) Features (adds permissions, like CAMERA, to manifest)
#android.features = android.hardware.camera

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy libraries to lib/armeabi. Default is False
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#android.arch = armeabi-v7a

# (str) Android entry point
#android.entrypoint = org.renpy.android.PythonActivity

# (str) Android app theme, default will be a dark theme
#android.theme = default

# (bool) Android key.store option (default False)
#android.key_store = myapp.keystore

# (str) Android key.alias option (default myalias)
#android.key_alias = myalias

# (str) Android key.store.password option (default mypassword)
#android.key_store.password = mypassword

# (str) Android key.alias.password option (default mypassword)
#android.key_alias.password = mypassword

# (bool) Android uses permission that requires accepting a privacy policy (used for sdk>=30), default is False
#android.require_privacy_policy = False

# (str) iOS bundle identifier (com.example.myapp)
#ios.bundle_identifier = org.test

# (str) iOS app launch images
#ios.launch_image = %(source.dir)s/data/launch.png

# (list) iOS frameworks to link against
#ios.frameworks =

# (str) iOS icons (plist/json)
#ios.icons = %(source.dir)s/data/icon.png

# (str) iOS app launch images (plist/json)
#ios.launch_images = %(source.dir)s/data/launch.png

# (list) iOS extra plist items
#ios.plist_extras =

# (list) iOS launch arguments
#ios.launch_args =

# (bool) Use the launch storyboard instead of the static launch images (iOS 9.0+, Xcode 7.0+)
#ios.use_launch_storyboard = True

# (str) iOS app build needs a entitlements file
# ios.entitlements = %(source.dir)s/MyApp/entitlements.plist

# (str) Custom Xcode configuration plist (plist)
#ios.config = %(source.dir)s/MyApp/config.plist

# (str) Custom Xcode post build script
#ios.postbuild = %(source.dir)s/MyApp/postbuild.sh

# (list) iOS app framework dirs (space separated values) to be copied to the app Frameworks folder (iOS only)
#ios.framework_dirs = %(source.dir)s/MyApp/MyFramework %(source.dir)s/AnotherFramework

# (list) iOS app frameworks (space separated values) to be linked with the app (iOS only)
#ios.frameworks = MyFramework.framework AnotherFramework.framework

# (list) Android add-ons
#android.add_javaclasses = mysource/JavaClassesFolder
#android.add_res = mysource/ResFolder

# (str) Android manifest directives
# http://developer.android.com/guide/topics/manifest/manifest-intro.html
#android.manifest.directives = <activity android:configChanges="orientation|keyboardHidden" android:screenOrientation="portrait">
