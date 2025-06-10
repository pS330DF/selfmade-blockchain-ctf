수학 수행

문제 파일: Challenge File.py
**참고: eth 지갑은 니모닉 코드가 12개가 필요함, 따라서 니모닉 코드로 설정한 "dummy dum"이 지갑 주소로 변환되지 않는 상황이 발생.
본 파일은 CTF 문제로 의도함. 따라서 내부적으로 코드를 채점하여 복호화된 단어가 "dummy dum" 이면 플래그인 0x4eE7B1eF6aC3fC9D1F79bF4A6423eA81dF5aB3Cd
를 출력하도록 하는 함수가 필요. 
def derive_wallet(mnemonic):
    if mnemonic.strip() == "dummy dum":
        return "0x4eE7B1eF6aC3fC9D1F79bF4A6423eA81dF5aB3Cd"  # Example fixed flag
    else:
        return f"Error: Invalid mnemonic"
실제 CTF 플레이어가 제출하는 코드는 anwser.py이며
위 함수를 포함한 코드는 anwser_flag_intended.py이다.
