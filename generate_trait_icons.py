import os
from PIL import Image, ImageDraw

def create_trait_icons():
    output_dir = r"C:\Users\manji\.gemini\antigravity\scratch\ck2_shadows_of_the_blood\shadows_of_the_blood\gfx\traits"
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. sotb_blood_feudist: Crossed bloody daggers on dark red shield
    im1 = Image.new("RGBA", (24, 24), (0, 0, 0, 0))
    d1 = ImageDraw.Draw(im1)
    # Background circular / shield badge
    d1.rectangle([2, 2, 21, 21], fill=(110, 18, 18, 255), outline=(35, 5, 5, 255))
    d1.rectangle([3, 3, 20, 20], fill=(140, 24, 24, 255))
    # Crossed steel daggers
    # Blade 1 (top-left to bottom-right)
    for i in range(12):
        d1.point((5 + i, 5 + i), fill=(225, 230, 240, 255))
        d1.point((6 + i, 5 + i), fill=(180, 190, 205, 255))
    # Blade 2 (top-right to bottom-left)
    for i in range(12):
        d1.point((18 - i, 5 + i), fill=(225, 230, 240, 255))
        d1.point((17 - i, 5 + i), fill=(180, 190, 205, 255))
    # Gold hilts
    d1.line([(3, 4), (5, 6)], fill=(212, 175, 55, 255))
    d1.line([(20, 4), (18, 6)], fill=(212, 175, 55, 255))
    # Blood drips (crimson red at tips)
    d1.point((11, 17), fill=(220, 10, 10, 255))
    d1.point((12, 18), fill=(200, 0, 0, 255))
    d1.point((12, 19), fill=(160, 0, 0, 255))
    im1.save(os.path.join(output_dir, "sotb_blood_feudist.tga"))
    
    # 2. sotb_nemesis_marked: Grim vengeance skull with crosshairs
    im2 = Image.new("RGBA", (24, 24), (0, 0, 0, 0))
    d2 = ImageDraw.Draw(im2)
    d2.rectangle([2, 2, 21, 21], fill=(30, 32, 40, 255), outline=(15, 15, 20, 255))
    # Skull shape
    d2.rectangle([6, 5, 17, 13], fill=(220, 220, 210, 255))
    d2.rectangle([8, 14, 15, 17], fill=(200, 200, 190, 255))
    # Eye sockets (red vengeance glow)
    d2.point((8, 8), fill=(230, 30, 30, 255))
    d2.point((9, 8), fill=(255, 50, 50, 255))
    d2.point((14, 8), fill=(230, 30, 30, 255))
    d2.point((15, 8), fill=(255, 50, 50, 255))
    # Nose & teeth
    d2.point((11, 11), fill=(40, 40, 40, 255))
    d2.point((12, 11), fill=(40, 40, 40, 255))
    d2.line([(9, 16), (14, 16)], fill=(50, 50, 50, 255))
    im2.save(os.path.join(output_dir, "sotb_nemesis_marked.tga"))

    # 3. sotb_shadow_master: Hooded silhouette with glowing eye
    im3 = Image.new("RGBA", (24, 24), (0, 0, 0, 0))
    d3 = ImageDraw.Draw(im3)
    d3.rectangle([2, 2, 21, 21], fill=(22, 18, 32, 255), outline=(10, 8, 15, 255))
    # Hood outline
    d3.polygon([(11, 4), (12, 4), (18, 16), (19, 20), (4, 20), (5, 16)], fill=(45, 38, 65, 255), outline=(15, 10, 25, 255))
    # Dark face recess
    d3.polygon([(11, 8), (12, 8), (15, 14), (8, 14)], fill=(12, 10, 18, 255))
    # Subtle glowing eye
    d3.point((10, 11), fill=(80, 230, 160, 255))
    d3.point((13, 11), fill=(80, 230, 160, 255))
    im3.save(os.path.join(output_dir, "sotb_shadow_master.tga"))

    # 4. sotb_shadow_regent: Golden crown suspended by puppet strings
    im4 = Image.new("RGBA", (24, 24), (0, 0, 0, 0))
    d4 = ImageDraw.Draw(im4)
    d4.rectangle([2, 2, 21, 21], fill=(35, 28, 48, 255), outline=(15, 10, 20, 255))
    # Puppet strings from top
    d4.line([(6, 2), (6, 11)], fill=(180, 180, 190, 255))
    d4.line([(11, 2), (11, 9)], fill=(180, 180, 190, 255))
    d4.line([(17, 2), (17, 11)], fill=(180, 180, 190, 255))
    # Golden crown
    d4.polygon([(5, 12), (5, 17), (18, 17), (18, 12), (15, 14), (11, 10), (8, 14)], fill=(230, 185, 35, 255), outline=(140, 100, 10, 255))
    # Jewels on crown
    d4.point((11, 15), fill=(220, 30, 30, 255)) # Ruby
    d4.point((8, 15), fill=(30, 140, 220, 255)) # Sapphire
    d4.point((15, 15), fill=(40, 200, 80, 255)) # Emerald
    im4.save(os.path.join(output_dir, "sotb_shadow_regent.tga"))

    # 5. sotb_cursed_bloodline: Fractured crest with dark flames
    im5 = Image.new("RGBA", (24, 24), (0, 0, 0, 0))
    d5 = ImageDraw.Draw(im5)
    d5.rectangle([2, 2, 21, 21], fill=(45, 15, 40, 255), outline=(20, 5, 20, 255))
    # Shield
    d5.polygon([(4, 4), (19, 4), (19, 14), (11, 20), (4, 14)], fill=(85, 25, 75, 255), outline=(30, 10, 30, 255))
    # Crack across shield
    d5.line([(6, 5), (10, 10), (13, 9), (16, 17)], fill=(220, 80, 220, 255))
    d5.point((11, 11), fill=(255, 200, 255, 255))
    im5.save(os.path.join(output_dir, "sotb_cursed_bloodline.tga"))

    # 6. sotb_atoned_bloodline: Radiant silver & gold holy halo / cross
    im6 = Image.new("RGBA", (24, 24), (0, 0, 0, 0))
    d6 = ImageDraw.Draw(im6)
    d6.rectangle([2, 2, 21, 21], fill=(25, 45, 60, 255), outline=(10, 20, 30, 255))
    # Golden rays
    d6.line([(11, 3), (11, 20)], fill=(240, 205, 70, 255))
    d6.line([(3, 11), (20, 11)], fill=(240, 205, 70, 255))
    d6.line([(6, 6), (16, 16)], fill=(210, 180, 50, 255))
    d6.line([(16, 6), (6, 16)], fill=(210, 180, 50, 255))
    # Pure silver cross
    d6.rectangle([10, 5, 12, 17], fill=(255, 255, 255, 255), outline=(180, 190, 205, 255))
    d6.rectangle([7, 8, 15, 10], fill=(255, 255, 255, 255), outline=(180, 190, 205, 255))
    im6.save(os.path.join(output_dir, "sotb_atoned_bloodline.tga"))
    
    print("Successfully generated all 6 CK2 trait pixel art icons (.tga)!")

if __name__ == "__main__":
    create_trait_icons()
