
# Pylertatron

A simple Alertatron wrapper for Python








## Installation

Install pylertatron with PIP:

```
pip install pylertatron
```
## Usage

```py
from alertatron.sync import Alertatron, Alert
from alertatron.commands import *

al = Alertatron(webhook_url="https://webhook.com", 
balance_ratio=0.5, api_key_name="ApiKey", ")
```