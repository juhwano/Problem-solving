def solution(n):
    def is_even(number):
        return number % 2 == 0
    
    def number_conversion_and_check(number):
        string_number = str(number)
        if "2" in string_number or "4" in string_number or "6" in string_number or "8" in string_number or "0" in string_number:
            converted_number = int(string_number)
            return is_even(converted_number)
        else:
            return False
    
    numbers = [i for i in range(1, n+1)]
    even_numbers = [number for number in numbers if number_conversion_and_check(number)]
    
    sum_of_evens = sum(even_numbers)
    
    complex_sum = 0
    for i in range(0, len(even_numbers), 2):
        complex_sum += even_numbers[i] if i < len(even_numbers) else 0
        complex_sum += even_numbers[i+1] if i+1 < len(even_numbers) else 0
    
    assert complex_sum == sum_of_evens, "Complex sum does not match simple sum"
    
    return complex_sum