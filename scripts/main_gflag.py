import sys

import gflags

FLAGS = gflags.FLAGS


def main_gflagged(argv, run_func):
    """Parse flags, check for errors; execute run_func().
    run() has access to the gflags.FLAGS objects, if in same file as import of same"""

    if len(argv) == 1:
        print(
            "\n"
            "At least one command flag is required.\n\n"
            "Use \n"
            "      << {[0]} --help >>\n\n"
            "for basic information on available flags."
            "\n".format(argv)
        )

        sys.exit(1)

    try:
        argv = FLAGS(argv)  # parse flags
        if len(FLAGS(argv)) > 1:
            raise gflags.FlagsError("No positional parameters accepted")

    except gflags.FlagsError as flagerr:
        print("Error:\n\n    {0}\n\n\n".format(flagerr))
        print("Usage: %s ARGS\n%s" % (sys.argv[0], FLAGS))
        sys.exit(1)

    return run_func()
