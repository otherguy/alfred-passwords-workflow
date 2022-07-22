# Generate Passwords Workflow 🔐 for [Alfred 4](http://www.alfredapp.com)

[![Latest Version](https://img.shields.io/github/tag/otherguy/alfred-passwords-workflow.svg?style=flat-square&label=release)](https://github.com/otherguy/alfred-passwords-workflow/tags)
[![Downloads](https://img.shields.io/github/downloads/otherguy/alfred-passwords-workflow/total.svg?style=flat-square)](https://github.com/otherguy/alfred-passwords-workflow/releases)
[![Issues](https://img.shields.io/github/issues/otherguy/alfred-passwords-workflow.svg?style=flat-square)](https://github.com/otherguy/alfred-passwords-workflow/issues)
[![Code Climate technical debt](https://img.shields.io/codeclimate/tech-debt/otherguy/alfred-passwords-workflow?style=flat-square)](https://codeclimate.com/github/otherguy/alfred-passwords-workflow)
[![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/otherguy/alfred-passwords-workflow?style=flat-square)](https://codeclimate.com/github/otherguy/alfred-passwords-workflow)
[![MIT License](https://img.shields.io/badge/license-MIT-pink.svg?style=flat-square)](LICENSE.md)

A workflow for [Alfred 4](http://www.alfredapp.com) that helps you to quickly and securely generate random passwords of any given length.

By default, it generates a strong password (containing special characters), an alphanumeric password, and an easy-to-read strong password (omitting characters which might be ambiguous like `I`, `1`, `O`, `0`, etc. and potentially problematic special characters). As a bonus, it also generates [XKCD passwords](https://xkcd.com/936/) with both 3 and 4 words.

Selecting the generated password in Alfred copies it to the clipboard.

![Example Screencast](resources/screencast-1.gif)

The latest version can also be found on:

* [Pacmax](https://pacmax.org/pac/otherguy-alfred-passwords-workflow/)
* [The Alfred Forum](https://www.alfredforum.com/topic/11717-generate-passwords-workflow/)

## Installation

Download the latest version of the `GenereratePasswords.alfredworkflow` from the [Releases](https://github.com/otherguy/alfred-passwords-workflow/releases) page and double click the downloaded file to install it.

The workflow supports automatic updates and will perform daily update checks.

## Caveats and Requirements

This workflow requires [Alfred 4](https://www.alfredapp.com).

## Usage

The default keyword is `pw`. The first and only parameter is the desired password length, defaulting to 20.

When hitting `⏎ Return` on a selected item, the generated password is copied to the clipboard.

## Planned Features

* Possibility to change default options (default password length, delimiter, XKCD word lists, ...)

## Developers

If you want to contribute, fork this repository and submit a pull request.

To make the project work locally on your machine, check out the repository and issue the following commands:

    $ python -m pip install --ignore-installed --target=lib -r requirements.txt

Alternatively, if you would rather work with a virtual environment, run these commands (replace `<your-python-version>`
with the version of Python you want to use, but 3.4 is the minimum requirement):

    $ python -m pip install virtualenv
    $ python -m virtualenv --python=python<your-python-version> .venv
    $ source .venv/bin/activate
    $ python -m pip install -r requirements.txt

To run the script in the terminal, simply run:

    $ python pwgen.py

You can install `jq` from [Homebrew](https://brew.sh) and pipe the output of the workflow through this program to get nice formatting and the option to query the JSON.

## Acknowledgements

The following resources were used when creating this workflow:

* The excellent [Alfred-Workflow](https://github.com/deanishe/alfred-workflow) python library by [Dean Jackson](https://github.com/deanishe).
* The lock icon used in the workflow by [Pixel perfect](https://www.flaticon.com/authors/pixel-perfect) and licensed under [CC 3.0 BY](http://creativecommons.org/licenses/by/3.0/).
* The [`xkcdpass`](https://pypi.org/project/xkcdpass/) Python library for generating [XKCD passwords](https://xkcd.com/936/)

A big ♥️ _thank you_ to all creators!
