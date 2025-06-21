from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.appearance import Appearance
from models import db

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    try:
        appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        if appearance.rating < 1 or appearance.rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict()), 201
    except Exception as e:
        return jsonify(error=str(e)), 400
