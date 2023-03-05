#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Optional

from webhook_info import WebhookInfo

class Update:
    """
    This object represents an incoming update.
    At most one of the optional parameters can be present in any given update.

    https://core.telegram.org/bots/api#update
    """

    def __init__(self,
                 update_id: int,
                 message: Optional[Message] = None,
                 edited_message: Optional[Message] = None,
                 channel_post: Optional[Message] = None,
                 edited_channel_post: Optional[Message] = None,
                 inline_query: Optional[InlineQuery] = None,
                 chosen_inline_result: Optional[ChosenInlineResult] = None,
                 callback_query: Optional[CallbackQuery] = None,
                 shipping_query: Optional[ShippingQuery] = None,
                 pre_checkout_query: Optional[PreCheckoutQuery] = None,
                 poll: Optional[Poll] = None,
                 poll_answer: Optional[PollAnswer] = None,
                 my_chat_member: Optional[ChatMemberUpdated] = None,
                 chat_member: Optional[ChatMemberUpdated] = None,
                 chat_join_request: Optional[ChatJoinRequest] = None):
        """
        :param update_id: The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you're using webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
        :param message: New incoming message of any kind - text, photo, sticker, etc.
        :param edited_message: New version of a message that is known to the bot and was edited
        :param channel_post: New incoming channel post of any kind - text, photo, sticker, etc.
        :param edited_channel_post: New version of a channel post that is known to the bot and was edited
        :param inline_query: New incoming inline query
        :param chosen_inline_result: The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.
        :param callback_query: New incoming callback query
        :param shipping_query: New incoming callback query
        :param pre_checkout_query: New incoming pre-checkout query. Contains full information about checkout
        :param poll: New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
        :param poll_answer: New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
        :param my_chat_member: New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
        :param chat_member: New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
        :param chat_join_request: New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
        """
        self.update_id = update_id
        self.message = message
        self.edited_message = edited_message
        self.channel_post = channel_post
        self.edited_channel_post = edited_channel_post
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query
        self.poll = poll
        self.poll_answer = poll_answer
        self.my_chat_member = my_chat_member
        self.chat_member = chat_member
        self.chat_join_request = chat_join_request

    def get_updates(self,
                    offset: Optional[int] = None,
                    limit: Optional[int] = None,
                    timeout: Optional[int] = None,
                    allowed_updates: Optional[list[str]] = None) -> list[Update]:
        """
        Use this method to receive incoming updates using long polling (wiki).

        :param offset: Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will forgotten.
        :param limit: Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100.
        :param timeout: Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only.
        :param allowed_updates: A JSON-serialized list of the update types you want your bot to receive. For example, specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all update types except chat_member (default). If not specified, the previous setting will be used. Please note that this parameter doesn't affect updates created before the call to the getUpdates, so unwanted updates may be received for a short period of time.
        :return: Returns an Array of Update objects.

        https://core.telegram.org/bots/api#getupdates
        """
        pass

    def set_webhook(self,
                    url: str,
                    certificate: Optional[InputFile] = None,
                    ip_address: Optional[str] = None,
                    max_connections: Optional[int] = None,
                    allowed_updates: Optional[list[str]] = None,
                    drop_pending_updates: Optional[bool] = None,
                    secret_token: Optional[str] = None) -> bool:
        """
        Use this method to specify a URL and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified URL, containing a JSON-serialized Update. In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns True on success. If you'd like to make sure that the webhook was set by you, you can specify secret data in the parameter secret_token. If specified, the request will contain a header “X-Telegram-Bot-Api-Secret-Token” with the secret token as content.

        :param url: HTTPS URL to send updates to. Use an empty string to remove webhook integration
        :param certificate: Upload your public key certificate so that the root certificate in use can be checked. See our self-signed guide for details.
        :param ip_address: Upload your public key certificate so that the root certificate in use can be checked. See our self-signed guide for details.
        :param max_connections: Upload your public key certificate so that the root certificate in use can be checked. See our self-signed guide for details.
        :param allowed_updates: A JSON-serialized list of the update types you want your bot to receive. For example, specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all update types except chat_member (default). If not specified, the previous setting will be used. Please note that this parameter doesn't affect updates created before the call to the setWebhook, so unwanted updates may be received for a short period of time.
        :param drop_pending_updates: Pass True to drop all pending updates
        :param secret_token: A secret token to be sent in a header “X-Telegram-Bot-Api-Secret-Token” in every webhook request, 1-256 characters. Only characters A-Z, a-z, 0-9, _ and - are allowed. The header is useful to ensure that the request comes from a webhook set by you.
        :return: Returns True on success.

        https://core.telegram.org/bots/api#setwebhook
        """
        pass

    def delete_webhook(self, drop_pending_updates: Optional[bool] = None) -> bool:
        """
        Use this method to remove webhook integration if you decide to switch back to getUpdates.

        :param drop_pending_updates: Pass True to drop all pending updates
        :return: Returns True on success.

        https://core.telegram.org/bots/api#deletewebhook
        """
        pass

    def get_webhook_info(self) -> WebhookInfo:
        """
        Use this method to get current webhook status. Requires no parameters.

        :return: On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty.

        https://core.telegram.org/bots/api#getwebhookinfo
        """
        pass
