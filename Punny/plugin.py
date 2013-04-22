###
# Copyright (C) 2013 Dylan Steinmetz <dtsteinm@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.
#
#
###

import punny
from os.path import isfile
from pickle import Pickler, Unpickler

import supybot.conf as conf
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

filename = conf.supybot.directories.data.dirize('Punny.dat')
see_help = 'You did not provide enough parameters. Please use @help '\
                'punny add for details.'

class Punny(callbacks.Plugin):
    """Generates and displays puns with the 'squid' command.
    Additional replacements can be specified with the 'add' command.  """
    def __init__(self, irc):
        callbacks.Plugin.__init__(self, irc)
        self.pungen = punny.PunGenerator()
        if isfile(filename):
            # TODO: Use punny load or update (when written)
            self.config = self._getpuns(filename)
            self._setconf(self.config)
        # plugins.ChannelDBHandler.__init__(self)

    def _getpuns(self, filename):
        """Get the pun dictionary from the conf file."""
        with open(filename, 'r') as f:
            pickle = Unpickler(f)
            return pickle.load()

    def _setconf(self, config):
        """Overwrite the default pun dictionary with """ \
                """the one retrieved from the config file."""
        # FIXME: Check for changes in module's pun dictionary
        self.pungen.puns = config

    def _squid(self, irc, msg, args, phrase):
        """<phrase>

        Generates a clever squid pun.
        """
        # TODO: I would like to find a way to force this being
        #       displayed in the channel
        # TODO: Log when called
        irc.reply(self.pungen.generate_pun(phrase))
    squid = wrap(_squid, [additional('text')])

    def _add(self, irc, msg, args, words):
        """<pun> [<word> [<replace>]]

        Add a new pun to the dictionary.
        If <word> is supplied, <pun> will automatically replace
        all occurences of <word> found in phrases sent to squid.
        <replace> can be used to specify an alternative when a
        drop-in replacement of <word> with <pun> does not make sense.
        """
        """Compare:
        user : bot: punny add fin even
        user : bot: punny squid What is this, I don't even.
        bot : user: What is this, I don't fin.
        To:
        user : bot: punny add fin even efin
        user : bot: punny squid What is this, I don't even.
        bot : user: What is this, I don't efin.
        """
        if words is None:
            irc.reply(see_help)
            return
        # TODO: Use 'spiced up' success messages
        try:
            # TODO: Check if it exists (probably just
            #       implement in punny module?)
            self.pungen.add_pun(*words.split())
            self._save()
            irc.reply(conf.supybot.replies.success)
        except:
            # TODO: Log this
            irc.reply(conf.supybot.replies.error)
    add = wrap(_add, [additional('text')])

    def _save(self):
        """Save the current pun dictionary to a conf file."""
        # TODO: Use punny dump (when written)
        with open(filename, 'w') as f:
            pickle = Pickler(f)
            pickle.dump(self.pungen.puns)

    def _list(self, irc, msg, args):
        """List the currently available puns."""
        # TODO: write _list; use punny modules print/list if avail
        pass
    #list = wrap(_list)

# TODO: Add error classes

Class = Punny


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
