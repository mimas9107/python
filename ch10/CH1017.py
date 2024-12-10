import argparse

def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(
        description="一個簡單的計算器."
    )

    # Add arguments
    parser.add_argument(
        "num1", type=float, help="第一個數字."
    )
    parser.add_argument(
        "num2", type=float, help="第二個數字."
    )
    parser.add_argument(
        "operation",
        type=str,
        choices=["add", "subtract", "multiply", "divide"],
        help="可用以下操作: add, subtract, multiply, or divide.",
    )

    # Parse arguments
    args = parser.parse_args()

    # Perform calculation based on the operation
    if args.operation == "add":
        result = args.num1 + args.num2
    elif args.operation == "subtract":
        result = args.num1 - args.num2
    elif args.operation == "multiply":
        result = args.num1 * args.num2
    elif args.operation == "divide":
        if args.num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = args.num1 / args.num2

    # Print the result
    print(f"{args.operation} 操作的計算結果是: {result}")

if __name__ == "__main__":
    main()
