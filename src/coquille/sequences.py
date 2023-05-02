"""
# ANSI Escape Sequences

## Disclaimer

It is most likely not to be exhaustive -- if you have knowledge about
missing sequences, please contribute by adding them to the project.

## Sources

The sequences are mostly based on the ANSI escape code Wikipedia page:
<https://en.m.wikipedia.org/wiki/ANSI_escape_code>

Some are also taken from Microsoft documentation:
<https://learn.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences>

## Bracket notation

- [U] = the abbreviation was made up for convenience.
- [RS] = rarely (never, basically) supported.
"""
from typing import Literal
from typing import NewType


# Constants

CHAR_ESC = "\u001b"

CURSOR_VISIBILITY = 25
FOCUS_REPORT = 1004
ALT_SCREEN_BUFFER = 1049
BRACKETED_PASTE_MODE = 2004

FOREGROUND_CODE = 30
BACKGROUND_CODE = 40
UNDERLINE_CODE = 50
RESET = 9


# Helper types
EscapeSequence = NewType("EscapeSequence", str)
AltFontNumber = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]


def escape_sequence(
    code: str,
    subcode: str | None = None,
    *args: int,
) -> EscapeSequence:
    r"""
    Generate an escape sequence string.

    ## Shape:

    ```
    \u001b  [  38;2;255;127;0  m
      ↑     ↑  \____________/   ↖ subcode
     ESC  code      args
    ```
    """

    _code: str = code
    _subcode: str = subcode or ""
    _args: str = ";".join(map(str, args))

    # \u001b  [  38;2;255;127;0  m
    #   ↑     ↑  ~~~~~~~~~~~~~~   ↖ subcode
    #  ESC  code      args
    return EscapeSequence(CHAR_ESC + _code + _args + _subcode)


# alias
ESC = escape_sequence

# *- Fe -* #


def single_shift_two() -> EscapeSequence:
    return ESC("N")


def single_shift_three() -> EscapeSequence:
    return ESC("O")


def device_control_string() -> EscapeSequence:
    return ESC("P")


def control_sequence_introducer(subcode: str, *args: int) -> EscapeSequence:
    return ESC("[", subcode, *args)


def string_terminator() -> EscapeSequence:
    return ESC("\\")


def operating_system_command() -> EscapeSequence:
    return ESC("]")


def start_of_string() -> EscapeSequence:
    return ESC("X")


def privacy_message() -> EscapeSequence:
    return ESC("^")


def application_program_command() -> EscapeSequence:
    return ESC("_")


# aliases
SS2 = single_shift_two
SS3 = single_shift_three
DCS = device_control_string
CSI = control_sequence_introducer
ST = string_terminator
OSC = operating_system_command
SOS = start_of_string
PM = privacy_message
APC = application_program_command


# helper functions
def _CSI_private(subcode: str, *args: int) -> EscapeSequence:
    return ESC("[?", subcode, *args)


# *- FS -* #


reset_initial_state = ESC("c")


# alias
RIS = reset_initial_state


# *- Fp -* #


DEC_save_cursor = ESC("7")
DEC_restore_cursor = ESC("8")


# aliases
DECSC = DEC_save_cursor
DECRC = DEC_restore_cursor


# *- CSI-based sequences -* #


# helper functions
def _AUX_port(n: int) -> EscapeSequence:
    return CSI("i", n)


def _enable_CSI(*args: int) -> EscapeSequence:
    return _CSI_private("h", *args)


def _disable_CSI(*args: int) -> EscapeSequence:
    return _CSI_private("l", *args)


def cursor_shape(n: int) -> EscapeSequence:
    return EscapeSequence(CHAR_ESC + f"[{n} q")


# sequences
def cursor_up(n: int = 1) -> EscapeSequence:
    return CSI("A", n)


def cursor_down(n: int = 1) -> EscapeSequence:
    return CSI("B", n)


def cursor_forward(n: int = 1) -> EscapeSequence:
    return CSI("C", n)


def cursor_back(n: int = 1) -> EscapeSequence:
    return CSI("D", n)


def cursor_next_line(n: int = 1) -> EscapeSequence:
    return CSI("E", n)


def cursor_previous_line(n: int = 1) -> EscapeSequence:
    return CSI("F", n)


def cursor_horizontal_absolute(n: int = 1) -> EscapeSequence:
    return CSI("G", n)


def cursor_position(n: int = 1, m: int = 1) -> EscapeSequence:
    return CSI("H", n, m)


def erase_in_display(n: int) -> EscapeSequence:
    return CSI("J", n)


def erase_in_line(n: int) -> EscapeSequence:
    return CSI("K", n)


def scroll_up(n: int = 1) -> EscapeSequence:
    return CSI("S", n)


def scroll_down(n: int = 1) -> EscapeSequence:
    return CSI("T", n)


def horizontal_vertical_position(n: int = 1, m: int = 1) -> EscapeSequence:
    return CSI("f", n, m)


def select_graphical_rendition(*args: int) -> EscapeSequence:
    return CSI("m", *args)


def numpad(n: int) -> EscapeSequence:
    return CSI("~", n)


AUX_port_on = _AUX_port(5)
AUX_port_off = _AUX_port(4)
device_status_report = CSI("n", 6)
save_current_cursor_position = CSI("s")
restore_current_cursor_position = CSI("u")
show_cursor = _enable_CSI(CURSOR_VISIBILITY)
hide_cursor = _disable_CSI(CURSOR_VISIBILITY)
enable_focus_report = _enable_CSI(FOCUS_REPORT)
disable_focus_report = _disable_CSI(FOCUS_REPORT)
enable_alternative_screen_buffer = _enable_CSI(ALT_SCREEN_BUFFER)
disable_alternative_screen_buffer = _disable_CSI(ALT_SCREEN_BUFFER)
enable_bracketed_paste_mode = _enable_CSI(BRACKETED_PASTE_MODE)
disable_bracketed_paste_mode = _disable_CSI(BRACKETED_PASTE_MODE)


# *- Cursor shapes -* #

user_defined_cursor_shape = cursor_shape(0)
blinking_block_cursor_shape = cursor_shape(1)
steady_block_cursor_shape = cursor_shape(2)
blinking_underline_cursor_shape = cursor_shape(3)
steady_underline_cursor_shape = cursor_shape(4)
blinking_bar_cursor_shape = cursor_shape(5)
steady_bar_cursor_shape = cursor_shape(6)


# aliases
CUU = cursor_up
CUD = cursor_down
CUF = cursor_forward
CUB = cursor_back
CNL = cursor_next_line
CPL = cursor_previous_line
CHA = cursor_horizontal_absolute
CUP = cursor_position
ED = erase_in_display
EL = erase_in_line
SU = scroll_up
SD = scroll_down
HVP = horizontal_vertical_position
SGR = select_graphical_rendition
EAP = AUX_port_off  # Enable Aux Port [U]
DAP = AUX_port_off  # Disable Aux Port [U]
DSR = device_status_report
SCP = SCOSC = save_current_cursor_position
RCP = SCORC = restore_current_cursor_position
ECV = show_cursor  # Enable Cursor Visibility  [U]
DCV = hide_cursor  # Disable Cursor Visibility [U]
EFR = enable_focus_report  # [U]
DFR = disable_focus_report  # [U]
EASB = enable_alternative_screen_buffer  # [U]
DASB = disable_alternative_screen_buffer  # [U]
EBPM = enable_bracketed_paste_mode  # [U]
DBPM = disable_bracketed_paste_mode  # [U]
UDFCS = user_defined_cursor_shape  # [U]
BBLCS = blinking_block_cursor_shape  # [U]
SBLCS = steady_block_cursor_shape  # [U]
BULCS = blinking_underline_cursor_shape  # [U]
SULCS = steady_underline_cursor_shape  # [U]
BBRCS = blinking_bar_cursor_shape  # [U]
SBRCS = steady_bar_cursor_shape  # [U]


# *- SGR-based sequences -* #


reset = SGR(0)
bold = SGR(1)
faint = SGR(2)
italic = SGR(3)
underline = SGR(4)
slow_blink = SGR(5)
rapid_blink = SGR(6)
invert = SGR(7)
conceal = SGR(8)  # = hide
crossed_out = SGR(9)
primary_font = SGR(10)


def alternative_font(n: AltFontNumber) -> EscapeSequence:
    return SGR(n + 10)


fraktur = SGR(20)  # [RS]
double_underline = SGR(21)  # THIS MIGHT DISABLE BOLD ON SOME TERMINALS
normal_intensity = SGR(22)
no_italic = SGR(23)
no_underline = SGR(24)  # Also disables double underline
no_blink = SGR(25)  # Disables both blinks
proportional_spacing = SGR(26)
no_invert = SGR(27)
no_conceal = SGR(28)  # = reveal
not_crossed_out = SGR(29)


def foreground_color(n: int) -> EscapeSequence:
    return SGR(FOREGROUND_CODE + 8, 5, n)


def foreground_truecolor(r: int, g: int, b: int) -> EscapeSequence:
    return SGR(FOREGROUND_CODE + 8, 2, r, g, b)


default_foreground_color = SGR(FOREGROUND_CODE + RESET)


def background_color(n: int) -> EscapeSequence:
    return SGR(BACKGROUND_CODE + 8, 5, n)


def background_truecolor(r: int, g: int, b: int) -> EscapeSequence:
    return SGR(BACKGROUND_CODE + 8, 2, r, g, b)


default_background_color = SGR(BACKGROUND_CODE + RESET)


no_proportional_spacing = SGR(50)
framed = SGR(51)
encircled = SGR(52)
overlined = SGR(53)
not_framed_encircled = SGR(54)
not_overlined = SGR(55)


def underline_color(n: int) -> EscapeSequence:  # NOT STANDARD
    return SGR(UNDERLINE_CODE + 8, 5, n)


def underline_truecolor(r: int, g: int, b: int) -> EscapeSequence:  # NOT STANDARD
    return SGR(UNDERLINE_CODE + 8, 2, r, g, b)


default_underline_color = SGR(UNDERLINE_CODE + RESET)  # NOT STANDARD
ideogram_underline = SGR(60)  # [RS]
ideogram_double_underline = SGR(61)  # [RS]
ideogram_overline = SGR(62)  # [RS]
ideogram_double_overline = SGR(63)  # [RS]
ideogram_stress_marking = SGR(64)  # [RS]
no_ideogram = SGR(65)  # [RS]
superscript = SGR(73)  # mintty only?
subscript = SGR(74)  # mintty only?
no_superscript_subscript = SGR(75)  # mintty only?

# NOT STANDARD ↓
foreground_bright_black = SGR(90)
foreground_bright_red = SGR(91)
foreground_bright_green = SGR(92)
foreground_bright_yellow = SGR(93)
foreground_bright_blue = SGR(94)
foreground_bright_magenta = SGR(95)
foreground_bright_cyan = SGR(96)
foreground_bright_white = SGR(97)
background_bright_black = SGR(100)
background_bright_red = SGR(101)
background_bright_green = SGR(102)
background_bright_yellow = SGR(103)
background_bright_blue = SGR(104)
background_bright_magenta = SGR(105)
background_bright_cyan = SGR(106)
background_bright_white = SGR(107)

# aliases
dim = faint
hide = conceal
strikethrough = crossed_out
reveal = no_conceal
no_strikethrough = not_crossed_out
fg_color = foreground_color
fg_truecolor = foreground_truecolor
bg_color = background_color
bg_truecolor = background_truecolor
ul_color = underline_color
ul_truecolor = underline_truecolor

# convenient values
fg_black = foreground_color(0)
fg_red = foreground_color(1)
fg_green = foreground_color(2)
fg_yellow = foreground_color(3)
fg_blue = foreground_color(4)
fg_magenta = foreground_color(5)
fg_cyan = foreground_color(6)
fg_white = foreground_color(7)
bg_black = background_color(0)
bg_red = background_color(1)
bg_green = background_color(2)
bg_yellow = background_color(3)
bg_blue = background_color(4)
bg_magenta = background_color(5)
bg_cyan = background_color(6)
bg_white = background_color(7)
ul_black = underline_color(0)
ul_red = underline_color(1)
ul_green = underline_color(2)
ul_yellow = underline_color(3)
ul_blue = underline_color(4)
ul_magenta = underline_color(5)
ul_cyan = underline_color(6)
ul_white = underline_color(7)


# *- Designate character set -* #


# helpers
def DCHARSET(subcode: str) -> EscapeSequence:
    return ESC("(", subcode)


# sequences
DEC_line_drawing = DCHARSET("0")
US_ASCII = DCHARSET("B")


# *- Numpad and Fn keys -* #
insert = numpad(2)
delete = numpad(3)
page_up = numpad(5)
page_down = numpad(6)


# *- Extensions -* #

soft_reset = ESC("[!", "p")


# aliases
DECSTR = soft_reset
