# Sandra Bot #

An extendable module driven STT/TTS personal assistant bot.

## Pre-requisites

* Python3.7

### Installation

* Install default speech engine:

```
sudo apt install libespeak1
```

* Install requirements:

```
pip install -r requirements.txt
```

### Configuration

* Create WIT AI account and APP.
* Obtain WIT AI API Key.
* Define `WIT_AI_API_KEY` environment variable with key value.

## Unit Tests

```
python -m unittest discover
```

### Running the application

With the appropriate configuration and pre-requisites, you can run the application with:

```shell script
python sandra.py
```

## Modules

You can define new handler modules in the `sandra/modules/` folder and they will be automatically included at runtime.
Simply create a new python file in this directory of the following form:

```python

from sandra.handler.handler import Handler

class HelloWorldHandler(Handler):
    # Some regex to trigger this handler
    HANDLER_PATTERN = "(.*?)hello(.*?)world(.*?)"

    def __init__(self):
        super().__init__()

    # Return a text string to be spoken via TTS
    def handle(self, command):
        return "Hello World"

```