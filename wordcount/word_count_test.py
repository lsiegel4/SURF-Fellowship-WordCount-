"""Testing word_count."""

__author__ = "730478722"

from projects.wordcount.word_count import word_count


def test_word_count_empty() -> None:
    """Tests the function word count with the empty string."""
    text: str = " "
    assert word_count(text) == {}


def test_word_count_one_word() -> None:
    """Tests the function word count with one word."""
    text: str = "hello."
    assert word_count(text) == {'hello': 1}


def test_word_count_one_word_mult_times() -> None:
    """Tests the function word count with one word repeated multiple times."""
    text: str = "hello hello hello hello."
    assert word_count(text) == {'hello': 4}


def test_word_count_mult_words() -> None:
    """Tests the function word count with multiple words."""
    text: str = "hello world, it is me."
    assert word_count(text) == {'hello': 1, 'world': 1, 'it': 1, 'is': 1, 'me': 1}


def test_word_count_mult_words_mult_times() -> None:
    """Tests the function word count with multiple words used multiple times."""
    text: str = "Wake me up, oh wake me up! wake me up up up! She's a beauty."
    assert word_count(text) == {'wake': 3, 'me': 3, 'up': 5, 'oh': 1, 'she\'s': 1, 'a': 1, 'beauty': 1}