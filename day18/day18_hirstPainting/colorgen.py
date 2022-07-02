import colorgram

colors = colorgram.extract('oddinary.jpg', 10)
print(colors)


def color_gen():
    rgb_colors = []

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)

    return rgb_colors
