# Vespa Scooter Game

A modern arcade-style mobile game for Android and iOS featuring a Vespa-like scooter navigating through 4 lanes while avoiding obstacles and collecting power-ups.

## Game Features

- **4-Lane Gameplay**: Navigate your scooter through 4 lanes
- **Obstacles**: Potholes and traffic cones to avoid
- **Power-ups**: 
  - Ramp: Speed boost
  - Skull & Crossbones: Invincibility (temporary)
- **Controls**:
  - A/B buttons: Change speed
  - Left/Right arrows: Change lanes
- **Modern Arcade Style**: Beautiful graphics with arcade aesthetic

## Project Structure

```
vespagame/
├── godot/                 # Godot 4.x project
│   ├── scenes/           # Game scenes
│   ├── scripts/          # GDScript files
│   ├── assets/           # Graphics, sounds, fonts
│   └── project.godot     # Godot project file
├── python/               # Python utilities & tools
│   ├── asset_generator/  # Asset generation scripts
│   └── utils/            # Helper utilities
└── README.md
```

## Getting Started

### Requirements
- Godot 4.x
- Python 3.8+
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/jasonwbaxter/vespagame.git
cd vespagame
```

2. Open the Godot project:
   - Launch Godot 4.x
   - Select "Open Project"
   - Navigate to `godot/` folder
   - Select `project.godot`

3. Run the game:
   - Press F5 or click the Play button in Godot

## Game Controls

| Control | Action |
|---------|--------|
| A Button | Decrease Speed |
| B Button | Increase Speed |
| Left Arrow | Move Left Lane |
| Right Arrow | Move Right Lane |

## Development

### Python Utilities

Generate game assets using Python scripts:

```bash
cd python
python asset_generator/generate_obstacles.py
```

## License

MIT License - Feel free to use and modify!
