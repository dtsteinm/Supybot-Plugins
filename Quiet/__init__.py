###
# Copyright (C) 2013 Dylan Steinmetz <dtsteinm@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.
#
#
###

"""
Allows you to quickly and easily toggle whether your Infobot will speak when
not addressed.
"""

import supybot
import supybot.world as world

# Use this for the version of this plugin.  You may wish to put a CVS keyword
# in here if you're keeping the plugin in CVS or some similar system.
__version__ = "0.1"

# XXX Replace this with an appropriate author or supybot.Author instance.
__author__ = "Dylan Steinmetz <dtsteinm@gmail.com>"

# This is a dictionary mapping supybot.Author instances to lists of
# contributions.
__contributors__ = {}

# This is a url where the most recent plugin package can be downloaded.
__url__ = 'https://github.com/dtsteinm/supybot-plugins/tree/master/Quiet'

import config
import plugin
reload(plugin) # In case we're being reloaded.
# Add more reloads here if you add third-party modules and want them to be
# reloaded when this plugin is reloaded.  Don't forget to import them as well!

if world.testing:
    import test

Class = plugin.Class
configure = config.configure


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
