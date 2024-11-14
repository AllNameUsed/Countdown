import random
import operator

BIG = [25, 50, 75, 100]
SMALL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def generate_numbers(selections):
    # Placeholder for generating numbers based on selections
    # 'selections' is a list like ['Big', 'Small', ...]
    numbers_values = []
    for s in selections:
        if s == "Big":
            x = random.choice(BIG)
            numbers_values.append(x)
        elif s == 'Small':
            x = random.choice(SMALL)
            numbers_values.append(x)
        else:
            print("Selection " + str(s) + " is NOT VALID !!!")
    return numbers_values

def generate_random_goal(numbers):
    """
    Generate a random goal number by creating a random arithmetic expression
    using the given numbers and basic operations.
    """
    from math import isclose

    # Define operations
    operations = [operator.add, operator.sub, operator.mul, operator.truediv]
    operation_symbols = {
        operator.add: '+',
        operator.sub: '-',
        operator.mul: '*',
        operator.truediv: '/'
    }

    # Build a random expression tree
    def build_expression(nums):
        if len(nums) == 1:
            return nums[0], str(nums[0])
        else:
            # Randomly split the list into two non-empty parts
            split_index = random.randint(1, len(nums) - 1)
            left_nums = nums[:split_index]
            right_nums = nums[split_index:]

            # Recursively build expressions for left and right parts
            left_value, left_expr = build_expression(left_nums)
            right_value, right_expr = build_expression(right_nums)

            # Randomly select an operation
            op = random.choice(operations)

            # Avoid division by zero and ensure integer results
            if op == operator.truediv:
                # Avoid division by zero
                if isclose(right_value, 0):
                    op = random.choice([operator.add, operator.sub, operator.mul])
                else:
                    # Ensure division results in integer
                    result = left_value / right_value
                    if not isclose(result, int(result)):
                        op = random.choice([operator.add, operator.sub, operator.mul])

            # Compute the new value
            try:
                if op == operator.truediv:
                    result = op(left_value, right_value)
                    # Ensure division results in integer
                    if not isclose(result, int(result)):
                        raise ValueError('Result is not integer')
                    result = int(result)
                else:
                    result = op(left_value, right_value)
            except ZeroDivisionError:
                # Retry with a different operation if division by zero occurs
                op = random.choice([operator.add, operator.sub, operator.mul])
                result = op(left_value, right_value)

            # Build the expression string
            expr = f"({left_expr} {operation_symbols[op]} {right_expr})"
            return result, expr

    # Shuffle numbers to randomize
    random_numbers = numbers.copy()

    # Keep generating until we get a valid goal
    max_attempts = 100
    for _ in range(max_attempts):
        random.shuffle(random_numbers)
        try:
            goal_value, goal_expr = build_expression(random_numbers)
            # Ensure goal is an integer between 101 and 999
            if isinstance(goal_value, int) and 101 <= goal_value <= 999:
                return goal_value, goal_expr
        except (ZeroDivisionError, ValueError):
            continue  # Retry if an error occurs

    # If no valid goal found after max_attempts, default to a random number
    return random.randint(101, 999), 'Random Goal'

