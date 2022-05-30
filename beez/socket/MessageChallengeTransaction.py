from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from beez.socket.SocketConnector import SocketConnector
    from beez.transaction.ChallengeTX import ChallengeTX


from beez.socket.Message import Message
from beez.socket.MessageType import MessageType

class MessageChallengeTransation(Message):

    def __init__(self, senderConnector: SocketConnector, messageType: MessageType, challengeTx: ChallengeTX):
        super().__init__(senderConnector, messageType)
        self.challengeTx = challengeTx