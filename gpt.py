import openai

api_key = "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"
openai.api_key = api_key

# 사용자에게 무엇을 물어볼지 프롬프트로 정의합니다.
prompt = """너는 지금부터 면접관이고, 사용자를 면접보는 역할이야
사용자에게 질문을 해야해
첫 질문은 사용자의 이력서를 보고 질문할 내용을 선택한다
다음에 질문할 내용을 선택하고 사용자에게 딱 한가지 질문하세요
안녕하세요로 시작
"""
# 왜 해당 직군으로 지원했나요?
# 왜 저희 회사에 지원하셨나요?
# 해당 직군의 매력이 무엇이라고 생각하나요?
# 해당 직군에서 본인의 장점은?
# 해당 직군을 하면서 이루고자 하는 목표는?
# 해당 직군을 하기 위해 어떤 노력을 했나요?
# 왜 저희가 지원자를 뽑아야 하나요?
# 지원자의 단점은 무엇인가요?

text = "이 력 서 성 명 홍길동 영 문 Hong Gil Dong 한 문 洪吉東 생년월일 2000년 01월 01일 나이(만) 19세 휴 대 폰 010-1234-5678 전화번호 042-630-9681 이 메 일 wsjob@wsi.ac.kr 주 소 대전광역시 동구 동대전로 171 E1 206호 보훈대상자 해당 □ 해당없음 ■ 장애여부 해당 □ 해당없음 ■ 학력사항 (최종학력: 우송정보대학 졸업예정) 재학기간 학교명 및 전공 학점 2016. 03 ~ 2020. 02 우송정보대학 호텔관광과 3.0 / 4.5 2014. 03 ~ 2016. 02 우송고등학교 구분 주간 인문계 소재지 대전 대전 자격증 취득일 2014. 07 2016. 03 2019. 05 주요활동 및 경력 자격증/면허증 전자기기기능사 운전면허증 ITQ정보기술자격 등급 발행처 2종보통 한국산업인력공단 한국생산성본부 기간 활동내용 활동구분 기관명/업체명 2019. 06. 17 ~ 2019. 07. 12 지진계 장비 설치 및 유지 보수 실습 2018. 12 .10 ~ 2019. 02. 03 서빙 및 손님 대응 아르바이트 우송기술 롯데리아 능력사항 워드/한글 상 □ / 중 ■ / 하 □ 영어 상 □ / 중 ■ / 하 □ OA능력 엑셀 상 □ / 중 ■ / 하 □ 어학능력 일본어 상 □ / 중 □ / 하 □ 파워포인트 상 □ / 중 ■ / 하 □ 기타( ) 상 □ / 중 □ / 하 □ 병역사항 복무기간 2017. 02 ~ 2018. 11 군별 군필 계급 병장 병과 통신 전역사유 위에 기재한 사항은 사실과 틀림이 없습니다. 2019년 01월 01일 성 명 : 홍 길 동 (인) 자기소개서 성장과정 성격의장단점 학내외활동 및 주요경력 지원동기 및 입사후포부 "
messages = []
messages.append({"role": "user", "content": text})
# GPT 모델에 프롬프트를 전달하여 질문 생성
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
        # {"role": "user", "content": prompt}
    ],
    temperature=0.5,
    max_tokens=300  # 생성된 응답의 최대 길이를 조절할 수 있습니다.
)

user_question = response.choices[0].message["content"].strip()
text = user_question.split("?")[0] + "?"
# text = ""
# for question in user_question.split("\n"):
#     if question == '':
#         continue
#     if question[0]=='2':
#         break
#     text+=question
    

print("GPT가 생성한 질문:", text)
messages.append({"role": "assistant", "content": text})


prompt2 = """
사용자에게 질문을 해야해
사용자의 이력서와 답변을 바탕으로 추가적인 질문을 해줘
"""
for _ in range(3):
    text = input()
    messages.append({"role": "user", "content": text})

    # GPT 모델에 프롬프트를 전달하여 질문 생성
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt2}
            # {"role": "user", "content": prompt}
            , *messages
        ],
        temperature=0.5,
        max_tokens=300  # 생성된 응답의 최대 길이를 조절할 수 있습니다.
    )
    user_question = response.choices[0].message["content"].strip()
    user_question = user_question.split("?")[0] + "?"
    messages.append({"role": "assistant", "content": user_question})
    print("GPT가 생성한 질문:", user_question)

############################################################################################

text = input()
messages.append({"role": "user", "content": text})

messages2 = []
prompt3 = """
사용자에게 질문을 해야해
실제 면접을 보듯이 조언하지 말고 강하게 말해줘
사용자의 답변을 바탕으로 cs면접 추가적인 질문을 해줘
프로젝트에 관한 내용보다 CS지식에 대한 질문
다음에 질문할 내용을 선택하고 사용자에게 딱 한가지 질문하세요
좋습니다 다음은 cs면접을 시작하겠습니다. 로 시작해
사용자가 모른다고 해도 답변하지말고 다음 질문을 시작해
"""
# GPT 모델에 프롬프트를 전달하여 질문 생성
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt3}
        # {"role": "user", "content": prompt}
        , *messages2
    ],
    temperature=0.5,
    max_tokens=300  # 생성된 응답의 최대 길이를 조절할 수 있습니다.
)
user_question = response.choices[0].message["content"].strip()
text = user_question.split("?")[0] + "?"
messages2.append({"role": "assistant", "content": text})

print("GPT가 생성한 CS질문:", text)
# text = input()
# messages.append({"role": "user", "content": text})

# # GPT 모델에 프롬프트를 전달하여 질문 생성
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": prompt3}
#         # {"role": "user", "content": prompt}
#         , *messages
#     ],
#     temperature=0.5,
#     max_tokens=300  # 생성된 응답의 최대 길이를 조절할 수 있습니다.
# )
    

prompt4 = """
당신은 지금부터 cs직종 면접관입니다. 당신의 질문을 통해 면접자의 채용 유무를 판단할 것 입니다.
면접자의 답변에 조언, 설명등 을 해선 안됩니다. 설령 답변을 하지 못하더라도 당신은 그에게
정보를 제공해선 안됩니다.
면접 질문은 최대한 간결하게 말해주십시오
만약 모른다라고 답변 한다면 그렇다면 이라하고 다음 질문으로 넘어가세요 
"""
for _ in range(3):
    text = input()
    messages2.append({"role": "user", "content": text})

    # GPT 모델에 프롬프트를 전달하여 질문 생성
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt4}
            # {"role": "user", "content": prompt}
            , *messages2
        ],
        temperature=0.5,
        max_tokens=300  # 생성된 응답의 최대 길이를 조절할 수 있습니다.
    )
    user_question = response.choices[0].message["content"].strip()
    messages2.append({"role": "assistant", "content": user_question})

    print("GPT가 생성한 질문:", user_question)