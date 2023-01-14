# Rohan Rajesh Kalbag
# Roll: 20D170033


from argparse import ArgumentParser


# main function to perform command line functionality
def perform_command_line_functionality():
    parser = ArgumentParser(description="cli assignment for ae6102")
    parser.add_argument('-a', '--arg1',
                        type=float, default=5.0, help="argument 1")
    parser.add_argument('-b', '--arg2',
                        type=float, default=2.0, help="argument 2")
    parser.add_argument('--action', choices=['add', 'mul', 'sub', 'exp'],
                        default='add', help="the action to be performed")
    parser.add_argument('-o', '--output', required=False,
                        default="", help="file name for output to be printed")
    parser.add_argument('-q', '--quiet',
                        action='store_true', help="to not print")
    args = parser.parse_args()

    result = 0

    # check for action
    if (args.action == 'add'):
        result = args.arg1 + args.arg2
    elif (args.action == 'sub'):
        result = args.arg1 - args.arg2
    elif (args.action == 'mul'):
        result = args.arg1 * args.arg2
    else:
        result = args.arg1 ** args.arg2

    # check if needed to be outputted to files
    if (len(args.output) > 0):
        with open(args.output, 'w') as t:
            t.write(str(result))

    # check if needed to be printed
    if (not args.quiet):
        print(result)


if __name__ == '__main__':
    perform_command_line_functionality()
