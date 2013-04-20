###
# Copyright (c) 2013, Dylan Steinmetz 

# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.conf as conf
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import punny
from os.path import isfile
from pickle import Pickler, Unpickler

filename = conf.supybot.directories.data.dirize('Punny.dat')

class Punny(callbacks.Plugin):
    """ Generates and displays puns with the 'squid' command.
    Additional replacements can be specified with the 'add' command.  """
    def __init__(self, irc):
        callbacks.Plugin.__init__(self, irc)
        self.pungen = punny.PunGenerator()
        if isfile(filename):
            self.conf = self._getpuns(filename)
            self._setconf(self.conf)
        # plugins.ChannelDBHandler.__init__(self)


    def _getpuns(self, filename):
        """Get the pun dictionary from the conf file."""
        with open(filename, 'r') as f:
            pickle = Unpickler(f)
            return pickle.load()
    def _setconf(self, conf):
        """Overwrite the default pun dictionary with """ \
                """the one retrieved from the conf file."""
        self.pungen.puns = conf
    def _squid(self, irc, msg, args, phrase):
        """<phrase>

        Generates a clever squid pun.
        """
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
        self.pungen.add_pun(*words.split())
        self._save()
    add = wrap(_add, [additional('text')])    
    def _save(self):
        """Save the current pun dictionary to a conf file."""
        with open(filename, 'w') as f:
            pickle = Pickler(f)
            pickle.dump(self.pungen.puns)
    def _list(self, irc, msg, args):
        """List the currently available puns."""
        pass
    #list = wrap(_list)

Class = Punny


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
