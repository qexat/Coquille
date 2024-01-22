import typing

CHAR_ESC: str

CURSOR_VISIBILITY: int
FOCUS_REPORT: int
ALT_SCREEN_BUFFER: int
BRACKETED_PASTE_MODE: int

FOREGROUND_CODE: int
BACKGROUND_CODE: int
UNDERLINE_CODE: int
RESET: int

# Helper types
EscapeSequenceName: typing.TypeAlias = str
AltFontNumber: typing.TypeAlias = typing.Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]

class EscapeSequence(str):
    pass

def escape_sequence(
    code: str,
    subcode: str | None = None,
    *args: int,
) -> EscapeSequence:
    pass

ESC = escape_sequence

def single_shift_two() -> EscapeSequence: ...
def single_shift_three() -> EscapeSequence: ...
def device_control_string() -> EscapeSequence: ...
def control_sequence_introducer(subcode: str, *args: int) -> EscapeSequence: ...
def string_terminator() -> EscapeSequence: ...
def operating_system_command() -> EscapeSequence: ...
def start_of_string() -> EscapeSequence: ...
def privacy_message() -> EscapeSequence: ...
def application_program_command() -> EscapeSequence: ...

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

# *- FS -* #

reset_initial_state: EscapeSequence

# alias
RIS: EscapeSequence

# *- Fp -* #

DEC_save_cursor: EscapeSequence
DEC_restore_cursor: EscapeSequence

# aliases
DECSC: EscapeSequence
DECRC: EscapeSequence

# *- CSI-based sequences -* #

# helper functions
def _AUX_port(n: int) -> EscapeSequence: ...
def _enable_CSI(*args: int) -> EscapeSequence: ...
def _disable_CSI(*args: int) -> EscapeSequence: ...
def cursor_shape(n: int) -> EscapeSequence: ...

# sequences
def cursor_up(n: int = 1) -> EscapeSequence: ...
def cursor_down(n: int = 1) -> EscapeSequence: ...
def cursor_forward(n: int = 1) -> EscapeSequence: ...
def cursor_back(n: int = 1) -> EscapeSequence: ...
def cursor_next_line(n: int = 1) -> EscapeSequence: ...
def cursor_previous_line(n: int = 1) -> EscapeSequence: ...
def cursor_horizontal_absolute(n: int = 1) -> EscapeSequence: ...
def cursor_position(n: int = 1, m: int = 1) -> EscapeSequence: ...
def erase_in_display(n: int) -> EscapeSequence: ...
def erase_in_line(n: int) -> EscapeSequence: ...
def scroll_up(n: int = 1) -> EscapeSequence: ...
def scroll_down(n: int = 1) -> EscapeSequence: ...
def horizontal_vertical_position(n: int = 1, m: int = 1) -> EscapeSequence: ...
def select_graphical_rendition(*args: int) -> EscapeSequence: ...
def numpad(n: int) -> EscapeSequence: ...

AUX_port_on: EscapeSequence
AUX_port_off: EscapeSequence
device_status_report: EscapeSequence
save_current_cursor_position: EscapeSequence
restore_current_cursor_position: EscapeSequence
show_cursor: EscapeSequence
hide_cursor: EscapeSequence
enable_focus_report: EscapeSequence
disable_focus_report: EscapeSequence
enable_alternative_screen_buffer: EscapeSequence
disable_alternative_screen_buffer: EscapeSequence
enable_bracketed_paste_mode: EscapeSequence
disable_bracketed_paste_mode: EscapeSequence

# *- Cursor shapes -* #

user_defined_cursor_shape: EscapeSequence
blinking_block_cursor_shape: EscapeSequence
steady_block_cursor_shape: EscapeSequence
blinking_underline_cursor_shape: EscapeSequence
steady_underline_cursor_shape: EscapeSequence
blinking_bar_cursor_shape: EscapeSequence
steady_bar_cursor_shape: EscapeSequence

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
EAP: EscapeSequence  # Enable Aux Port [U]
DAP: EscapeSequence  # Disable Aux Port [U]
DSR: EscapeSequence
SCP: EscapeSequence
SCOSC: EscapeSequence
RCP: EscapeSequence
SCORC: EscapeSequence
ECV: EscapeSequence  # Enable Cursor Visibility  [U]
DCV: EscapeSequence  # Disable Cursor Visibility [U]
EFR: EscapeSequence  # [U]
DFR: EscapeSequence  # [U]
EASB: EscapeSequence  # [U]
DASB: EscapeSequence  # [U]
EBPM: EscapeSequence  # [U]
DBPM: EscapeSequence  # [U]
UDFCS: EscapeSequence  # [U]
BBLCS: EscapeSequence  # [U]
SBLCS: EscapeSequence  # [U]
BULCS: EscapeSequence  # [U]
SULCS: EscapeSequence  # [U]
BBRCS: EscapeSequence  # [U]
SBRCS: EscapeSequence  # [U]

# *- SGR-based sequences -* #

reset: EscapeSequence
bold: EscapeSequence
faint: EscapeSequence
italic: EscapeSequence
underline: EscapeSequence
slow_blink: EscapeSequence
rapid_blink: EscapeSequence
invert: EscapeSequence
conceal: EscapeSequence  # = hide
crossed_out: EscapeSequence
primary_font: EscapeSequence

def alternative_font(n: AltFontNumber) -> EscapeSequence: ...

fraktur: EscapeSequence  # [RS]
double_underline: EscapeSequence  # THIS MIGHT DISABLE BOLD ON SOME TERMINALS
normal_intensity: EscapeSequence
no_italic: EscapeSequence
no_underline: EscapeSequence  # Also disables double underline
no_blink: EscapeSequence  # Disables both blinks
proportional_spacing: EscapeSequence
no_invert: EscapeSequence
no_conceal: EscapeSequence  # = reveal
not_crossed_out: EscapeSequence

def foreground_color(n: int) -> EscapeSequence: ...
def foreground_truecolor(r: int, g: int, b: int) -> EscapeSequence: ...

default_foreground_color: EscapeSequence

def background_color(n: int) -> EscapeSequence: ...
def background_truecolor(r: int, g: int, b: int) -> EscapeSequence: ...

default_background_color: EscapeSequence

no_proportional_spacing: EscapeSequence
framed: EscapeSequence
encircled: EscapeSequence
overlined: EscapeSequence
not_framed_encircled: EscapeSequence
not_overlined: EscapeSequence

def underline_color(n: int) -> EscapeSequence:  # NOT STANDARD
    ...
def underline_truecolor(r: int, g: int, b: int) -> EscapeSequence:  # NOT STANDARD
    ...

default_underline_color: EscapeSequence  # NOT STANDARD
ideogram_underline: EscapeSequence  # [RS]
ideogram_double_underline: EscapeSequence  # [RS]
ideogram_overline: EscapeSequence  # [RS]
ideogram_double_overline: EscapeSequence  # [RS]
ideogram_stress_marking: EscapeSequence  # [RS]
no_ideogram: EscapeSequence  # [RS]
superscript: EscapeSequence  # mintty only?
subscript: EscapeSequence  # mintty only?
no_superscript_subscript: EscapeSequence  # mintty only?

# NOT STANDARD ↓
foreground_bright_black: EscapeSequence
foreground_bright_red: EscapeSequence
foreground_bright_green: EscapeSequence
foreground_bright_yellow: EscapeSequence
foreground_bright_blue: EscapeSequence
foreground_bright_magenta: EscapeSequence
foreground_bright_cyan: EscapeSequence
foreground_bright_white: EscapeSequence
background_bright_black: EscapeSequence
background_bright_red: EscapeSequence
background_bright_green: EscapeSequence
background_bright_yellow: EscapeSequence
background_bright_blue: EscapeSequence
background_bright_magenta: EscapeSequence
background_bright_cyan: EscapeSequence
background_bright_white: EscapeSequence

# aliases
dim: EscapeSequence
hide: EscapeSequence
strikethrough: EscapeSequence
reveal: EscapeSequence
no_strikethrough: EscapeSequence
fg_color = foreground_color
fg_truecolor = foreground_truecolor
bg_color = background_color
bg_truecolor = background_truecolor
ul_color = underline_color
ul_truecolor = underline_truecolor

# convenient values
fg_black: EscapeSequence
fg_red: EscapeSequence
fg_green: EscapeSequence
fg_yellow: EscapeSequence
fg_blue: EscapeSequence
fg_magenta: EscapeSequence
fg_cyan: EscapeSequence
fg_white: EscapeSequence
bg_black: EscapeSequence
bg_red: EscapeSequence
bg_green: EscapeSequence
bg_yellow: EscapeSequence
bg_blue: EscapeSequence
bg_magenta: EscapeSequence
bg_cyan: EscapeSequence
bg_white: EscapeSequence
ul_black: EscapeSequence
ul_red: EscapeSequence
ul_green: EscapeSequence
ul_yellow: EscapeSequence
ul_blue: EscapeSequence
ul_magenta: EscapeSequence
ul_cyan: EscapeSequence
ul_white: EscapeSequence

# *- Designate character set -* #

# helpers
def DCHARSET(subcode: str) -> EscapeSequence: ...

# sequences
DEC_line_drawing: EscapeSequence
US_ASCII: EscapeSequence

# *- Numpad and Fn keys -* #
insert: EscapeSequence
delete: EscapeSequence
page_up: EscapeSequence
page_down: EscapeSequence

# *- Extensions -* #

soft_reset: EscapeSequence

# aliases
DECSTR: EscapeSequence

def get_sequence_from_name(name: str) -> EscapeSequence: ...
