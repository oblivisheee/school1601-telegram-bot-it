import white_list
import argparse

parser = argparse.ArgumentParser(description="Add a user ID to the whitelist.")

parser.add_argument('--id', type=int, help="The ID of the user to add.")

args = parser.parse_args()

if args.id:
    white_list.add_user(id=args.id)
    print('Success.')
else:
    print("Please provide a user ID with the --id option.")
