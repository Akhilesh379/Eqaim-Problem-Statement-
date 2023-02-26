import json

def add(num1, num2):
    # convert the numbers to strings and reverse them
    num1 = str(num1)[::-1]
    num2 = str(num2)[::-1]

    carry = 0
    steps = {}

    # loop through the digits of the numbers and add them
    for i in range(max(len(num1), len(num2))):
        # get the digits, or use 0 if one number is shorter than the other
        digit1 = int(num1[i]) if i < len(num1) else 0
        digit2 = int(num2[i]) if i < len(num2) else 0

        # add the digits and the carry
        total = digit1 + digit2 + carry

        # update the carry for the next iteration
        carry = total // 10

        # get the sum digit and append it to the sum string
        sum_digit = total % 10
        sum_string = str(sum_digit) + (steps.get("step"+str(i), {"carryString": ""})["carryString"] if i > 0 else "")

        # get the carry string for this step
        carry_string = "1" * carry if carry > 0 else ""

        # add the step to the dictionary
        steps["step"+str(i+1)] = {"carryString": carry_string, "sumString": sum_string}

    # reverse the dictionary and return it as JSON
    return json.dumps({k: steps[k] for k in reversed(steps)}, indent=4)

# example usage
print(add(1489, 714))
