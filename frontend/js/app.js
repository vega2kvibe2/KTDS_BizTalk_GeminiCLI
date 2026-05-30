// app.js
const API_BASE = "http://localhost:8000";

document.addEventListener("DOMContentLoaded", () => {
    const targetButtons = document.querySelectorAll(".target-btn");
    const convertBtn = document.getElementById("convertBtn");
    const copyBtn = document.getElementById("copyBtn");
    const inputText = document.getElementById("inputText");
    const outputText = document.getElementById("outputText");
    const loader = document.getElementById("loader");

    let selectedTarget = null;

    // 수신 대상 버튼 클릭 이벤트
    targetButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            targetButtons.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            selectedTarget = btn.dataset.target;
        });
    });

    // 변환 로직
    async function convertTone() {
        const text = inputText.value.trim();
        
        if (!text) {
            alert("변환할 내용을 입력해주세요.");
            return;
        }

        if (!selectedTarget) {
            alert("수신 대상을 선택해주세요.");
            return;
        }

        setLoading(true);

        try {
            const response = await fetch(`${API_BASE}/api/convert`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    text: text,
                    target_audience: selectedTarget
                }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || "변환 중 오류가 발생했습니다.");
            }

            const data = await response.json();
            outputText.value = data.converted_text;
        } catch (error) {
            console.error("Error:", error);
            alert(`오류: ${error.message}`);
        } finally {
            setLoading(false);
        }
    }

    // 로딩 상태 제어
    function setLoading(isLoading) {
        if (isLoading) {
            loader.classList.remove("hidden");
            convertBtn.disabled = true;
            convertBtn.textContent = "변환 중...";
        } else {
            loader.classList.add("hidden");
            convertBtn.disabled = false;
            convertBtn.textContent = "변환하기";
        }
    }

    // 복사 기능
    function copyToClipboard() {
        if (!outputText.value) return;

        navigator.clipboard.writeText(outputText.value)
            .then(() => {
                const originalText = copyBtn.textContent;
                copyBtn.textContent = "복사 완료!";
                setTimeout(() => {
                    copyBtn.textContent = originalText;
                }, 2000);
            })
            .catch(err => {
                console.error("Copy failed:", err);
                alert("복사에 실패했습니다.");
            });
    }

    // 이벤트 리스너 등록
    convertBtn.addEventListener("click", convertTone);
    copyBtn.addEventListener("click", copyToClipboard);
});
