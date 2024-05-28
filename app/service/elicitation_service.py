from ..service.ia_service import configure_ai
from ..utils.prompt_builder import build_prompt_elicitation

def get_elicitation_response(stakeholder_data):
    prompt = build_prompt_elicitation(stakeholder_data)
    model = configure_ai()
    convo = model.start_chat(history=[])
    convo.send_message(prompt)
    response = convo.last.text
    return response