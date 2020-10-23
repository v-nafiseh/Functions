def digSum(n):
    sum = 0

    while n > 0 or sum > 9:

        if n == 0:
            n = sum
            sum = 0

        sum += n % 10
        n //= 10

    return sum


def check(number):
    rep = {"ones": 0, "twos": 0}
    for num in range(1, number):
        sum_num = digSum(num)
        if sum_num == 1:
            rep["ones"] += 1
        elif sum_num == 2:
            rep["twos"] += 1

    return rep




def show_result(result):
    for k, v in result.items():
        print(f"number of {k} is : {v}\n")


num = int(input("enter ur number : "))
result = check(num)
show_result(result)
