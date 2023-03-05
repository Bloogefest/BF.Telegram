#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Optional

from photo_size import PhotoSize

class Audio:
    """
    This object represents an audio file to be treated as music by the Telegram clients.

    https://core.telegram.org/bots/api#audio
    """

    def __init__(self,
                 file_id: str,
                 file_unique_id: str,
                 duration: int,
                 performer: Optional[str] = None,
                 title: Optional[str] = None,
                 file_name: Optional[str] = None,
                 mime_type: Optional[str] = None,
                 file_size: Optional[int] = None,
                 thumb: Optional[PhotoSize] = None):
        """
        :param file_id: Identifier for this file, which can be used to download or reuse the file
        :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        :param duration: Duration of the audio in seconds as defined by sender
        :param performer: Performer of the audio as defined by sender or by audio tags
        :param title: Title of the audio as defined by sender or by audio tags
        :param file_name: Original filename as defined by sender
        :param mime_type: MIME type of the file as defined by sender
        :param file_size: File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
        :param thumb: Thumbnail of the album cover to which the music file belongs
        """
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumb = thumb
