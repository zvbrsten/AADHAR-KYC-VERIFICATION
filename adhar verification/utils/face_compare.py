import torch
from torchvision import transforms
from facenet_pytorch import InceptionResnetV1
from utils.face_detect import extract_face  

resnet = InceptionResnetV1(pretrained='vggface2').eval()


def get_embedding(face_tensor):
    if face_tensor.ndim == 3:
        face_tensor = face_tensor.unsqueeze(0)  # Shape: [1, 3, 160, 160]
    with torch.no_grad():
        embedding = resnet(face_tensor)
    return embedding[0]

def cosine_similarity(a, b):
    return torch.nn.functional.cosine_similarity(a.unsqueeze(0), b.unsqueeze(0)).item()

def compare_faces(image1_path, image2_path):
    face1 = extract_face(image1_path)  # Tensor
    face2 = extract_face(image2_path)  # Tensor

    emb1 = get_embedding(face1)
    emb2 = get_embedding(face2)

    return cosine_similarity(emb1, emb2)
