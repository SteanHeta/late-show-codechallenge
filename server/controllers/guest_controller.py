from flask import Blueprint, jsonify
from models.guest import Guest

guest_bp = Blueprint('guests', __name__)

@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests])
