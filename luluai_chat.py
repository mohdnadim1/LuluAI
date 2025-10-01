import argparse
from luluai.core import LuluModel

def main():
    """
    Main function to run the LuluAI chat application.
    """
    parser = argparse.ArgumentParser(description="LuluAI Chat Application")
    parser.add_argument(
        "--model",
        type=str,
        default="yourusername/luluai",
        help="The name of the model to use.",
    )
    args = parser.parse_args()

    # Initialize the model
    model = LuluModel(model_name=args.model)

    print("Welcome to LuluAI Chat! Type 'exit' to quit.")

    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            break

        # Generate and print the response from the model
        response = model.generate_response(user_input)
        print(response)

if __name__ == "__main__":
    main()