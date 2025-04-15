# 간단한 예시 코드
# 데이터 처리 예시

def calculate_average(numbers):
    """
    숫자 리스트의 평균을 계산하는 함수
    
    Args:
        numbers (list): 숫자 리스트
        
    Returns:
        float: 평균값
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers):
    """
    숫자 리스트에서 최댓값을 찾는 함수
    
    Args:
        numbers (list): 숫자 리스트
        
    Returns:
        int or float: 최댓값
    """
    if not numbers:
        return None
    return max(numbers)

def count_words(text):
    """
    문자열에서 단어 수를 세는 함수
    
    Args:
        text (str): 입력 문자열
        
    Returns:
        int: 단어 수
    """
    if not text:
        return 0
    words = text.split()
    return len(words)

# 테스트
if __name__ == "__main__":
    sample_numbers = [10, 20, 30, 40, 50]
    print(f"평균: {calculate_average(sample_numbers)}")
    print(f"최댓값: {find_max(sample_numbers)}")
    
    sample_text = "이것은 예시 문장입니다. Claude와 함께 작업해 보세요!"
    print(f"단어 수: {count_words(sample_text)}")
