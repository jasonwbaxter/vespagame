extends Node2D

# Obstacle types
var obstacle_type = "pothole"  # "pothole" or "cone"

func _ready():
	pass

func set_type(type_name):
	obstacle_type = type_name
	# Update visual based on type
	if type_name == "pothole":
		modulate = Color.DIM_GRAY
	elif type_name == "cone":
		modulate = Color.ORANGE

func get_type():
	return obstacle_type
