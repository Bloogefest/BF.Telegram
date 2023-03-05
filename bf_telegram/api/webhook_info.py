#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Optional

class WebhookInfo:
    """
    Describes the current status of a webhook.

    https://core.telegram.org/bots/api#webhookinfo
    """

    def __init__(self,
                 url: str,
                 has_custom_certificate: bool,
                 pending_update_count: int,
                 ip_address: Optional[str] = None,
                 last_error_date: Optional[int] = None,
                 last_error_message: Optional[str] = None,
                 last_synchronization_error_date: Optional[int] = None,
                 max_connections: Optional[int] = None,
                 allowed_updates: Optional[list[str]] = None):
        """
        :param url: Webhook URL, may be empty if webhook is not set up
        :param has_custom_certificate: True, if a custom certificate was provided for webhook certificate checks
        :param pending_update_count: Number of updates awaiting delivery
        :param ip_address: Currently used webhook IP address
        :param last_error_date: Unix time for the most recent error that happened when trying to deliver an update via webhook
        :param last_error_message: Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook
        :param last_synchronization_error_date: Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters
        :param max_connections: Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters
        :param allowed_updates: A list of update types the bot is subscribed to. Defaults to all update types except chat_member
        """
        self.url = url
        self.has_custom_certificate = has_custom_certificate
        self.pending_update_count = pending_update_count
        self.ip_address = ip_address
        self.last_error_date = last_error_date
        self.last_error_message = last_error_message
        self.last_synchronization_error_date = last_synchronization_error_date
        self.max_connections = max_connections
        self.allowed_updates = allowed_updates
