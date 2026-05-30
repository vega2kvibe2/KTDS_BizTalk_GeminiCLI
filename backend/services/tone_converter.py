import os
from dotenv import load_dotenv
from langchain_upstage import ChatUpstage
from langchain_core.prompts import ChatPromptTemplate
from backend.prompts.templates import PROMPTS, DEFAULT_PROMPT

# .env 파일 로드
load_dotenv()

class ToneConverter:
    def __init__(self):
        api_key = os.getenv("UPSTAGE_API_KEY")
        if not api_key:
            raise ValueError("UPSTAGE_API_KEY가 .env 파일에 설정되지 않았습니다.")
        
        # Solar-Pro3 모델 초기화
        self.llm = ChatUpstage(model="solar-pro3", api_key=api_key)

    async def convert(self, text: str, target_audience: str) -> str:
        # 수신 대상에 따른 시스템 프롬프트 선택
        system_prompt = PROMPTS.get(target_audience, DEFAULT_PROMPT)
        
        # 프롬프트 템플릿 생성
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{text}")
        ])
        
        # 체인 생성 및 실행
        chain = prompt | self.llm
        
        try:
            import time
            start_time = time.time()
            print(f"[DEBUG] LLM 호출 시작: target={target_audience}, text_len={len(text)}")
            
            response = await chain.ainvoke({"text": text})
            
            end_time = time.time()
            print(f"[DEBUG] LLM 호출 완료: 소요 시간 {end_time - start_time:.2f}초")
            
            return response.content.strip()
        except Exception as e:
            print(f"Error during LLM invocation: {e}")
            raise RuntimeError("LLM 호출 중 오류가 발생했습니다.")

# 싱글톤 인스턴스 생성
converter = ToneConverter()
