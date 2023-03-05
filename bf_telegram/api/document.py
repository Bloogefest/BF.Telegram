#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Optional

from photo_size import PhotoSize

class Document:
    """
    This object represents a general file (as opposed to photos, voice messages and audio files).

    https://core.telegram.org/bots/api#document
    """

    def __init__(self,
                 file_id: str,
                 file_unique_id: str,
                 thumb: Optional[PhotoSize] = None,
                 file_name: Optional[str] = None,
                 mime_type: Optional[str] = None,
                 file_size: Optional[int] = None):
        """
        :param file_id: Identifier for this file, which can be used to download or reuse the file
        :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        :param thumb: Document thumbnail as defined by sender
        :param file_name: Original filename as defined by sender
        :param mime_type: MIME type of the file as defined by sender
        :param file_size: File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
        """
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
