[app]
# Application title and name
title = Medical LLM Tutor
package.name = medicallmtutor
package.domain = org.unn

# Version
version = 1.0
versioning = PVN

# Requirements
requirements = python3,kivy,pillow,requests

# Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Features
android.features = android.hardware.screen.portrait

# Orientation
orientation = portrait

# Source
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt,md

# Build directory
buildozer.log_level = 2
buildozer.warn_on_root = 1

# Java compilation
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Architecture
android.archs = arm64-v8a,armeabi-v7a

# Icon and presplash
#icon.filename = %(source.dir)s/data/icon.png
#presplash.filename = %(source.dir)s/data/presplash.png

# App behavior
fullscreen = False
android.fullscreen = False

# Bootstrap
p4a.bootstrap = sdl2

# Gradle dependencies
android.gradle_dependencies = com.android.volley:volley:1.1.0

# Internet permission
android.add_src = 

# Release settings
android.release_artifact = apk
