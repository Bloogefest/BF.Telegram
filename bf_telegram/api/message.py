#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Optional

from user import User
from chat import Chat

class Message:
    """
    This object represents a message.

    https://core.telegram.org/bots/api#message
    """

    def __init__(self,
                 message_id: int,
                 message_thread_id: Optional[int] = None,
                 from_: Optional[User] = None,
                 sender_chat: Optional[Chat] = None,
                 date: Optional[int] = None,
                 chat: Optional[Chat] = None,
                 forward_from: Optional[User] = None,
                 forward_from_chat: Optional[Chat] = None,
                 forward_from_message_id: Optional[int] = None,
                 forward_signature: Optional[str] = None,
                 forward_sender_name: Optional[str] = None,
                 forward_date: Optional[int] = None,
                 is_topic_message: Optional[bool] = None,
                 is_automatic_forward: Optional[bool] = None,
                 reply_to_message: Optional[Message] = None,
                 via_bot: Optional[User] = None,
                 edit_date: Optional[int] = None,
                 has_protected_content: Optional[bool] = None,
                 media_group_id: Optional[str] = None,
                 author_signature: Optional[str] = None,
                 text: Optional[str] = None,
                 entities: Optional[list[MessageEntity]] = None,
                 animation: Optional[Animation] = None,
                 audio: Optional[Audio] = None,
                 document: Optional[Document] = None,
                 photo: Optional[list[PhotoSize]] = None,
                 sticker: Optional[Sticker] = None,
                 video: Optional[Video] = None,
                 video_note: Optional[VideoNote] = None,
                 voice: Optional[Voice] = None,
                 caption: Optional[str] = None,
                 caption_entities: Optional[list[MessageEntity]] = None,
                 has_media_spoiler: Optional[bool] = None,
                 contact: Optional[bool] = None,
                 dice: Optional[Dice] = None,
                 game: Optional[Game] = None,
                 poll: Optional[Poll] = None,
                 venue: Optional[Venue] = None,
                 location: Optional[Location] = None,
                 new_chat_members: Optional[list[User]] = None,
                 left_chat_member: Optional[User] = None,
                 new_chat_title: Optional[str] = None,
                 new_chat_photo: Optional[list[PhotoSize]] = None,
                 delete_chat_photo: Optional[bool] = None,
                 group_chat_created: Optional[bool] = None,
                 supergroup_chat_created: Optional[bool] = None,
                 channel_chat_created: Optional[bool] = None,
                 message_auto_delete_timer_changed: Optional[MessageAutoDeleteTimerChanged] = None,
                 migrate_to_chat_id: Optional[int] = None,
                 migrate_from_chat_id: Optional[int] = None,
                 pinned_message: Optional[Message] = None,
                 invoice: Optional[Invoice] = None,
                 successful_payment: Optional[SuccessfulPayment] = None,
                 user_shared: Optional[UserShared] = None,
                 chat_shared: Optional[ChatShared] = None,
                 connected_website: Optional[str] = None,
                 write_access_allowed: Optional[WriteAccessAllowed] = None,
                 passport_data: Optional[PassportData] = None,
                 proximity_alert_triggered: Optional[ProximityAlertTriggered] = None,
                 forum_topic_created: Optional[ForumTopicCreated] = None,
                 forum_topic_edited: Optional[ForumTopicEdited] = None,
                 forum_topic_closed: Optional[ForumTopicClosed] = None,
                 forum_topic_reopened: Optional[ForumTopicReopened] = None,
                 general_forum_topic_hidden: Optional[GeneralForumTopicHidden] = None,
                 general_forum_topic_unhidden: Optional[GeneralForumTopicUnhidden] = None,
                 video_chat_scheduled: Optional[VideoChatScheduled] = None,
                 video_chat_started: Optional[VideoChatStarted] = None,
                 video_chat_ended: Optional[VideoChatEnded] = None,
                 video_chat_participants_invited: Optional[VideoChatParticipantsInvited] = None,
                 web_app_data: Optional[WebAppData] = None,
                 reply_markup: Optional[InlineKeyboardMarkup] = None):
        """
        :param message_id: Unique message identifier inside this chat
        :param message_thread_id: Unique identifier of a message thread to which the message belongs; for supergroups only
        :param from_: Sender of the message; empty for messages sent to channels. For backward compatibility, the field contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
        :param sender_chat: Sender of the message, sent on behalf of a chat. For example, the channel itself for channel posts, the supergroup itself for messages from anonymous group administrators, the linked channel for messages automatically forwarded to the discussion group. For backward compatibility, the field from contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
        :param date: Date the message was sent in Unix time
        :param chat: Conversation the message belongs to
        :param forward_from: For forwarded messages, sender of the original message
        :param forward_from_chat: For messages forwarded from channels or from anonymous administrators, information about the original sender chat
        :param forward_from_message_id: For messages forwarded from channels, identifier of the original message in the channel
        :param forward_signature: For forwarded messages that were originally sent in channels or by an anonymous chat administrator, signature of the message sender if present
        :param forward_sender_name: Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages
        :param forward_date: For forwarded messages, date the original message was sent in Unix time
        :param is_topic_message: True, if the message is sent to a forum topic
        :param is_automatic_forward: True, if the message is a channel post that was automatically forwarded to the connected discussion group
        :param reply_to_message: For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
        :param via_bot: Bot through which the message was sent
        :param edit_date: Date the message was last edited in Unix time
        :param has_protected_content: True, if the message can't be forwarded
        :param media_group_id: The unique identifier of a media message group this message belongs to
        :param author_signature: Signature of the post author for messages in channels, or the custom title of an anonymous group administrator
        :param text: For text messages, the actual UTF-8 text of the message
        :param entities: For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
        :param animation: Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set
        :param audio: Message is an audio file, information about the file
        :param document: Message is an audio file, information about the file
        :param photo: Message is a photo, available sizes of the photo
        :param sticker: Message is a sticker, information about the sticker
        :param video: Message is a video, information about the video
        :param video_note: Message is a video note, information about the video message
        :param voice: Message is a voice message, information about the file
        :param caption: Caption for the animation, audio, document, photo, video or voice
        :param caption_entities: For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
        :param has_media_spoiler: True, if the message media is covered by a spoiler animation
        :param contact: Message is a shared contact, information about the contact
        :param dice: Message is a dice with random value
        :param game: Message is a game, information about the game.
        :param poll: Message is a native poll, information about the poll
        :param venue: Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set
        :param location: Message is a shared location, information about the location
        :param new_chat_members: New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
        :param left_chat_member: A member was removed from the group, information about them (this member may be the bot itself)
        :param new_chat_title: A chat title was changed to this value
        :param new_chat_photo: A chat photo was change to this value
        :param delete_chat_photo: Service message: the chat photo was deleted
        :param group_chat_created: Service message: the group has been created
        :param supergroup_chat_created: Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
        :param channel_chat_created: Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
        :param message_auto_delete_timer_changed: Service message: auto-delete timer settings changed in the chat
        :param migrate_to_chat_id: The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
        :param migrate_from_chat_id: The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
        :param pinned_message: The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
        :param invoice: Message is an invoice for a payment, information about the invoice.
        :param successful_payment: Message is a service message about a successful payment, information about the payment.
        :param user_shared: Service message: a user was shared with the bot
        :param chat_shared: Service message: a chat was shared with the bot
        :param connected_website: The domain name of the website on which the user has logged in.
        :param write_access_allowed: Service message: the user allowed the bot added to the attachment menu to write messages
        :param passport_data: Telegram Passport data
        :param proximity_alert_triggered: Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.
        :param forum_topic_created: Service message: forum topic created
        :param forum_topic_edited: Service message: forum topic edited
        :param forum_topic_closed: Service message: forum topic closed
        :param forum_topic_reopened: Service message: forum topic reopened
        :param general_forum_topic_hidden: Service message: the 'General' forum topic hidden
        :param general_forum_topic_unhidden: Service message: the 'General' forum topic unhidden
        :param video_chat_scheduled: Service message: video chat scheduled
        :param video_chat_started: Service message: video chat started
        :param video_chat_ended: Service message: video chat ended
        :param video_chat_participants_invited: Service message: new participants invited to a video chat
        :param web_app_data: Service message: data sent by a Web App
        :param reply_markup: Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
        """
        self.message_id = message_id
        self.message_thread_id = message_thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.forward_from = forward_from
        self.forward_from_chat = forward_from_chat
        self.forward_from_message_id = forward_from_message_id
        self.forward_signature = forward_signature
        self.forward_sender_name = forward_sender_name
        self.forward_date = forward_date
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.text = text
        self.entities = entities
        self.animation = animation
        self.audio = audio
        self.document = document
        self.photo = photo
        self.sticker = sticker
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.caption = caption
        self.caption_entities = caption_entities
        self.has_media_spoiler = has_media_spoiler
        self.contact = contact
        self.dice = dice
        self.game = game
        self.poll = poll
        self.venue = venue
        self.location = location
        self.new_chat_members = new_chat_members
        self.left_chat_member = left_chat_member
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.message_auto_delete_timer_changed = message_auto_delete_timer_changed
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = pinned_message
        self.invoice = invoice
        self.successful_payment = successful_payment
        self.user_shared = user_shared
        self.chat_shared = chat_shared
        self.connected_website = connected_website
        self.write_access_allowed = write_access_allowed
        self.passport_data = passport_data
        self.proximity_alert_triggered = proximity_alert_triggered
        self.forum_topic_created = forum_topic_created
        self.forum_topic_edited = forum_topic_edited
        self.forum_topic_closed = forum_topic_closed
        self.forum_topic_reopened = forum_topic_reopened
        self.general_forum_topic_hidden = general_forum_topic_hidden
        self.general_forum_topic_unhidden = general_forum_topic_unhidden
        self.video_chat_scheduled = video_chat_scheduled
        self.video_chat_started = video_chat_started
        self.video_chat_ended = video_chat_ended
        self.video_chat_participants_invited = video_chat_participants_invited
        self.web_app_data = web_app_data
        self.reply_markup = reply_markup
