#!/usr/bin/env python3

import argparse

def greet(name):
    print(f"Hello, {name}! Welcome to your CLI tool.")

def main():
    parser = argparse.ArgumentParser(description="A simple CLI greeting tool.")
    parser.add_argument("name", help="Your name")
    args = parser.parse_args()
    greet(args.name)

if __name__ == "__main__":
    main()

#To Test: `python mycli.py Ian`