
# Pylertatron

A simple Pylertatron wrapper for Python
## Installation

Install pylertatron with PIP:

```
pip install pylertatron
```
## Usage

```py
from alertatron.sync import Pylertatron, Alert
from alertatron.commands import *

al = Pylertatron(webhook_url="https://webhook.com", 
balance_ratio=0.5, api_key_name="ApiKey", ")
```