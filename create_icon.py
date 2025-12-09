from PIL import Image, ImageDraw

def create_icon():
    """Create an icon for the application"""
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    images = []
    
    for size in sizes:
        width, height = size
        image = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))
        dc = ImageDraw.Draw(image)
        
        # Calculate sizes based on image size
        padding = width // 8
        circle_size = width - (padding * 2)
        
        # Draw gradient circle background
        dc.ellipse(
            [padding, padding, padding + circle_size, padding + circle_size],
            fill='#1e1b4b',
            outline='#a78bfa',
            width=max(2, width // 32)
        )
        
        # Draw clock hands
        center = width // 2
        hand_length = circle_size // 3
        
        # Hour hand (pointing up)
        dc.line(
            [center, center, center, center - hand_length],
            fill='#a78bfa',
            width=max(2, width // 32)
        )
        
        # Minute hand (pointing right)
        dc.line(
            [center, center, center + hand_length, center],
            fill='#93c5fd',
            width=max(1, width // 48)
        )
        
        # Center dot
        dot_size = max(3, width // 16)
        dc.ellipse(
            [center - dot_size, center - dot_size, center + dot_size, center + dot_size],
            fill='#ffffff'
        )
        
        images.append(image)
    
    # Save as ICO file
    images[0].save('icon.ico', format='ICO', sizes=[(img.width, img.height) for img in images])
    print("Icon created successfully: icon.ico")

if __name__ == "__main__":
    create_icon()
