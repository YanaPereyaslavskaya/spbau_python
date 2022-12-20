def gcd(first_num:int, sec_num:int) -> int:
    if sec_num == 0:
        return first_num
    return gcd(sec_num, first_num % sec_num)


print(gcd(1404, 15912))

#Success: no issues found in 1 source file


def gcd(first_num:int, sec_num:int) -> None:
    if sec_num == 0:
        return first_num
    return gcd(sec_num, first_num % sec_num)


print(gcd(1404, 15912))
#qw.py:3: error: No return value expected  [return-value]
#qw.py:7: error: "gcd" does not return a value  [func-returns-value]
#Found 2 errors in 1 file (checked 1 source file)

def gcd(first_num:bool, sec_num:int) -> int:
    if sec_num == 0:
        return first_num
    return gcd(sec_num, first_num % sec_num)


print(gcd(1404, 15912))

#qw.py:4: error: Argument 1 to "gcd" has incompatible type "int"; expected "bool"  [arg-type]
#qw.py:7: error: Argument 1 to "gcd" has incompatible type "int"; expected "bool"  [arg-type]
#Found 2 errors in 1 file (checked 1 source file)
