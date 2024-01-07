from PIL import Image, ImageDraw

def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def draw_triangle(draw, points):
    draw.polygon(points, outline="black")

def sierpinski_triangle(draw, points, degree):
    if degree == 0:
        draw_triangle(draw, points)
    else:
        p1 = midpoint(points[0], points[1])
        p2 = midpoint(points[1], points[2])
        p3 = midpoint(points[0], points[2])

        sierpinski_triangle(draw, [points[0], p1, p3], degree - 1)
        sierpinski_triangle(draw, [p1, points[1], p2], degree - 1)
        sierpinski_triangle(draw, [p3, p2, points[2]], degree - 1)

def main():
    # Set the size of the image
    width, height = 400, 400

    # Create a white image
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Define the vertices of the initial equilateral triangle
    vertices = [(200, 350), (50, 50), (350, 50)]

    # Set the recursion depth
    recursion_depth = 6

    # Draw the Sierpinski Triangle on the image
    sierpinski_triangle(draw, vertices, recursion_depth)

    # Save or display the image
    image.save("sierpinski_triangle.png")

if __name__ == "__main__":
    main()