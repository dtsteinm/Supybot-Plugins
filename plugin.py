###
# Copyright (C) 2013 Dylan Steinmetz <dtsteinm@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.conf as conf
# from supybot.Config import config


class Quiet(callbacks.Plugin):
    """Instruct your Infobot plugin to speak only when spoken to."""
    def __init__(self, irc):
        callbacks.Plugin.__init__(self, irc)

    def quiet(self, irc, msg, args):
        """Turn polite-mode on."""
        if conf.get(conf.supybot.plugins.Infobot.unaddressed.answerQuestions)\
            or\
            conf.get(conf.supybot.plugins.Infobot.unaddressed.
                    replyExistingFactoid):
            if conf.get(conf.supybot.plugins.Infobot.personality):
                irc.reply("Sorry, {}, I'll try to stay "
                        "quiet.".format(msg.nick), prefixNick=False)
            else:
                irc.reply("Entering polite mode.")
            conf.supybot.plugins.Infobot.unaddressed.answerQuestions.\
                    setValue(False)
            conf.supybot.plugins.Infobot.unaddressed.replyExistingFactoid.\
                    setValue(False)
        else:
            pass
    quiet = wrap(quiet)
    # TODO: shut up

    def wake(self, irc, msg, args):
        """Turn off polite-mode."""
        if conf.get(conf.supybot.plugins.Infobot.unaddressed.answerQuestions)\
            or\
            conf.get(conf.supybot.plugins.Infobot.unaddressed.
            replyExistingFactoid):
            pass
        else:
            if conf.get(conf.supybot.plugins.Infobot.personality):
                irc.reply("Good morning, {}.".format(msg.nick),
                        prefixNick=False)
            else:
                irc.reply("Leaving polite mode.")
            conf.supybot.plugins.Infobot.unaddressed.answerQuestions.\
                    setValue(True)
            conf.supybot.plugins.Infobot.unaddressed.replyExistingFactoid.\
                    setValue(True)
    awaken = wrap(wake)


Class = Quiet


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
