def extract_triangles_from_obj(obj_file, output_file):
    vertices = []
    triangles = []

    with open(obj_file, 'r') as file:
        for line in file:
            parts = line.split()
            if not parts:
                continue
            
            if parts[0] == 'v':  # Vertex line
                vertices.append(list(map(float, parts[1:4])))
            
            elif parts[0] == 'f':  # Face line
                indices = [int(p.split('/')[0]) - 1 for p in parts[1:4]]
                for index in indices:
                    triangles.extend(vertices[index])

    # Save to text file with each coordinate on a new line
    with open(output_file, 'w') as file:
        for value in triangles:
            file.write(f"{value}\n")

    print(f"✅ Triangle coordinates saved to {output_file}")


# 🔹 Example usage
obj_file_path = "model.obj"   # Change this to your actual OBJ file path
output_file_path = "triangles.txt"  # Output text file

extract_triangles_from_obj(obj_file_path, output_file_path)