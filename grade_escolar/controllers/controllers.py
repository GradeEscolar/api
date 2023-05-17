from flask import jsonify

def create_response(status_code: int = 200, message: str = None):
    data = {
        'success': status_code == 200,
        'message': message
    }
    
    response = jsonify(data)
    response.status_code = status_code
    return response