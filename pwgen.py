#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from workflow import Workflow3 as Workflow, ICON_INFO

def main(wf):
  # Imports go here.
  from xkcdpass import xkcd_password as xp
  import string
  from random import SystemRandom

  def genpw(size, chars):
    return ''.join(SystemRandom().choice(chars) for _ in range(size))

  # Defaults
  defaults = {
    'password_length': 10,
    'xkcd_delimiter':  '-',
    'xkcd_minlength':  4,
    'xkcd_maxlength':  10,
    'xkcd_wordllist': 'eff-long', # eff-long (English), spa-mich (Spanish), fin-kotus (Finnish),ita-wiki (Italian), ger-anlx (German)
  }

  # ================================= MAIN ===================================

  # Get args from Workflow, already in normalized Unicode
  password_length = defaults['password_length']
  if len(wf.args) >= 1:
    try:
      password_length = int(wf.args[0].strip())
    except ValueError:
      pass

  # XKCD options
  # TODO: add possibility to change options
  xkcd_wordfile = defaults['xkcd_wordllist']
  xkcd_min_length = defaults['xkcd_minlength']
  xkcd_max_length = defaults['xkcd_maxlength']
  xkcd_delimiter = defaults['xkcd_delimiter']

  # Get XKCD Wordlist and passwords
  mywords = xp.generate_wordlist(wordfile=xkcd_wordfile, min_length=xkcd_min_length, max_length=xkcd_max_length)
  xkcd_3 = xp.generate_xkcdpassword(mywords, 3, False, False, xkcd_delimiter)
  xkcd_4 = xp.generate_xkcdpassword(mywords, 4, False, False, xkcd_delimiter)

  # Allowed Special Characters
  # https://www.owasp.org/index.php/Password_special_characters
  special_chars = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
  full_pw_charset = string.ascii_uppercase + string.ascii_lowercase + string.digits + special_chars
  alnum_pw_charset = string.ascii_uppercase + string.ascii_lowercase + string.digits

  # Generate passwords
  full_pw = genpw(password_length, full_pw_charset)
  alnum_pw = genpw(password_length, alnum_pw_charset)

  # Update workflow if a new version is available.
  if wf.update_available is True:
    wf.add_item('New version available', 'Press enter to install the update.',
      autocomplete='workflow:update',
      icon=ICON_INFO
    )

  # Add password items
  wf.add_item('%d character password' % password_length, full_pw, valid=True, arg=full_pw)
  wf.add_item('%d character password (no special characters)' % password_length, alnum_pw, valid=True, arg=alnum_pw)
  wf.add_item('XKCD Password (3 words)', xkcd_3, valid=True, arg=xkcd_3)
  wf.add_item('XKCD Password (4 words)', xkcd_4, valid=True, arg=xkcd_4)

  # Send output to Alfred.
  wf.send_feedback()
  return 0

if __name__ == '__main__':
  # Create a global `Workflow` object
  workflow3 = Workflow(
    libraries=['./lib'], update_settings={
      'github_slug': 'otherguy/alfred-passwords-workflow',
      'frequency': 1, # every day
    },
    help_url='https://github.com/otherguy/alfred-passwords-workflow'
  )

  workflow3.magic_prefix = 'wf:'

  # Call your entry function via `Workflow.run()` to enable its helper
  # functions, like exception catching, ARGV normalization, magic
  # arguments etc.
  sys.exit(workflow3.run(main))
