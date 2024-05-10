LDPlayer Tools
==============
This is package for ldplayer emulator control software. (unofficial)

#### Table of contents

* [Install](#install)
* [Other libraries](#other-libraries)
* [Environments](#environments)
* [Example](#example)
* [License](#license)

#### Contribute to ldplayer
Please fork and create a pull request 🙂


Install
==========
```shell
pip install ldplayer-tools
```

Other libraries
===============
other libraries that may be needed for your automation
* __uiautomator2__ [repo](https://github.com/openatx/uiautomator2)
* __pure-python-adb__ [repo](https://github.com/Swind/pure-python-adb)
* __weditor__ [repo](https://github.com/alibaba/web-editor)

Environments
============
* __ldplayer 9__
* __python 3.11__
* __pure-python-adb__

Example
=======

manage instance
```python
from ldplayer import LDPlayer

ld = LDPlayer("path/to/ldconsole.exe")
print(ld.instances())
```

tap or swipe event
```python
from ppadb.client import Client as AdbClient
from ldplayer import Controller

client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("emulator-5554") # or your device name

ldc = Controller(device)
ldc.tap(x=10, y=10)
```

License
==========
This package is open-sourced software licensed under the [MIT license](https://github.com/mantvmass/ldplayer/blob/main/LICENSE).