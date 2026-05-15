## Player Scooter Controller
extends CharacterBody2D

## Movement constants
@export var lane_positions: Array[float] = [80.0, 160.0, 240.0, 320.0]
@export var move_speed: float = 200.0
@export var current_lane: int = 1

## Invincibility system
var is_invincible: bool = false
var invincibility_timer: float = 0.0
@export var invincibility_duration: float = 5.0

## Game reference
var game_manager: Node

func _ready() -> void:
	game_manager = get_parent()
	if not is_instance_valid(game_manager):
		push_error("Game manager not found!")
	
	position.x = lane_positions[current_lane]

func _process(delta: float) -> void:
	if not is_instance_valid(game_manager):
		return
	
	# Handle lane change input
	if Input.is_action_pressed("ui_left"):
		change_lane(-1)
	elif Input.is_action_pressed("ui_right"):
		change_lane(1)
	
	# Update invincibility
	if is_invincible:
		invincibility_timer -= delta
		if invincibility_timer <= 0:
			is_invincible = false
			modulate = Color.WHITE
		else:
			# Visual feedback - green tint during invincibility
			modulate = Color(0.2, 1.0, 0.3, 1.0)

func change_lane(direction: int) -> void:
	var new_lane: int = clampi(current_lane + direction, 0, lane_positions.size() - 1)
	
	if new_lane != current_lane:
		current_lane = new_lane
		var target_x: float = lane_positions[current_lane]
		position.x = target_x

func activate_invincibility() -> void:
	is_invincible = true
	invincibility_timer = invincibility_duration

func is_safe() -> bool:
	return is_invincible
