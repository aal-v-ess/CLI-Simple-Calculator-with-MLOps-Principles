#!/usr/bin/env python

"""
Main cli or app entry point
"""

from mylib.calculator import add, subtract, divide, multiply
import click


@click.argument("a", type=int)
@click.argument("b", type=int)
def add_cli(a, b):
    """Add two numbers together

    Example:
        ./main.py add 1 2
    """

    click.echo(click.style(str(add(a, b)), fg="green"))


@click.argument("a", type=int)
@click.argument("b", type=int)
def subtract_cli(a, b):
    """Subtracts two numbers together

    Example:
        ./main.py subtract 1 2
    """

    click.echo(click.style(str(subtract(a, b)), fg="green"))


@click.argument("a", type=int)
@click.argument("b", type=int)
def divide_cli(a, b):
    """Divides two numbers together

    Example:
        ./main.py divide 1 2
    """

    click.echo(click.style(str(divide(a, b)), fg="green"))


@click.argument("a", type=int)
@click.argument("b", type=int)
def multiply_cli(a, b):
    """Multiplies two numbers together

    Example:
        ./main.py multiply 1 2
    """

    click.echo(click.style(str(multiply(a, b)), fg="green"))


@click.command("operation")
@click.argument("operation", type=str)
@click.argument("a", type=int)
@click.argument("b", type=int)
def calc_operation(operation, a, b):
    """Identifies operation to execute and calls proper cli

    Example:
        ./main.py multiply 2 2
    """
    try:
        if operation == "add":
            add_cli(a, b)
        elif operation == "subtract":
            subtract_cli(a, b)
        elif operation == "divide":
            divide_cli(a, b)
        elif operation == "multiply":
            multiply_cli(a, b)
        else:
            click.echo(
                "Invalid operation specified. Available options are: add, subtract, divide, multiply."
            )
    except ValueError as e:
        click.echo(f"Error: {e}. Please check your inputs and try again.")


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    calc_operation()
