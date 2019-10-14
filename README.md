# Generate Passwords Workflow 🔐 for [Alfred 3](http://www.alfredapp.com)

[![Latest Version](https://img.shields.io/github/tag/otherguy/alfred-passwords-workflow.svg?style=flat-square&label=release)](https://github.com/otherguy/alfred-passwords-workflow/tags)
[![Downloads](https://img.shields.io/github/downloads/otherguy/alfred-passwords-workflow/total.svg?style=flat-square)](https://github.com/otherguy/alfred-passwords-workflow/releases)
[![Circle CI](https://img.shields.io/circleci/project/github/otherguy/alfred-passwords-workflow/master.svg?style=flat-square)](https://circleci.com/gh/otherguy/alfred-passwords-workflow/tree/master)
[![Issues](https://img.shields.io/github/issues/otherguy/alfred-passwords-workflow.svg?style=flat-square)](https://github.com/otherguy/alfred-passwords-workflow/issues)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE.md)
[![Beerpay](https://img.shields.io/beerpay/otherguy/alfred-passwords-workflow.svg?style=flat-square)](https://beerpay.io/otherguy/alfred-passwords-workflow)

A workflow for [Alfred 3](http://www.alfredapp.com) that helps you to quickly and securely generate random passwords of any given length.

By default, it generates both an alphanumeric password and a strong password, containing special characters. As a bonus, it also generates [XKCD passwords](https://xkcd.com/936/) with 3 and 4 words.

Selecting the generated password copies it to the clipboard.

![Example Screencast](resources/screencast-1.gif)

The latest version can also be found here:

* https://https://pacmax.org/pac/otherguy-alfred-passwords-workflow/
* https://www.alfredforum.com/topic/11717-generate-passwords-workflow/

## Installation

Download the latest version of the `GenereratePasswords.alfredworkflow` from the [Releases](https://github.com/otherguy/alfred-passwords-workflow/releases) page and double click the downloaded file to install it.

The workflow supports automatic updates and will perform daily update checks.

## Caveats and Requirements

This workflow requires [Alfred 3](https://www.alfredapp.com) and won’t run on **Snow Leopard (10.6)** or lower.

## Usage

The default keyword is `pw`. The first and only parameter is the desired password length, defaulting to 10.

When hitting `⏎ Return` on a selected item, the generated password is copied to the clipboard.

## Planned Features

* Possibility to change default options (default password length, delimiter, XKCD word lists, ...)

## Developers

If you want to contribute, fork this repository and submit a pull request.

To make the project work locally on your machine, check out the repository and issue the following commands:

    $ pip install --ignore-installed --target=. Alfred-Workflow==1.36
    $ pip install --ignore-installed --target=lib -r requirements.txt

Alternatively, if you would rather work with a virtual environment, run these commands:

    $ virtualenv --python=python2.7 .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt

To run the script in the terminal, simply do:

    $ python pwgen.py

You can install `jq` from [Homebrew](https://brew.sh) and pipe the output of the workflow through this program to get nice formatting and the option to query the JSON.

## Acknowledgements

The following resources were used when creating this workflow:

* The excellent [Alfred-Workflow](https://github.com/deanishe/alfred-workflow) python library by [Dean Jackson](https://github.com/deanishe).
* The lock icon used in the workflow by [Pixel perfect](https://www.flaticon.com/authors/pixel-perfect) and licensed under [CC 3.0 BY](http://creativecommons.org/licenses/by/3.0/).
* The [`xkcdpass`](https://pypi.org/project/xkcdpass/) Python library for generating [XKCD passwords](https://xkcd.com/936/)

A big ♥️ _thank you_ to all creators!

## Support on Beerpay

If this is useful to you in any way or you end up building it yourself, you could buy me a beer! 

[![Beerpay](https://beerpay.io/otherguy/alfred-passwords-workflow/badge.svg?style=beer-square)](https://beerpay.io/otherguy/alfred-passwords-workflow)  [![Beerpay](https://beerpay.io/otherguy/alfred-passwords-workflow/make-wish.svg?style=flat-square)](https://beerpay.io/otherguy/alfred-passwords-workflow?focus=wish)
