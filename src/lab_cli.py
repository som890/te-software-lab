import argparse

def positive_slot(value):
    try:
           slot = int(value)
    except ValueError:
         raise argparse.ArgumentTypeError(f"Invalid slot value: {value}")

    if slot <= 0:
         raise argparse.ArgumentTypeError(f"Slot must be a positve integer")
    return slot

def build_parser():

    parser = argparse.ArgumentParser(
        description="TE Software Tranning CLI"
    )

    parser.add_argument(
        "slot",
          type=positive_slot,
            help="Slot number"
    )

    parser.add_argument(
        "mode", 
        choices=["ON", "OFF"], 
        help="Test mode"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug output"
    )

    parser.add_argument(
         "--verbose",
         action="store_true",
         help="Enable verbose output"
    )

    parser.add_argument(
         "--version",
         action="version",
         help="Show version information",
         version="LineDataClient 0.1.0"
    )
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    print(f"LAB_ONLY|Slot: {args.slot} | Mode: {args.mode}")

    if args.debug:
        print("[DEBUG] Debug mode enabled")

    if args.verbose:
        print(f"[VERBOSE] Slot number: {args.slot} | Mode: {args.mode}")


if __name__ == "__main__":
    main()