from io import StringIO

import pytest
from coquille.coquille import *
from coquille.sequences import DEC_save_cursor
from coquille.sequences import erase_in_display
from coquille.sequences import select_graphical_rendition
from coquille.sequences import start_of_string


@pytest.mark.parametrize(
    ["args", "output"],
    [
        ((DEC_save_cursor,), DEC_save_cursor),
        ((start_of_string,), "\u001bX"),
        ((erase_in_display, 2), "\u001b[2J"),
        ((select_graphical_rendition, 38, 5, 16), "\x1b[38;5;16m"),
    ],
)
def test_prepare(args, output):
    assert prepare(*args) == output


@pytest.mark.parametrize(
    ["sequence", "args", "output"],
    [
        (DEC_save_cursor, (), DEC_save_cursor),
        (start_of_string, (), "\u001bX"),
        (erase_in_display, (2,), "\u001b[2J"),
        (select_graphical_rendition, (38, 5, 16), "\x1b[38;5;16m"),
    ],
)
def test_apply(sequence, args, output):
    file = StringIO()
    apply(sequence, file, *args)
    assert file.getvalue() == output


# TODO: test_ContextCoquille_*
# TODO: test_Coquille_*
