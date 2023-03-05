#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Optional

from user import User

class MessageEntity:
    """
    This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    https://core.telegram.org/bots/api#messageentity
    """

    def __init__(self,
                 type: str,
                 offset: int,
                 length: int,
                 url: Optional[str] = None,
                 user: Optional[User] = None,
                 language: Optional[str] = None,
                 custom_emoji_id: Optional[str] = None):
        """
        :param type: Type of the entity. Currently, can be “mention” (@username), “hashtag” (#hashtag), “cashtag” ($USD), “bot_command” (/start@jobs_bot), “url” (https://telegram.org), “email” (do-not-reply@telegram.org), “phone_number” (+1-212-555-0123), “bold” (bold text), “italic” (italic text), “underline” (underlined text), “strikethrough” (strikethrough text), “spoiler” (spoiler message), “code” (monowidth string), “pre” (monowidth block), “text_link” (for clickable text URLs), “text_mention” (for users without usernames), “custom_emoji” (for inline custom emoji stickers)
        :param offset: Offset in UTF-16 code units to the start of the entity
        :param length: Length of the entity in UTF-16 code units
        :param url: For “text_link” only, URL that will be opened after user taps on the text
        :param user: For “text_mention” only, the mentioned user
        :param language: For “pre” only, the programming language of the entity text
        :param custom_emoji_id: For “custom_emoji” only, unique identifier of the custom emoji. Use getCustomEmojiStickers to get full information about the sticker
        """
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language
        self.custom_emoji_id = custom_emoji_id
