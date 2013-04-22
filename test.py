###
# Copyright (C) 2013 Dylan Steinmetz <dtsteinm@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.
#
#
###

from supybot.test import *

class QuietTestCase(PluginTestCase):
    plugins = ('Quiet',)


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
