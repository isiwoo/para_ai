import random  # 무작위 선택을 위한 모듈
import sys     # 프로그램 종료를 위해 사용

# 변수 설명
# file_         : words.txt 파일 객체 
# words_        : 텍스트 파일에서 불러온 전체 단어 목록 리스트
# line_         : 파일에서 한 줄씩 읽은 문자열 
# clean_line_   : 각 줄에서 앞뒤 공백 제거된 문자열
# used_         : 지금까지 게임에서 사용된 단어들의 리스트
# word_         : 사용자 입력 단어
# last_         : 마지막에 사용된 단어 
# last_char_    : last_의 마지막 글자
# candidates_   : 컴퓨터가 선택할 수 있는 후보 단어 리스트
# random_index_ : candidates_ 중 무작위로 선택된 인덱스
# comp_word_    : 컴퓨터가 선택한 단어


# 코엔엘파이 or 코포라 활용해 텍스트 파일 열기 (실페...)
words_ = []
try:
    with open("words.txt", "r", encoding="utf-8") as file_: # 파일 염
        for line_ in file_: # 하나씩 공백없이 저장
            clean_line_ = line_.strip()
            if clean_line_ != "":
                words_.append(clean_line_)
except:
    
    words_ = [] # 파일이 없다면 빈 리스트

print("🔤 끝말잇기 게임을 시작합니다!")
print("❗ '그만'이라고 입력하면 게임이 종료됩니다.")

used_ = []  # 사용된 단어들을 저장하는 리스트

word_ = input("😊 시작 단어를 입력하세요: ").strip() # 끝말잇기 받기

if word_ == "그만": # 사용자 멈추고 싶을떄 중지지
    print("👋 게임을 종료합니다.")
    sys.exit()

if word_ in words_:
    used_.append(word_) # 텍스트 파일에서 꺼내오기
    last_ = word_ # 마지막 단어 씌우기기
else:
    print("❌ 이 단어는 단어 목록에 없습니다. 프로그램을 종료합니다.") # 예외
    sys.exit()

while True:
    last_char_ = last_[-1]  # 마지막으로 사용된 단어의 마지막 글자를 가져오기기기

    candidates_ = [w_ for w_ in words_ if w_ not in used_ and w_[0] == last_char_] # 아직 사용하지 않은 단어들 찾기

    if len(candidates_) == 0:  # 후보 단어가 없으면 컴퓨터가 낼 단어가 없는 상태태태
        print("🎉 컴퓨터가 사용할 수 있는 단어가 없습니다! 당신이 이겼습니다!")
        break  # 게임 종료 (사용자 승리)

    # 후보 단어들 중 무작위로 하나 선택
    random_index_ = random.randint(0, len(candidates_) - 1)
    comp_word_ = candidates_[random_index_]
    print("🤖 컴퓨터:", comp_word_)  # 컴퓨터가 낸 단어 출력

    used_.append(comp_word_)  # 컴퓨터가 낸 단어를 사용한 단어 목록에 추가
    last_ = comp_word_  # 마지막 단어를 컴퓨터가 낸 단어로 교체

    word_ = input("😊 다음 단어를 입력하세요: ").strip()  # 사용자로부터 다음 단어 입력받기

    if word_ == "그만":  # '그만' 입력 시 게임 종료
        print("👋 게임을 종료합니다.")
        break

    if word_ in used_:  # 이미 사용한 단어인지 검사
        print("❌ 이 단어는 이미 사용됐습니다.")
        break

    if word_ not in words_:  # 단어 목록에 없는 단어인지 검사
        print("❌ 이 단어는 단어 목록에 없습니다.")
        break

    if word_[0] != last_[-1]:  # 사용자가 낸 단어 첫 글자가 이전 단어 마지막 글자와 일치하는지 검사
        print(f"❌ 단어는 '{last_[-1]}'(으)로 시작해야 합니다.")
        break

    used_.append(word_)  # 사용자 단어를 사용한 단어 목록에 추가
    last_ = word_  # 마지막 단어를 사용자 단어로 갱신
