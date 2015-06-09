Encompass-Mercury Server for the Encompass Multi-Coin client
============================================================

  * Author: Tyler Willis (kefkius)
  * Language: Python

Forked from [Electrum Server](https://github.com/spesmilo/electrum)

Features
--------

  * Arbitrary blockchains can be supported via modules.

  * The server indexes UTXOs by address, in a Patricia tree structure
    described by Alan Reiner (see the 'ultimate blockchain
    compression' thread in the Bitcointalk forum)

  * The server requires bitcoind, leveldb and plyvel

  * The server code is open source. Anyone can run a server, removing
    single points of failure concerns.

  * The server knows which set of Bitcoin addresses belong to the same
    wallet, which might raise concerns about anonymity. However, it
    should be possible to write clients capable of using several
    servers.

Installation
------------

  1. To install and run a server, see INSTALL. For greater
     detail on the installation process, see HOWTO.md.

  2. To start and stop the server, use the 'encompass-mercury' script



License
-------

Encompass-Mercury is made available under the terms of the [GNU Affero General
Public License](http://www.gnu.org/licenses/agpl.html), version 3. See the 
included `LICENSE` for more details.
