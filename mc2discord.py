def to_ansi(msg: str) -> str:
    """Converts a Minecraft message (§a, §b, §l,...) to ANSI escape codes.
    Uses discord's ansi escape codes
    """
    cursor_pos = 0
    length = len(msg)
    current_color = 37
    ansi_msg = ""
    while cursor_pos < length:
        if msg[cursor_pos] == "§":
            symbol = msg[cursor_pos + 1] if cursor_pos + 1 < length else ""
            if symbol in color_codes:
                current_color = color_codes[symbol]
                ansi_msg += f"\u001b[{current_color}m"
                cursor_pos += 1
            elif symbol in escape_codes:
                ansi_msg += f"\u001b[{escape_codes[symbol]};{current_color}m"
                cursor_pos += 1
            elif symbol in ["k", "o", "§"]:
                pass  # Ignore these
                cursor_pos += 1
            else:
                ansi_msg += "§"
        else:
            ansi_msg += msg[cursor_pos]
        cursor_pos += 1
    return ansi_msg


"""
30: Gray
31: Red
32: Green
33: Yellow
34: Blue
35: Pink
36: Cyan
37: White
"""
color_codes = {
    "0": 30,
    "1": 34,
    "2": 32,
    "3": 36,
    "4": 31,
    "5": 35,
    "6": 33,
    "7": 37,
    "8": 30,
    "9": 34,
    "a": 32,
    "b": 36,
    "c": 31,
    "d": 35,
    "e": 33,
    "f": 37,
}

escape_codes = {
    "l": 1,
    "m": 4,
    "n": 4,
    "r": 0,
}
