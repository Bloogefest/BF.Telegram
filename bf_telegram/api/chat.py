#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Optional

class Chat:
    """
    This object represents a chat.

    https://core.telegram.org/bots/api#chat
    """

    def __init__(self,
                 id: int,
                 type: str,
                 title: Optional[str] = None,
                 username: Optional[str] = None,
                 first_name: Optional[str] = None,
                 last_name: Optional[str] = None,
                 is_forum: Optional[bool] = None,
                 photo: Optional[ChatPhoto] = None,
                 active_usernames: Optional[list[str]] = None,
                 emoji_status_custom_emoji_id: Optional[str] = None,
                 bio: Optional[str] = None,
                 has_private_forwards: Optional[bool] = None,
                 has_restricted_voice_and_video_messages: Optional[bool] = None,
                 join_to_send_messages: Optional[bool] = None,
                 join_by_request: Optional[bool] = None,
                 description: Optional[str] = None,
                 invite_link: Optional[str] = None,
                 pinned_message: Optional[Message] = None,
                 permissions: Optional[ChatPermissions] = None,
                 slow_mode_delay: Optional[int] = None,
                 message_auto_delete_time: Optional[int] = None,
                 has_aggressive_anti_spam_enabled: Optional[bool] = None,
                 has_hidden_members: Optional[bool] = None,
                 has_protected_content: Optional[bool] = None,
                 sticker_set_name: Optional[str] = None,
                 can_set_sticker_set: Optional[bool] = None,
                 linked_chat_id: Optional[int] = None,
                 location: Optional[ChatLocation] = None):
        """
        :param id: Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
        :param type: Type of chat, can be either “private”, “group”, “supergroup” or “channel”
        :param title: Title, for supergroups, channels and group chats
        :param username: Username, for private chats, supergroups and channels if available
        :param first_name: First name of the other party in a private chat
        :param last_name: Last name of the other party in a private chat
        :param is_forum: True, if the supergroup chat is a forum (has topics enabled)
        :param photo: Chat photo. Returned only in getChat.
        :param active_usernames: If non-empty, the list of all active chat usernames; for private chats, supergroups and channels. Returned only in getChat.
        :param emoji_status_custom_emoji_id: Custom emoji identifier of emoji status of the other party in a private chat. Returned only in getChat.
        :param bio: Bio of the other party in a private chat. Returned only in getChat.
        :param has_private_forwards: True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user. Returned only in getChat.
        :param has_restricted_voice_and_video_messages: True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat. Returned only in getChat.
        :param join_to_send_messages: True, if users need to join the supergroup before they can send messages. Returned only in getChat.
        :param join_by_request: True, if all users directly joining the supergroup need to be approved by supergroup administrators. Returned only in getChat.
        :param description: Description, for groups, supergroups and channel chats. Returned only in getChat.
        :param invite_link: Primary invite link, for groups, supergroups and channel chats. Returned only in getChat.
        :param pinned_message: The most recent pinned message (by sending date). Returned only in getChat.
        :param permissions: Default chat member permissions, for groups and supergroups. Returned only in getChat.
        :param slow_mode_delay: For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user; in seconds. Returned only in getChat.
        :param message_auto_delete_time: The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat.
        :param has_aggressive_anti_spam_enabled: True, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators. Returned only in getChat.
        :param has_hidden_members: True, if non-administrators can only get the list of bots and administrators in the chat. Returned only in getChat.
        :param has_protected_content: True, if messages from the chat can't be forwarded to other chats. Returned only in getChat.
        :param sticker_set_name: For supergroups, name of group sticker set. Returned only in getChat.
        :param can_set_sticker_set: True, if the bot can change the group sticker set. Returned only in getChat.
        :param linked_chat_id: Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat.
        :param location: For supergroups, the location to which the supergroup is connected. Returned only in getChat.
        """
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum
        self.photo = photo
        self.active_usernames = active_usernames
        self.emoji_status_custom_emoji_id = emoji_status_custom_emoji_id
        self.bio = bio
        self.has_private_forwards = has_private_forwards
        self.has_restricted_voice_and_video_messages = has_restricted_voice_and_video_messages
        self.join_to_send_messages = join_to_send_messages
        self.join_by_request = join_by_request
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = permissions
        self.slow_mode_delay = slow_mode_delay
        self.message_auto_delete_time = message_auto_delete_time
        self.has_aggressive_anti_spam_enabled = has_aggressive_anti_spam_enabled
        self.has_hidden_members = has_hidden_members
        self.has_protected_content = has_protected_content
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.linked_chat_id = linked_chat_id
        self.location = location
