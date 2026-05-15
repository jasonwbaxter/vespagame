#!/usr/bin/env python3
"""
Asset Generator for Vespa Scooter Game
Generates all sprite assets using PIL (Pillow)
"""

import os
from PIL import Image, ImageDraw

def ensure_dir(path):
    """Ensure directory exists"""
    os.makedirs(path, exist_ok=True)

def generate_scooter_sprite(output_path):
    """Generate scooter sprite"""
    img = Image.new('RGBA', (60, 80), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw scooter body (red)
    draw.rectangle([(10, 20), (50, 60)], fill=(200, 50, 50, 255))
    
    # Draw wheels (black)
    draw.ellipse([(15, 55), (35, 75)], fill=(30, 30, 30, 255))
    draw.ellipse([(35, 55), (55, 75)], fill=(30, 30, 30, 255))
    
    # Draw handlebars (black)
    draw.rectangle([(20, 10), (40, 20)], fill=(30, 30, 30, 255))
    
    img.save(output_path)
    print(f"✓ Generated scooter sprite: {output_path}")

def generate_pothole_sprite(output_path):
    """Generate pothole obstacle sprite"""
    img = Image.new('RGBA', (50, 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw pothole (dark brown circle)
    draw.ellipse([(5, 5), (45, 45)], fill=(80, 60, 40, 255))
    
    # Add shadow effect
    draw.ellipse([(10, 10), (40, 40)], fill=(100, 80, 60, 255))
    
    img.save(output_path)
    print(f"✓ Generated pothole sprite: {output_path}")

def generate_cone_sprite(output_path):
    """Generate traffic cone obstacle sprite"""
    img = Image.new('RGBA', (40, 60), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw cone (orange/yellow)
    draw.polygon([(5, 50), (35, 50), (20, 5)], fill=(255, 165, 0, 255))
    
    # Add stripe
    draw.line([(20, 15), (20, 45)], fill=(255, 255, 255, 255), width=3)
    
    img.save(output_path)
    print(f"✓ Generated cone sprite: {output_path}")

def generate_ramp_sprite(output_path):
    """Generate ramp power-up sprite"""
    img = Image.new('RGBA', (50, 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw ramp (yellow)
    draw.polygon([(5, 40), (45, 40), (45, 10)], fill=(255, 255, 0, 255))
    
    # Add border
    draw.polygon([(5, 40), (45, 40), (45, 10)], outline=(200, 200, 0, 255), width=2)
    
    img.save(output_path)
    print(f"✓ Generated ramp sprite: {output_path}")

def generate_invincibility_sprite(output_path):
    """Generate invincibility power-up sprite (skull & crossbones)"""
    img = Image.new('RGBA', (50, 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw skull (white)
    draw.ellipse([(10, 5), (40, 25)], fill=(255, 255, 255, 255))
    
    # Draw eye sockets
    draw.ellipse([(15, 8), (23, 16)], fill=(0, 0, 0, 255))
    draw.ellipse([(27, 8), (35, 16)], fill=(0, 0, 0, 255))
    
    # Draw nose hole
    draw.ellipse([(21, 17), (29, 22)], fill=(0, 0, 0, 255))
    
    # Draw crossbones (white X)
    draw.line([(10, 35), (40, 45)], fill=(255, 255, 255, 255), width=3)
    draw.line([(40, 35), (10, 45)], fill=(255, 255, 255, 255), width=3)
    
    img.save(output_path)
    print(f"✓ Generated invincibility sprite: {output_path}")

def main():
    """Generate all assets"""
    assets_dir = "godot/assets"
    ensure_dir(assets_dir)
    
    print("Generating Vespa Scooter Game assets...")
    print()
    
    # Generate sprites
    generate_scooter_sprite(os.path.join(assets_dir, "scooter.png"))
    generate_pothole_sprite(os.path.join(assets_dir, "pothole.png"))
    generate_cone_sprite(os.path.join(assets_dir, "cone.png"))
    generate_ramp_sprite(os.path.join(assets_dir, "ramp.png"))
    generate_invincibility_sprite(os.path.join(assets_dir, "invincibility.png"))
    
    print()
    print("✓ All assets generated successfully!")

if __name__ == "__main__":
    main()
