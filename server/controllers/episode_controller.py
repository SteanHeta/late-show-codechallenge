from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.episode import Episode
from models import db

episode_bp = Blueprint('episodes', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes])

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify(episode.to_dict(rules=("appearances",)))

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify(message="Episode deleted")
