from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from beez.socket.SocketConnector import SocketConnector
    from beez.challenge.Challenge import Challenge

from beez.socket.Message import Message
from beez.socket.MessageType import MessageType

class MessageChallenges(Message):

    def __init__(self, senderConnector: SocketConnector, messageType: MessageType, challenges: List[Challenge]):
        super().__init__(senderConnector, messageType)
        self.challenges = challenges