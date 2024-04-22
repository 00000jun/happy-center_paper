"""
Number to KOR function
- 숫자를 한글로 변환해주는 모듈
"""

#숫자 -> 한글
def readnumber_pre(n):

    units = [''] + list('십백천')
    nums = '일이삼사오육칠팔구'
    result = []

    i = 0

    while n > 0:
        n, r = divmod(n, 10)
        if r > 0:
            result.append(nums[r-1] + units[i])
        i += 1

    return ''.join(result[::-1])

def readnumber(n):
    """1억 미만의 숫자를 읽는 함수"""
    a, b = [readnumber_pre(x) for x in divmod(n, 10000)]

    if a:
        return a + "만" + b
        
    return b