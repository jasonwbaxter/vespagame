"""
Game utilities and helper functions
"""

import math

def calculate_lane_position(lane_number, lane_width=80):
    """Calculate the x position for a given lane"""
    return lane_number * lane_width + lane_width / 2

def check_collision(pos1, pos2, radius1=30, radius2=30):
    """Check if two circular objects collide"""
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    distance = math.sqrt(dx * dx + dy * dy)
    return distance < (radius1 + radius2)

def get_score_multiplier(current_speed, base_speed=1.0):
    """Calculate score multiplier based on current speed"""
    return max(1.0, current_speed / base_speed)

def format_score(score):
    """Format score with thousands separator"""
    return f"{score:,}"

def ease_in_out(t, power=2):
    """Ease-in-out interpolation function"""
    if t < 0.5:
        return 0.5 * pow(2 * t, power)
    else:
        return 1 - 0.5 * pow(2 * (1 - t), power)
