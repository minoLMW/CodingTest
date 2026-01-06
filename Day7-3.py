# 문제
# 문자열 s가 주어진다.
# 알파벳 문자만 남기고, 모두 소문자로 변환한 뒤,
# 연속으로 중복된 문자는 하나만 남긴 문자열을 반환하시오.

s = "AA!!bbCCcDD123"

def keep_alpha_to_lower(s: str) -> str:
    result_chars= []

    
    for ch in s:
        if ch.isalpha():
            result_chars.append(ch.lower())

    keep_alpha_to_lower = set(s)

    return "".join(result_chars)

print(keep_alpha_to_lower(s)) # 반환하시오라는 문제에서는 빼도 된다.


# 오답노트

def keep_alpha_to_lower(s: str) -> str:
    result = []

    for ch in s:
        if ch.isalpha():
            ch = ch.lower()
            # 처음이거나, 직전에 추가한 문자와 다를 때만 추가
            if not result or reslut[-1] != ch:
                result.append(ch)
    return "".join(result)