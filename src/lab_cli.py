import argparse

def build_parser():

    parser = argparse.ArgumentParser(
        description="TE Software Tranning CLI"
    )

    parser.add_argument(
        "slot",
          type=int,
            help="Slot number"
    )

    parser.add_argument(
        "mode", 
        choices=["ON", "OFF"], 
        help="Test mode"
    )

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    print(f"LAB_ONLY|Slot: {args.slot} | Mode: {args.mode}")
    
if __name__ == "__main__":
    main()