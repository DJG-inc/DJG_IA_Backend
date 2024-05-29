from flask import Blueprint, request, jsonify
from .service.ia_service import get_ai_response
from .service.srs_service import generate_srs_document
from .service.elicitation_service import get_elicitation_response
from .service.acta_reunion_service import generate_acta_reunion
import os
import tempfile

main_bp = Blueprint('main', __name__)

@main_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = get_ai_response(user_input)
    return jsonify({"response": response})

@main_bp.route('/generate_srs', methods=['POST'])
def generate_srs():
    data = request.json
    requirements = data.get("requirements")
    if not requirements:
        return jsonify({"error": "No requirements provided"}), 400

    srs_document = generate_srs_document(requirements)
    return jsonify({"srs_document": srs_document})

@main_bp.route('/get-elicitations', methods=['POST'])
def get_elicitations():
    data = request.json
    stakeholder_data = data.get("elicitation")
    if not stakeholder_data:
        return jsonify({"error": "No elicitation provided"}), 400

    response = get_elicitation_response(stakeholder_data)
    return jsonify({"response": response})

@main_bp.route('/generate_reunion', methods=['POST'])
def generate_minutes():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    if audio_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Crear un archivo temporal para guardar el audio
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp:
        file_path = tmp.name
        audio_file.save(file_path)

    minutes_document = generate_acta_reunion(file_path)
    
    # Eliminar el archivo temporal después de su uso
    os.remove(file_path)
    
    if not minutes_document:
        return jsonify({"error": "Failed to transcribe audio or generate minutes"}), 500

    return jsonify({"acta_reunion": minutes_document})