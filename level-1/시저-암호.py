def solution(s, n):
    answer = ''
    s = list(s)
    
    for letter in s: 
        #아스키코드 변환
        a = ord(letter)
        
        if letter.isupper(): #대문자일 경우
            a = ((a - 65) + n) % 26 + 65
        elif letter.islower(): #소문자일 경우
            a = ((a - 97) + n) % 26 + 97
        
        answer += chr(a) 
        
    return answer