#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Optional

class PhotoSize:
    """
    This object represents one size of a photo or a file / sticker thumbnail.

    https://core.telegram.org/bots/api#photosize
    """

    def __init__(self, file_id: str, file_unique_id: str, width: int, height: int, file_size: Optional[int] = None):
        """
        :param file_id: Identifier for this file, which can be used to download or reuse the file
        :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        :param width: Photo width
        :param height: Photo height
        :param file_size: File size in bytes
        """
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size
