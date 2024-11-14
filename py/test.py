import webcolors
rgb = (51, 55, 63)

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

hex_color = rgb_to_hex(rgb)
print(f"HEX: {hex_color}")
