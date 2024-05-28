from ..service.ia_service import configure_ai
from ..utils.prompt_builder import build_prompt_srs

def generate_srs_document(requirements):
    prompt = build_prompt_srs(requirements)
    model = configure_ai()
    convo = model.start_chat(history=[])
    convo.send_message(prompt)
    response = convo.last.text
    return response
