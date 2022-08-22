"""
Tests for `snacker_tracker_scanner` module.
"""
import pytest
from unittest import mock

from snacker_tracker_scanner.inputs.file import File


class TestFile(object):
    def test_it_reads_the_specified_file(self):
        things = ["12345","34567"]
        m = mock.mock_open(read_data = "\n".join(things))
        with mock.patch('snacker_tracker_scanner.inputs.file.open', m):
            f = File("./test/file.csv")

            list(f.events())

            m.assert_called_once_with("./test/file.csv", "r")

    def test_it_returns_one_thing_per_line(self):
        things = ["12345","34567"]
        m = mock.mock_open(read_data = "\n".join(things))
        with mock.patch('snacker_tracker_scanner.inputs.file.open', m):
            f = File("./test/file.csv")

            assert(len(list(f.events())) == 2)

    def test_it_returns_the_lines_wrapped_in_a_dict(self):
        things = ["12345","34567"]
        m = mock.mock_open(read_data = "\n".join(things))
        with mock.patch('snacker_tracker_scanner.inputs.file.open', m):
            f = File("./test/file.csv")

            returned_things = list(f.events())

            assert(returned_things == [{"code": thing} for thing in things])
