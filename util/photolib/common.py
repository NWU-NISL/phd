"""Utility functions."""
import hashlib
import re

from labm8.py import app

FLAGS = app.FLAGS

# The top level photolib directories.
TOP_LEVEL_DIRS = set(["photos", "third_party", "lightroom"])

KNOWN_IMG_FILE_EXTENSIONS = set([".dng", ".jpg", ".png", ".tif"])

KNOWN_MOVIE_FILE_EXTENSIONS = set([".mov", ".mp4", ".m4v"])

# The set of all valid content file extensions.
KNOWN_FILE_EXTENSIONS = KNOWN_IMG_FILE_EXTENSIONS.union(
  KNOWN_MOVIE_FILE_EXTENSIONS
)

# A mapping from "bad" file extension to suggested file extension.
FILE_EXTENSION_SUGGESTIONS = {
  ".psd": ".tif",
  ".raf": ".dng",
  ".jpeg": ".jpg",
}

IGNORE_FILE_NAME = ".ignore"

# Files which are not linted.
IGNORED_FILES = set(
  [
    IGNORE_FILE_NAME,
    "autorun.inf",
    ".DS_Store",
    ".VolumeIcon.icns",
    ".VolumeIcon.ico",
    ".com.apple.timemachine.donotpresent",
    "README.md",
    ".sync_timestamp.txt",
  ]
)

# Directories which are not linted. The contents of ignored
# directories are not traversed.
IGNORED_DIRS = set([".tmp.drivedownload",])

PHOTO_LIB_PATH_COMPONENTS_RE = re.compile(
  r"(?P<year>(1\d|20)\d\d)(?P<month>(0[1-9]|1[012]))(?P<day>(0[1-9]|[12]\d|3[012]))T"
  r"(?P<hour>([01]\d|2[01234]))(?P<min>[0-5]\d)(?P<sec>[0-5]\d)(?P<seq>-\d+)?"
  r"(-(?P<modifier>Edit|HDR|Pano)(-\d+)?)*$"
)

PHOTO_LIB_SCAN_PATH_COMPONENTS_RE = re.compile(
  r"(?P<year>\d\d)(?P<month>(0[1-9]|1[012]))(?P<day>([012]\d|3[012]))"
  r"(?P<roll>[A-Z]+)-(?P<exposure>\d\d)(?P<seq>-\d+)?"
  r"(-(?P<modifier>Edit|HDR|Pano)(-\d+)?)*$"
)

PHOTOLIB_LEAF_DIR_RE = re.compile(
  r"//photos/\d\d\d\d/\d\d\d\d-\d\d/\d\d\d\d-\d\d-\d\d"
)

COMPOSITE_FILE_NAME_SUFFIXES = {"HDR", "Pano", "Edit"}


def Md5String(string: str) -> hashlib.md5:
  """
  Compute md5sum of string.

  This function returns the hash instance. The 16 byte binary string can be
  obtained using .digest(), or the 40 character hex representation using
  .hexdigest().

  Args:
    string: String to md5sum.

  Returns:
    Returns the hash instance.
  """
  md5_ = hashlib.md5()
  md5_.update(string.encode("utf-8"))
  return md5_
