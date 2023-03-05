#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Optional

class User:
    """
    This object represents a Telegram user or bot.

    https://core.telegram.org/bots/api#user
    """

    def __init__(self,
                 id_: int,
                 is_bot: bool,
                 first_name: str,
                 last_name: Optional[str] = None,
                 username: Optional[str] = None,
                 language_code: Optional[str] = None,
                 is_premium: Optional[bool] = None,
                 added_to_attachment_menu: Optional[bool] = None,
                 can_join_groups: Optional[bool] = None,
                 can_read_all_group_messages: Optional[bool] = None,
                 supports_inline_queries: Optional[bool] = None):
        """
        :param id_: Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
        :param is_bot: True, if this user is a bot
        :param first_name: User's or bot's first name
        :param last_name: User's or bot's last name
        :param username: User's or bot's username
        :param language_code: IETF language tag of the user's language
        :param is_premium: True, if this user is a Telegram Premium user
        :param added_to_attachment_menu: True, if this user added the bot to the attachment menu
        :param can_join_groups: True, if this user added the bot to the attachment menu
        :param can_read_all_group_messages: True, if privacy mode is disabled for the bot. Returned only in getMe.
        :param supports_inline_queries: True, if the bot supports inline queries. Returned only in getMe.
        """
        self.id_ = id_
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.is_premium = is_premium
        self.added_to_attachment_menu = added_to_attachment_menu
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries
