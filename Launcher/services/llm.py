from ollama import chat
from Services.prompt_builder import build_profile
from Services.session import get_profile


def ask_llm(pregunta, profile=None):

    if profile is None:
        profile = get_profile()

    contexto = build_profile(profile)

    prompt_final = contexto + "\n\n" + pregunta

    response = chat(

        model="qwen3:8b",

        messages=[

            {
                "role": "user",
                "content": prompt_final
            }

        ]

    )

    return response["message"]["content"]