# TTS Maker

An Android text-to-speech app built with Python and Kivy. Type some text, pick a language and a speed, and the phone reads it aloud.

## Features

- Six languages: English, Hindi, Telugu, French, German and Japanese.
- Adjustable speech rate from 0.5x to 4.0x.
- Uses Android's built-in `TextToSpeech` engine through Pyjnius.
- Shows a message for empty text or an out-of-range speed.

On a desktop the app opens, but speech only works on Android.

## Build the Android app

Buildozer packages the app as an APK (configured in `buildozer.spec`, target API 33). On Linux or WSL:

```
pip install buildozer==1.4.0
buildozer android debug     # the APK is written to bin/
```

`.github/workflows/build.yml` runs this build on GitHub Actions. It currently stops while compiling a dependency for Android, so build the APK locally until that is fixed.

## Run on a desktop (interface only)

```
pip install -r requirements.txt
python main.py
```

## Tech stack

Python, Kivy, Pyjnius, Android TextToSpeech, Buildozer, GitHub Actions.
