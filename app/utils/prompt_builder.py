def build_prompt_srs(requirements):
    prompt = """

    Basado en los siguientes requisitos, redacta un documento de especificación de requisitos de software (SRS) para un sistema de gestión de tareas. Asegúrate de incluir todos los elementos esenciales de un SRS, como: Introducción, Objetivos del Sistema, Requisitos Funcionales, Requisitos No Funcionales, Glosario y Referencias.

    En los requisitos, se incluye el número, descripción, precondiciones, postcondiciones, flujo basico y excepciones.

    Los requisitos son los siguientes:

    """
    for req in requirements:
        prompt += f"""
        Número: {req['Numero']}
        Descripción: {req['Requisito']}
        Tipo: {req['Tipo']}
        Prioridad: {req['Prioridad']}
        """

    prompt += """
    
    """
    return prompt


def build_prompt_elicitation(stakeholder_data):
    # Crear el prompt basado en los datos del stakeholder
    prompt = f"""
    Basado en la siguiente información sobre los stakeholders, determina la mejor técnica de elicitation y explica por qué se seleccionó esa técnica:

    - Nivel de Disponibilidad: {stakeholder_data.get('nivel_disponibilidad')}
    - Experiencia Técnica Previa: {stakeholder_data.get('experiencia_previa')}
    - Nivel de Conocimiento Técnico: {stakeholder_data.get('conocimiento_tecnico')}
    - Conocimiento de Tecnologías o Sistemas Existentes: {stakeholder_data.get('conocimiento_tecnologias_existentes')}
    - Tiempo Disponible para Participación: {stakeholder_data.get('tiempo_disponible')}
    - Preferencias de Comunicación: {stakeholder_data.get('preferencias_comunicacion')}
    - Comprensión de Problemas y Desafíos: {stakeholder_data.get('comprension_problemas')}
    - Nivel de Influencia en la Toma de Decisiones: {stakeholder_data.get('nivel_influencia')}
    - Preferencias de Entregables: {stakeholder_data.get('preferencias_entregables')}
    - Expectativas de Comunicación y Transparencia: {stakeholder_data.get('expectativas_comunicacion')}
    """

    return prompt

# app/utils/prompt_builder.py

def build_prompt_minutes(transcribed_text):
    prompt = f"""
    Basado en la siguiente transcripción de una reunión, redacta un acta de reunión completa e identifica posibles requisitos mencionados durante la reunión. El acta debe incluir: Objetivo, Participantes, Desarrollo de la Reunión, Temas Discutidos, Decisiones Tomadas, Compromisos, y Requisitos Identificados.

    Transcripción de la reunión:
    {transcribed_text}
    """
    return prompt
