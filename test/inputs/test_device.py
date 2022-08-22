"""
Tests for `snacker_tracker_scanner` module.
"""
import pytest
from unittest import mock

from snacker_tracker_scanner.inputs.device import EVDecoder

from dataclasses import dataclass

@dataclass
class InputEvent:
    # NOT ASCII, but kinda
    scancode: int

    # Wether the key is pressed (key down vs key up)
    keystate: int

class TestEVDecoder():
    def test_it_ignores_keyup_events(self):
        d = EVDecoder()
        d.add(InputEvent(2, 0))
        assert(d.buffer == [])

    def test_it_adds_things_to_the_buffer(self):
        d = EVDecoder()
        d.add(InputEvent(2, 1))
        assert(d.buffer == ['1'])

    def test_it_adds_the_alternate_when_caps_is_on(self):
        d = EVDecoder()

        d.add(InputEvent(42, 1))
        d.add(InputEvent(2, 1))

        assert(d.buffer == ['!'])

    def test_it_returns_none_prior_to_end_sequence(self):
        d = EVDecoder()

        assert(d.add(InputEvent(2, 1)) is None)

    def test_it_returns_the_content_of_buffer_on_ENTER(self):
        d = EVDecoder()

        d.buffer = ['h','e','l','l','o']

        assert(d.add(InputEvent(28, 1)) == 'hello')

    def test_it_empties_the_buffer_after_returning_it(self):
        d = EVDecoder()

        d.buffer = ['h','e','l','l','o']

        d.add(InputEvent(28, 1))
        assert(d.buffer == [])
