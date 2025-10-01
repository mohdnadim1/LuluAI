import argparse
from luluai.core import LuluModel

def main():
    """
    Main function to run the LuluAI command-line interface.
    """
    parser = argparse.ArgumentParser(description="LuluAI Command-Line Interface")
    parser.add_argument("prompt", type=str, help="The prompt to send to LuluAI.")
    parser.add_argument(
        "--model",
        type=str,
        default="yourusername/luluai",
        help="The name of the model to use.",
    )
    args = parser.parse_args()

    # Initialize the model
    model = LuluModel(model_name=args.model)

    # Generate and print the response
    response = model.generate_response(args.prompt)
    print(response)

if __name__ == "__main__":
    main()