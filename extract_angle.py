import numpy as np

def angle_between_vectors(v1, v2):
    """Calculate the angle (in degrees) between two vectors."""
    v1 = np.array(v1) / np.linalg.norm(v1)  # Normalize vector
    v2 = np.array(v2) / np.linalg.norm(v2)  # Normalize vector
    dot_product = np.dot(v1, v2)
    angle_radians = np.arccos(np.clip(dot_product, -1.0, 1.0))  # Clip to avoid numerical errors
    return np.degrees(angle_radians)  # Convert to degrees

def extract_angles(obj_file, output_file, comparison_vector):
    vertices = []
    angles = []

    with open(obj_file, 'r') as file:
        for line in file:
            parts = line.split()
            if not parts:
                continue
            
            if parts[0] == 'v':  # Vertex line
                vertices.append(list(map(float, parts[1:4])))
            
            elif parts[0] == 'f':  # Face line
                indices = [int(p.split('/')[0]) - 1 for p in parts[1:4]]
                triangle = [vertices[i] for i in indices]

                # Compute normal using cross product
                A, B, C = np.array(triangle[0]), np.array(triangle[1]), np.array(triangle[2])
                AB = B - A
                AC = C - A
                normal = np.cross(AB, AC)
                normal = normal / np.linalg.norm(normal)  # Normalize the normal vector

                # Compute angle between normal and comparison vector
                angle = angle_between_vectors(normal, comparison_vector)
                angles.append(angle)

    # Save only angles to text file (one per line)
    with open(output_file, 'w') as file:
        for angle in angles:
            file.write(f"{angle:.2f}\n")  # Writes only the angle

    print(f"✅ Angles saved to {output_file}")

# 🔹 Example usage
obj_file_path = "model.obj"   # Change this to your actual OBJ file path
output_file_path = "angles.txt"  # Output text file
comparison_vector = [1, 1, 1]  # Example comparison vector

extract_angles(obj_file_path, output_file_path, comparison_vector)