###
# Copyright (C) 2013 Dylan Steinmetz <dtsteinm@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.
#
#
###

from random import choice

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks


class Choose(callbacks.Plugin):
    """Make tough decisions between two or more options, easily."""
    def __init__(self, irc):
          callbacks.Plugin.__init__(self, irc)

    def choose(self, irc, msg, args, choices):
        """<choice1> ... <choiceN>

        Randomly selects one of multiple choices.
        """
        options = []
        options += [y.strip() for x in choices.split(' or ')
                for y in x.split(';')]
        irc.reply(choice(options))
    choose = wrap(choose, [additional('text')])

Class = Choose


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
