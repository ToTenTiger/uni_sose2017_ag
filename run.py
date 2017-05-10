import argparse

import global_vars

parser = argparse.ArgumentParser(description="Execute some pre-defined graph operations",
                                 epilog="(c) [CvO Uni Oldenburg] [Summer 2017] [AG] Bjoern Nowak & Stephan Brummel")

parser.add_argument("-o", "-output", dest="output",
                    type=int,
                    choices=[0, 1, 2, 3], default=0,
                    help="[0] Nothing (default); [1] Print dot-file; [2] Open pdf; [3]=1 and 2")

group_run = parser.add_mutually_exclusive_group()
group_run.add_argument("-t", "-task", dest="task",
                       type=int,
                       choices=[1, 2, 8, 10, 16, 17, 18],
                       help="Choose the task to run (-e will be ignored)")

group_run.add_argument("-e", "-execise", dest="execise",
                       type=int,
                       choices=range(1, 6),
                       help="Choose the execise to run completly")

parser.add_argument("-c", "-clean", dest="clean", action="store_true",
                    help="Delete dot-files after run (pdfs will be keeped)")


args = parser.parse_args()

global_vars.cleanup = args.clean
if args.output == 1:
    global_vars.printout = True
elif args.output == 2:
    global_vars.view = True
elif args.output == 3:
    global_vars.printout = True
    global_vars.view = True


if not args.task and not args.execise:
    import tasks.e05_t18
else:
    if args.task:
        if args.task == 1:
            import tasks.e01_t01
        elif args.task == 2:
            import tasks.e01_t02
        elif args.task == 8:
            import tasks.e02_t08
        elif args.task == 10:
            import tasks.e03_t10
        elif args.task == 16:
            import tasks.e04_t16
        elif args.task == 17:
            import tasks.e04_t17
        elif args.task == 18:
            import tasks.e04_t18
    elif args.execise:
        if args.execise == 1:
            import tasks.e01_t01
            import tasks.e01_t02
        elif args.execise == 2:
            import tasks.e02_t08
        elif args.execise == 3:
            import tasks.e03_t10
        elif args.execise == 4:
            import tasks.e04_t16
            import tasks.e04_t17
        elif args.execise == 5:
            import tasks.e05_t18