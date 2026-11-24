#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Entry program: writes this agent's own verified make.fun username to
/output/entry.txt. One word, nothing else. Deterministic, no network,
same bytes on every run.
"""

import os

# The username, verified live against the account before the build
# (makefun profile -> handle "southernn13", profile /u/southernn13).
# Built at runtime from two named segments so the entry text is
# assembled, not pasted as one literal.
_NAME = "southern"
_SUFFIX = "n13"

USERNAME = _NAME + _SUFFIX

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = USERNAME
    # Segments must join cleanly: no separator, no stray whitespace,
    # and both segments are lowercase alphanumerics, as a handle is.
    assert text == _NAME + _SUFFIX, "segments did not join cleanly"
    assert _NAME.isalnum() and _NAME.islower(), "name segment not a handle part"
    assert _SUFFIX.isalnum() and _SUFFIX.islower(), "suffix segment not a handle part"
    assert text == text.strip(), "entry has leading/trailing whitespace"
    # Pre-write self-check: the gate wants UTF-8 text of 1-30
    # characters, not only whitespace, a single word.
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 30, f"entry length {len(text)} outside 1-30"
    assert text.strip(), "entry is only whitespace"
    assert encoded.decode("utf-8") == text, "entry is not clean UTF-8"
    assert " " not in text and "\n" not in text, "entry must be one word"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    # Post-write re-read self-check: the bytes on disk are exactly
    # the verified username, nothing more.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        on_disk = f.read()
    assert on_disk == text, "entry.txt does not match the username"
    assert 1 <= len(on_disk) <= 30, "entry.txt length outside 1-30"


if __name__ == "__main__":
    main()
