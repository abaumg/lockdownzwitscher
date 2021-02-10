# lockdownzwitscher
Twitter bot to tweet a daily countdown message.

## Installation
- install Python3 modules: `pip install -r requirements.txt`
- copy configuration file: `cp lockdownzwitscher.sample.ini lockdownzwitscher.ini`
- register a new Twitter app in the [Twitter Developer Portal](https://developer.twitter.com/en/portal/projects-and-apps)
- obtain *consumer API key* and *consumer API secret* and configure it in `lockdownzwitscher.ini`
- run `python setup_oauth.py` to obtain oAuth credentials and configure them in `lockdownzwitscher.ini`
