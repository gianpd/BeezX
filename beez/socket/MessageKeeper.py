from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from beez.socket.SocketConnector import SocketConnector
    from beez.challenge.Keeper import Keeper

from beez.socket.Message import Message
from beez.socket.MessageType import MessageType

class MessageKeeper(Message):

    def __init__(self, senderConnector: SocketConnector, messageType: MessageType, keeper: Keeper):
        super().__init__(senderConnector, messageType)
        self.keeper = keeper