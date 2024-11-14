import os
from typing import Dict, List
from unittest import TestCase
from unittest.mock import Mock

from merger.merger import Merger


class CallRecoder():
    _write_calls_records: List[List] = []

    def __init__(self) -> None:
        self._write_calls_records = []

    def record(self, *args):
        call_args = []
        for arg in args:
            call_args.append(arg)
        self._write_calls_records.append(call_args)

    def get_record(self):
        return self._write_calls_records

    def get_times_called(self):
        return len(self._write_calls_records)


class TestMerger(TestCase):

    def setUp(self) -> None:
        self._file_searcher = Mock()
        self._dir_writer = Mock()
        self._client = Mock()

    def test_should_merge_files_same_name_preserving_folders_structure(self):

        expected_dir_write_call = [
            ["./out/"],
            ["./out/first"]
        ]

        expected_client_write_calls = [
            ["./out/a.pdf"],
            ["./out/d.pdf"],
            ["./out/first/b.pdf"],
            ["./out/first/c.pdf"],
            ["./out/first/e.pdf"],
        ]

        expected_client_append_calls = [
            ["./a.pdf"],
            ["./a-1.pdf"],
            ["./d.pdf"],
            ["./first/b.pdf"],
            ["./first/b-1.pdf"],
            ["./first/c.pdf"],
            ["./first/c-1.pdf"],
            ["./first/e.pdf"],
        ]

        expected_client_reset_calls = 5

        self._stub_file_search_mergeable_res()

        write_call_recoder = CallRecoder()

        self._dir_writer.write.side_effect = write_call_recoder.record

        reset_call_recoder = CallRecoder()

        self._client.reset.side_effect = reset_call_recoder.record

        client_write_call_recoder = CallRecoder()

        self._client.write.side_effect = client_write_call_recoder.record

        client_append_call_recoder = CallRecoder()

        self._client.append.side_effect = client_append_call_recoder.record

        merger = Merger(self._client, self._file_searcher, self._dir_writer)

        merger.merge_dir_tree_files(".", "./out")

        self._file_searcher.search_files.assert_called_with(".", "pdf")

        self.assertEqual(expected_dir_write_call,
                         write_call_recoder.get_record())

        self.assertEqual(expected_client_append_calls,
                         client_append_call_recoder.get_record())

        self.assertEqual(expected_client_write_calls,
                         client_write_call_recoder.get_record())

        self.assertEqual(expected_client_reset_calls,
                         reset_call_recoder.get_times_called())

    # stubs defs

    def _stub_file_search_mergeable_res(self):
        def search_files_success_result(path: str, ext: str) -> Dict[str, List[str]]:
            return {
                ".": ["./a.pdf", "./a-1.pdf", "./d.pdf"],
                "./first": ["./first/b.pdf", "./first/c.pdf", "./first/b-1.pdf", "./first/c-1.pdf", "./first/e.pdf"],
            }

        self._file_searcher.search_files.side_effect = search_files_success_result
