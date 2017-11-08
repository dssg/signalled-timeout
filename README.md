# signalled-timeout

Timeout library for generic interruption of main thread by an exception after a configurable duration.

## Use case

Set a timeout (seconds) upon expiration of which an exception is raised:

    from timeout import timeout

...as a context manager:

    with timeout(0.5):
        ... work ...

...or decorating a function:

    @timeout(0.5)
    def work():
        ...

The exception may be configured, either by passing an exception instance, or by specifying an overriding exception class and/or value(s):

    with timeout(0.5, RuntimeError("Work took too long")):
        ... work ...

    with timeout(0.5, RuntimeError, "Work took too long"):
        ... work ...

    with timeout(0.5, exc=RuntimeError):
        ... work ...

    with timeout(0.5, value="Work took too long"):
        ... work ...

    with timeout(0.5, value=(2, "Took too long", 'work.py')):
        ... work ...

The timeout exception defaults to `TimeoutError("Operation timed out")`.

Note: `timeout` is implemented via `signal`, and as such may not be applied outside of a process's main thread.

## Installation

`signalled-timeout` is a Python distribution, which may be installed via `easy_install` or `pip`, _e.g._:

    pip install signalled-timeout

...or, from source:

    python setup.py install

## Testing

To test the distribution on your system, execute its `test` command:

    python setup.py test
