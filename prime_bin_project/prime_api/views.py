# prime_api/views.py
import json
from django.http import JsonResponse

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def div(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def prime_binary(request):
    start = int(request.GET.get('start', 0))
    end = int(request.GET.get('end', 100))

    result = {}
    for num in range(start, end):
        if is_prime(num):
            result[num] = bin(num)[2:]
        else:
            result = div(num)

    return JsonResponse(result)
