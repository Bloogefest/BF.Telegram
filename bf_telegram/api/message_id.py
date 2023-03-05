#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

class MessageId:
    """
    This object represents a unique message identifier.

    https://core.telegram.org/bots/api#messageid
    """

    def __init__(self, message_id: int):
        """
        :param message_id: 	Unique message identifier 
        """
        self.message_id = message_id
