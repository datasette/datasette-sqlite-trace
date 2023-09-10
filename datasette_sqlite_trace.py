from datasette import hookimpl
import sys


def log_to_stderr(text):
    print(text, file=sys.stderr)


@hookimpl
def prepare_connection(conn):
    conn.set_trace_callback(log_to_stderr)
