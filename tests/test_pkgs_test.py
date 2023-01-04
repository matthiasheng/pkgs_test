import pytest
import matplotlib
from pkgs_test import pkgs_test
from pkgs_test import plotting
from collections import Counter
from pkgs_test.datasets import get_flatland


@pytest.fixture
def einstein_counts():
    return Counter({'insanity': 1, 'is': 1, 'doing': 1,
                    'the': 1, 'same': 1, 'thing': 1,
                    'over': 2, 'and': 2, 'expecting': 1,
                    'different': 1, 'results': 1})


def test_count_words(einstein_counts):
    """Test word counting from a file."""
    expected = einstein_counts
    actual = pkgs_test.count_words("tests/einstein.txt")
    assert actual == expected, "Einstein quote counted incorrectly!"
    print('test passed!')


def test_plot_words(einstein_counts):
    """Test plotting of word counts."""
    counts = einstein_counts
    fig = plotting.plot_words(counts)
    assert isinstance(fig, matplotlib.container.BarContainer), "Wrong plot type"
    assert len(fig.datavalues) == 10, "Incorrect number of bars plotted"


@pytest.mark.parametrize('obj', [3.141, 'tests.txt', ["Pythons", "are", "non", "venomous"]])
def test_plot_words_error(obj):
    """Check TypeError raised when Counter not used."""
    with pytest.raises(TypeError):
        plotting.plot_words(obj)


def test_integration():
    """Test count_words() and plot_words() workflow."""
    counts = pkgs_test.count_words("tests/einstein.txt")
    fig = plotting.plot_words(counts)
    assert isinstance(fig, matplotlib.container.BarContainer), "Wrong plot type"
    assert len(fig.datavalues) == 10, "Incorrect number of bars plotted"
    assert max(fig.datavalues) == 2, "Highest word count should be 2"


def test_regression():
    """Regression test for Flatland"""
    top_word = pkgs_test.count_words(get_flatland()).most_common(1)
    assert top_word[0][0] == "the", "Most common word is not 'the'"
    assert top_word[0][1] == 2263, "'the' count has changed"
