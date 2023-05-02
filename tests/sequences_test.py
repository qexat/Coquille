import pytest
from coquille.sequences import *


@pytest.mark.parametrize(
    ["args", "result"],
    [
        (("N"), "\u001bN"),  # code only
        (("[", "i"), "\u001b[i"),  # code + subcode
        (("[", "m", 1), "\u001b[1m"),  # code, subcode, 1 arg
        (
            ("[", "m", 38, 2, 255, 127, 0),
            "\u001b[38;2;255;127;0m",
        ),  # code, subcode, n-args
    ],
)
def test_escape_sequence(args, result):
    assert escape_sequence(*args) == result


def test_single_shift_two():
    assert single_shift_two() == "\u001bN"


def test_single_shift_three():
    assert single_shift_three() == "\u001bO"


def test_device_control_string():
    assert device_control_string() == "\u001bP"


def test_string_terminator():
    assert string_terminator() == "\u001b\\"


def test_operating_system_command():
    assert operating_system_command() == "\u001b]"


def test_start_of_string():
    assert start_of_string() == "\u001bX"


def test_privacy_message():
    assert privacy_message() == "\u001b^"


def test_application_program_command():
    assert application_program_command() == "\u001b_"


def test_cursor_shape():
    assert cursor_shape(0) == "\u001b[0 q"


@pytest.mark.parametrize(
    ["args", "output"],
    [
        ((), "\u001b[1A"),
        ((3,), "\u001b[3A"),
    ],
)
def test_cursor_up(args, output):
    assert cursor_up(*args) == output


@pytest.mark.parametrize(
    ["args", "output"],
    [
        ((), "\u001b[1B"),
        ((3,), "\u001b[3B"),
    ],
)
def test_cursor_down(args, output):
    assert cursor_down(*args) == output


@pytest.mark.parametrize(
    ["args", "output"],
    [
        ((), "\u001b[1C"),
        ((3,), "\u001b[3C"),
    ],
)
def test_cursor_forward(args, output):
    assert cursor_forward(*args) == output


@pytest.mark.parametrize(
    ["args", "output"],
    [
        ((), "\u001b[1D"),
        ((3,), "\u001b[3D"),
    ],
)
def test_cursor_back(args, output):
    assert cursor_back(*args) == output


@pytest.mark.parametrize(
    ["args", "output"],
    [
        ((), "\u001b[1E"),
        ((3,), "\u001b[3E"),
    ],
)
def test_cursor_next_line(args, output):
    assert cursor_next_line(*args) == output


@pytest.mark.parametrize(
    ["args", "output"],
    [
        ((), "\u001b[1F"),
        ((3,), "\u001b[3F"),
    ],
)
def test_cursor_previous_line(args, output):
    assert cursor_previous_line(*args) == output


@pytest.mark.parametrize(
    ["args", "output"],
    [
        ((), "\u001b[1G"),
        ((3,), "\u001b[3G"),
    ],
)
def test_cursor_horizontal_absolute(args, output):
    assert cursor_horizontal_absolute(*args) == output


@pytest.mark.parametrize(
    ["kwargs", "output"],
    [
        ({}, "\u001b[1;1H"),
        ({"n": 3}, "\u001b[3;1H"),
        ({"m": 3}, "\u001b[1;3H"),
        ({"n": 3, "m": 3}, "\u001b[3;3H"),
    ],
)
def test_cursor_position(kwargs, output):
    assert cursor_position(**kwargs) == output


def test_erase_in_display():
    assert erase_in_display(1) == "\u001b[1J"


def test_erase_in_line():
    assert erase_in_line(1) == "\u001b[1K"


@pytest.mark.parametrize(
    ["args", "output"],
    [
        ((), "\u001b[1S"),
        ((3,), "\u001b[3S"),
    ],
)
def test_scroll_up(args, output):
    assert scroll_up(*args) == output


@pytest.mark.parametrize(
    ["args", "output"],
    [
        ((), "\u001b[1T"),
        ((3,), "\u001b[3T"),
    ],
)
def test_scroll_down(args, output):
    assert scroll_down(*args) == output


@pytest.mark.parametrize(
    ["kwargs", "output"],
    [
        ({}, "\u001b[1;1f"),
        ({"n": 3}, "\u001b[3;1f"),
        ({"n": 3, "m": 4}, "\u001b[3;4f"),
        ({"m": 4}, "\u001b[1;4f"),
    ],
)
def test_horizontal_vertical_position(kwargs, output):
    assert horizontal_vertical_position(**kwargs) == output


def test_alternative_font():
    assert alternative_font(1) == "\x1b[11m"


def test_foreground_truecolor():
    assert foreground_truecolor(255, 255, 255) == "\x1b[38;2;255;255;255m"


def test_background_truecolor():
    assert background_truecolor(255, 255, 255) == "\x1b[48;2;255;255;255m"


def test_underline_truecolor():
    assert underline_truecolor(255, 255, 255) == "\x1b[58;2;255;255;255m"
