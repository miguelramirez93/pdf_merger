from typing import List
from unittest import TestCase
from unittest.mock import Mock

from dir.searcher import Searcher


class TestSearcher(TestCase):

    _expectedFolderLs: List[str] = ["first", "other.md", "a.pdf"]
    _expectedFilesLs: List[str] = ["b.pdf", "c.pdf"]

    def setUp(self) -> None:
        self._mocked_reader = Mock()

    def test_search_files_multi_path_result(self):

        self._stub_expected_folder_tree()

        searcher = Searcher(self._mocked_reader)

        res = searcher.search_files(".", "pdf")

        self.assertEqual(res, {
            ".": ["./a.pdf"],
            "./first": ["./first/b.pdf", "./first/c.pdf"],
        })

    def test_search_files_single_path_result(self):

        self._stub_expected_folder_tree()

        searcher = Searcher(self._mocked_reader)

        res = searcher.search_files(".", "md")

        self.assertEqual(res, {
            ".": ["./other.md"],
        })

        res = searcher.search_files(".", "not_exist")

        self.assertEqual(res, {})

    def test_search_files_no_results(self):

        self._stub_expected_folder_tree()

        searcher = Searcher(self._mocked_reader)

        res = searcher.search_files(".", "not_exist")

        self.assertEqual(res, {})

    def _stub_expected_folder_tree(self):
        def list_elements_side_effect(path: str) -> List[str]:
            if path == "./first":
                return self._expectedFilesLs
            return self._expectedFolderLs

        self._mocked_reader.list_elements.side_effect = list_elements_side_effect

        def is_dir_side_effect(target: str) -> bool:
            return target == "./first"

        self._mocked_reader.is_dir.side_effect = is_dir_side_effect
