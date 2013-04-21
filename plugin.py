###
# Copyright (c) 2013, Dylan Steinmetz
# All rights reserved.
#
#
###

from random import Random as rand

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks


class Choose(callbacks.Plugin):
    """Make tough desicions between two or more options, easily."""
    def __init__(self, irc):
          callbacks.Plugin.__init__(self, irc)

    def choose(self, irc, msg, args, choices):
        """<choice1> ... <choiceN>

        Randomly selects one of multiple choices.
        """
        options = []
        options += [x.strip() for x in choices.split('or')]
        irc.reply(rand().choice(options))
    choose = wrap(choose, [additional('text')])

Class = Choose


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
