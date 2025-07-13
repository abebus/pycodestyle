import pyperf
import tokenize
from io import StringIO
from pycodestyle import maximum_doc_length

logical_line = r"""This is a sample docstring that exceeds the maximum length.
                    This is a sample docstring that exceeds the maximum length. This is a sample docstring that exceeds the maximum length."""
max_doc_length = 72
noqa = False

tokens = list(tokenize.generate_tokens(StringIO(logical_line).readline))

def benchmark_maximum_doc_length():
    list(maximum_doc_length(logical_line, max_doc_length, noqa, tokens))

runner = pyperf.Runner()
runner.timeit(
    name="maximum_doc_length",
    stmt="benchmark_maximum_doc_length()",
    globals=globals()
)